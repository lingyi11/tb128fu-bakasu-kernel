# TB128FU BakaSU + SuSFS 内核

联想小新 Pad 2022（TB128FU / P89990JA1 / grass / SM6225，Android 12，ZUI 13.5.476）
的内核编译工作流。

- 内核源码：`Roynas-Android-Playground/kernel_lenovo_tb128fu`（社区 4.19.325 树，锁定 commit `e26c9a738`）
- Root 方案：BakaSU（原 ReSukiSU）`v4.2.0-rc3`，**SUSFS Inline Hook** 模式
- 隐藏增强：SuSFS v2.3.x 内核侧补丁（`patches/susfs_patch_to_4.19.patch`）＋ inline hook 脚本
- 工具链：AOSP clang r416183b（12.0.5）＋ aarch64-linux-gnu binutils

## 触发方式

Actions → *Build TB128FU kernel (BakaSU + SuSFS)* → Run workflow
（`mode=patch` 只做打补丁自检，`mode=full` 完整编译）

产物：`Image.gz`、`config.txt`、`System.map`、构建日志。

## 刷机

用原厂 boot.img 的 ramdisk 重打包，`fastboot flash boot_a/boot_b`（见本地 `刷机说明.md`）。

## 许可

- 内核侧补丁来自 [simonpunk/susfs4ksu](https://gitlab.com/simonpunk/susfs4ksu)（GPL-2.0）
- inline hook 脚本整理自 [JackA1ltman/NonGKI_Kernel_Build_2nd](https://github.com/JackA1ltman/NonGKI_Kernel_Build_2nd)（GPL-3.0）
- BakaSU 内核部分 GPL-2.0
