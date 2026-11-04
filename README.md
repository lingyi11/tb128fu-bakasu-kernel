# TB128FU BakaSU + SuSFS 内核

联想小新 Pad 2022（TB128FU / P89990JA1 / grass / SM6225，Android 12，ZUI 13.5.476）
的内核编译工作流。

- 内核源码：`Roynas-Android-Playground/kernel_lenovo_tb128fu`（社区 4.19.325 树，锁定 commit `e26c9a738`）
- Root 方案：BakaSU（原 ReSukiSU）`v4.2.0-rc3`，**SUSFS Inline Hook** 模式
- 隐藏增强：SuSFS v2.3.0 内核侧补丁（`patches/susfs_v2.3.0_4.19_grass.patch`）＋ inline hook 脚本
- 工具链：AOSP clang r416183b（12.0.5）＋ aarch64-linux-gnu binutils

## 零费用设计

| 项目 | 做法 | 费用 |
|---|---|---|
| 计算分钟 | 公开仓库 + 标准 `ubuntu-22.04` runner | 0 |
| 构建产物 | 发布到 **GitHub Release 附件**，不用 `upload-artifact` | 0 |
| 留存 | 自动只保留最近 3 个 release | 0 |
| 缓存 | 不使用 actions/cache | 0 |

> Actions 的 **artifact 存储**按 GB·月 计费（Free 计划 500 MB 额度），而 **Release 附件**不计入该额度，
> 所以产物一律走 Release。

## 触发方式

Actions → *Build TB128FU kernel (BakaSU + SuSFS)* → Run workflow

| 输入 | 说明 |
|---|---|
| `variant` | `bakasu`（BakaSU+SuSFS）、`bakasu-nosusfs`（BakaSU 手动 hook，无 SuSFS）、`vanilla`（纯净社区树，用于排查） |
| `mode` | `full` 完整编译；`patch` 只打补丁自检 |
| `bakasu_ref` | BakaSU tag/commit，默认 `v4.2.0-rc3` |
| `kernel_commit` | 内核提交，默认 `e26c9a738` |

产物在 **Releases** 页：`Image.gz` + `config.txt` + `SHA256SUMS.txt`。

## 刷机

用原厂 boot.img 的 ramdisk/DTB 重打包（`repack_boot.ps1`），再
`fastboot flash boot_a/boot_b`（详见本地 `刷机说明.md`）。

## 许可

- 内核侧补丁来自 [simonpunk/susfs4ksu](https://gitlab.com/simonpunk/susfs4ksu)（GPL-2.0）
- inline hook 脚本整理自 [JackA1ltman/NonGKI_Kernel_Build_2nd](https://github.com/JackA1ltman/NonGKI_Kernel_Build_2nd)（GPL-3.0）
- BakaSU 内核部分 GPL-2.0
