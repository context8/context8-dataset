# pytorch closed issues with explicit PR/commit links (sample up to 50)
- entries: 2

1. Issue #168303 — Inductor codegen is missing support for CPPScheduling (closed 2025-11-21T12:18:08Z)
   - Issue: https://github.com/pytorch/pytorch/issues/168303
   - Fix: PR #167781 https://github.com/pytorch/pytorch/pull/167781
   - Code excerpts:     - test/inductor/test_cpu_cpp_wrapper.py: +        BaseTest("test_bernoulli1_combo_kernels_False"), +        BaseTest("test_bernoulli1_combo_kernels_True"),

2. Issue #168255 — DTensor not cache hitting for torch.stack (and likely other ops involving lists) (closed 2025-11-21T16:51:58Z)
   - Issue: https://github.com/pytorch/pytorch/issues/168255
   - Fix: PR #168264 https://github.com/pytorch/pytorch/pull/168264
   - Code excerpts:     - test/cpp/jit/test_custom_operators.cpp: +  auto& ops = getAllOperatorsFor(Symbol::fromQualString("foo::bar")); +  auto& ops = +      getAllOperatorsFor(Symbol::fromQualString("foo::bar_with_schema")); +  auto& ops = getAllOperatorsFor(Symbo

