Web Components
==============

* Custom elements (自定义元素)：允许定义自定义元素 ``<custom-element>`` 和他的行为
* Shadow DOM (影子 DOM)：允许将组件内的元素与文档 DOM 分开呈现，保持元素功能私有
* HTML template (HTML 模板)：复用 HTML 结构

基本用法：

1. 创建一个类 ``class XXXElement extends HTMLElement`` 定义自定义元素的行为
2. 使用 ``CustomElementRegistry.define()`` 注册自定义元素
3. 如果需要，使用 ``Element.attachShadow()`` 方法将 shadow DOM 附加到自定义元素上
4. 如果需要，使用 ``<template>`` 和 ``<solt>`` 定义 HTML 模板，再次使用常规 DOM 方法克隆模板并附加到组件 DOM 中。
5. 使用您定义的自定义元素，就像常规 HTML 元素那样

准备自定义元素的类
------------------

.. code:: js

    class CustomElement extends HTMLElement {
      constructor() {
        super() // 必须先调用父类构造

        var shadow = this.attachShadow({ mode: 'closed' }) // closed 就是 shadow DOM
        var template = document.getElementById('template').content // 取 <template> 的 content 对象
        shadow.appendChild(template.cloneNode(true)) // 深拷贝节点并附加进组件 DOM
      }
    }

注册自定义元素
--------------

.. note::
    | 自定义组件的名字应该符合 DOMString 标准
    | 自定义组件的名字不能是单个单词，并且其中 `必须含有短横线 <https://html.spec.whatwg.org/#valid-custom-element-name>`_

.. code:: js

    window.customElements.define('custom-elem', CustomElement)

接着就可以使用该元素了：

.. code:: html

    <custom-elem></custom-elem>

自定义元素生命周期
--------------------

- ``attributeChangedCallback`` 元素属性发生变化

attributeChangedCallback
^^^^^^^^^^^^^^^^^^^^^^^^

.. note:: 下面都是类成员

.. code:: js

    // 需要监听的属性列表
    static get observedAttributes() { return ['attr', 'names'] }

.. code:: js

    // 回调函数
    attributeChangedCallback(name, oldvalue, newvalue) {
      // name: 发生改变的属性名字
      // oldvalue: 旧值
      // newvalue: 新值
    }
