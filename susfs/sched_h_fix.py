#!/usr/bin/env python3
"""Insert SuSFS task_struct fields into include/linux/sched.h.

The upstream 4.19 SuSFS patch assumes Android-common KABI reserve macros;
the Lenovo tree only has a subset, so those two hunks fail. We insert the
two fields directly before randomized_struct_fields_end instead.
"""
import os
import sys

path = "include/linux/sched.h"
if not os.path.exists(path):
    sys.exit("sched.h not found")

src = open(path, "r", encoding="utf-8").read()
if "susfs_task_state" in src:
    print("sched.h already patched")
else:
    marker = "\n\trandomized_struct_fields_end"
    block = (
        "\n#if defined(CONFIG_KSU_SUSFS)\n"
        "\tu64 susfs_task_state;\n"
        "\tu64 susfs_last_fake_mnt_id;\n"
        "#endif\n"
    )
    if marker not in src:
        sys.exit("randomized_struct_fields_end marker not found")
    src = src.replace(marker, block + marker, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(src)
    print("inserted susfs fields into task_struct")

rej = "include/linux/sched.h.rej"
if os.path.exists(rej):
    os.remove(rej)
    print("removed sched.h.rej")
