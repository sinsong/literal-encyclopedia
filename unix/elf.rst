ELF 可执行可链接文件格式
================================================================================

ELF 头
--------------------------------------------------------------------------------

===============  ===========================
element          解释
===============  ===========================
``e_ident``      ELF 文件标记 EI_NIDENT 字节
``e_type``       文件类型
``e_machine``    机器体系结构
``e_version``    ELF 格式版本
``e_entry``      该文件入口点
``e_phoff``      program 表的文件位置
``e_shoff``      section 表的文件位置
``e_flags``      
``e_ehsize``     
``e_phentsize``  program 项目大小
``e_phnum``      program 表
``e_shentsize``  section 项目大小
``e_shnum``      section 个数
``e_shstrndx``   section 字符串表索引
===============  ===========================

``e_ident`` 前 4 个字节应该与字符串 ``ELFMAG`` 相等。

``e_ident[4]`` 指定 32 位还是 64 位： ``ELFCLASS..`` ：

================  =====
ELFCLASS          解释
================  =====
``ELFCLASSNONE``  未知
``ELFCLASS32``    32 位
``ELFCLASS64``    64 位
================  =====

``e_ident[5]`` 指定文件数据格式 ``ELFDATA..`` ：

===============  ======================
ELFDATA          解释
===============  ======================
``ELFDATANONE``  未知
``ELFDATA2LSB``  2 进制补码，小端字节序
``ELFDATA2MSB``  2 进制补码，大端字节序
===============  ======================

``e_type`` 指定文件格式：

===========  =============================
``e_type``   解释
===========  =============================
``ET_NONE``  未知格式
``ET_REL``   可重定位文件 relocatable file
``ET_EXEC``  可执行文件 executable file
``ET_DYN``   共享对象文件 shared object
``ET_CORE``  核心文件 core file
===========  =============================

从文件中加载 program 表和 section 表，使用 ``e_phoff`` 和 ``e_shoff``，他们的意义是文件中的偏移量：

.. code:: c

    // 加载 section 表
    lseek(fd, e_shoff, SEEK_SET);
    assert(e_shentsize == sizeof(Elf64_Shdr))
    // e_shentsize: section 项目大小
    // e_shnum: section 项目个数
    read(fd, shdr, e_shentsize * e_shnum);

节
--------------------------------------------------------------------------------

节的名字 ``sh_name`` 储存在 ``.shstrtab`` 中，使用 ELF 头的 ``e_shstrndx`` 来定位这个节的索引，提前加载到内存。
``sh_name`` 的意义是对应的字符串表中的偏移量，打印节名字的代码如下：

.. code:: c

    // shstrtab: 加载好的 .shstrtab 节
    puts(shstrtab + shent->sh_name);

符号表中的 ``st_name`` 由字符串表 ``.strtab`` 解释，由于 ``.shstrtab`` 和 ``.strtab`` 都带 ``SHT_STRTAB`` 标记，应该判断节的名字来加载字符串表：

.. code:: c

    if ( strcmp((shstrtab + shent->sh_name), ".strtab") == 0 )
    {
        // 加载 .symtab 表
    }

并且 ``st_name`` 的解释同理，为 ``.strtab`` 中的偏移量：

.. code:: c

    puts(strtab + symbol->st_name);

常见节的名字

============= =====================
section       解释
============= =====================
``.bss``      数据（未初始化）
``.comment``  版本控制信息
``.data``     数据（已初始化）
``.debug``    调试信息
``.dynamic``  动态链接信息
``.dynstr``   动态链接字符串表
``.dynsym``   动态链接符号表
``.fini``     正常退出代码
``.got``      全局偏移表 GOT
``.hash``     符号散列表
``.init``     程序启动代码
``.intrep``   解释器路径 （动态链接器）
``.line``     行号
``.note``     note
``.plt``      程序链接表 PLT
``.relNAME``  重定位信息
``.relaNAME`` 重定位信息   
``.rodata``   数据（只读）
``.shstrtab`` 节(section)名 字符串表
``.strtab``   字符串表 与符号表项目管理的名字
``.symtab``   符号表
``.text``     Program text 程序代码
``.en_frame`` C++ 异常处理信息
============= =====================