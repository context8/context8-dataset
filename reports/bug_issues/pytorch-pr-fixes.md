# pytorch merged PRs referencing issues via "Fixes #" (expanded set with issue context)
- entries: 202

1. Issue #163597 —  (closed )
   - Issue detail: ### Overview Bug in built-in `F. scaled_dot_product_attention` when using `mps` device on version 2.8.0. Affects non-contiguous tensors which get dispatched to the fast SDPA MPS implementation. Can be reproduced by the following script ```python import math import torch import torch.nn.functional as F def manual_scaled_dot_product_attention( query, key, value, attn_mask=None, dropout_p=0.0, is_causal=False, scale=None, enable_gqa=False ) -> torch.Tensor: """From...
   - Issue: https://github.com/pytorch/pytorch/issues/163597
   - Fix PR #164364 — [SDPA] [MPS] Fixes regression in 2.8.0 for scaled_dot_product_attention using mps
   - PR: https://github.com/pytorch/pytorch/pull/164364
   - Code excerpts:     - aten/src/ATen/native/mps/kernels/Attention.metal: +    const constant uint3& qkv_head_strides [[buffer(6)]], +    const constant uint3& qkv_seq_strides [[buffer(7)]], +  const uint q_head_stride = qkv_head_strides.x; +  const uint q_seq_stride = qkv_



2. Issue #165892 —  (closed )
   - Issue detail: ### 🐛 Describe the bug ``` import torch A = torch.rand((1, 1024, 1024), device="cuda", dtype=torch.float16) B = torch.rand((1, 1024, 1024), device="cuda", dtype=torch.float16) @torch.compile def linear(weight, input): return torch.bmm(input, weight, out_dtype=torch.float32) linear(A, B) ``` Output: ``` ... File "/usr/local/lib/python3.10/dist-packages/torch/_inductor/graph.py", line 1279, in call_function out = lowerings[target](*args, **kwargs) # type: ignore[index] File...
   - Issue: https://github.com/pytorch/pytorch/issues/165892
   - Fix PR #166922 — [Inductor] No longer throw error in bmm out_dtype lowering due to tem…
   - PR: https://github.com/pytorch/pytorch/pull/166922
   - Code excerpts:     - test/inductor/test_max_autotune.py: +    @unittest.skipIf(config.cpp_wrapper, "out_dtype override not supported for AOTI") +    @unittest.skipIf(TEST_WITH_ROCM, "out_dtype override only available on NVIDIA") +    def test_bmm_out_dtype(



3. Issue #166176 —  (closed )
   - Issue detail: Originally reported in an internal model. ```python import torch def fn(x): torch._dynamo.graph_break() with torch.no_grad(): with torch.no_grad(): torch._dynamo.graph_break() return x + 1 inp = torch.ones(3) opt_m = torch.compile(fn, backend="eager") opt_m(inp) ``` gives error ``` ... File "/data/users/williamwen/pytorch4/torch/_dynamo/symbolic_convert.py", line 1030, in handle_graph_break + self.create_call_resume_at( ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File...
   - Issue: https://github.com/pytorch/pytorch/issues/166176
   - Fix PR #166924 — [dynamo] fix keyerror in resume_execution,  fix store attr
   - PR: https://github.com/pytorch/pytorch/pull/166924
   - Code excerpts:     - test/dynamo/test_ctx_manager.py: +    def test_311_resume_block_keyerror(self): +        # https://github.com/pytorch/pytorch/issues/162313 +        flag = True + +        def fn(x): +            x = x + 1 +            torch._dynamo.



4. Issue #165341 —  (closed )
   - Issue detail: Current design not working too well. For example, we think Inductor doesn't guarantee a way to get FakeTensors for an IR node, but we rely on needing that. In PyTorch 2.9 we're going to monkeypatch PyTorch to work around this. We should use our learnings to evolve the design for PyTorch 2.10. cc @voznesenskym @penguinwu @EikanWang @jgong5 @Guobing-Chen @XiaobingSuper @zhuhaozhe @blzheng @wenzhe-nrv @jiayisunx @ipiszy @chenyang78 @kadeng @muchulee8 @amjames @chauhang @aakhundov @coconutruben
   - Issue: https://github.com/pytorch/pytorch/issues/165341
   - Fix PR #166967 — [Graph Partition] move custom rules to inductor config (#166458)
   - PR: https://github.com/pytorch/pytorch/pull/166967
   - Code excerpts:     - test/inductor/test_cudagraph_trees.py: +            def baz(x: torch.Tensor) -> torch.Tensor: +            def _(x): +            # custom_should_partition_ops takes effect which lead to 2 partitions +            torch._inductor.config.cus



5. Issue #163483 —  (closed )
   - Issue detail: ### 🐛 Describe the bug I try the `all_gather` operation on a tensor with `channels_last` format , then I found the memory ordering of output is changed so that the output and input are not aligned. This is not as expected. I think it's a BUG. The reproducible minimal example, test.py is: ``` import torch torch.distributed.init_process_group(backend='nccl') rank = torch.distributed.get_rank() world_size = torch.distributed.get_world_size() torch.cuda.set_device(rank) x = torch.arange(0,...
   - Issue: https://github.com/pytorch/pytorch/issues/163483
   - Fix PR #163987 — [dist] handle discontiguous allgather/reducescatter inputs
   - PR: https://github.com/pytorch/pytorch/pull/163987
   - Code excerpts:     - test/distributed/test_c10d_nccl.py: +    @requires_nccl() +    @skip_if_lt_x_gpu(2) +    def test_allgather_noncontig(self): +        store = dist.FileStore(self.file_name, self.world_size) +        dist.init_process_group( +           



6. Issue #161324 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Transferring data from two 2D tensors on one rank into a single 2D tensor on another rank using batch_isend_irecv and tensor views fails silently, the output contains inconsistent data. This issue occurs silently without explicit errors. Note: This does not happen if entire 2D tensor is used for the communication.Only, happens when slices are used. E.g ```if rank == 0: # Sender rank local_tensor = torch.randn(batch_size, total_columns) dst_t1 = local_tensor[:,...
   - Issue: https://github.com/pytorch/pytorch/issues/161324
   - Fix PR #163981 — [c10d] P2P tensors must be dense
   - PR: https://github.com/pytorch/pytorch/pull/163981
   - Code excerpts:     - test/distributed/test_c10d_nccl.py: +    @requires_nccl() +    @skip_if_lt_x_gpu(3) +    @skip_if_rocm_multiprocess +    def test_send_recv_non_dense_tensor(self): +        store = c10d.FileStore(self.file_name, self.world_size) +      



7. Issue #147841 —  (closed )
   - Issue detail: ### 🐛 Describe the bug I encountered an issue while trying to pickle an instance of a dynamically generated class using `make_opaque_bitwise_fn` from `torch.utils._sympy.functions`. ``` import pickle import sympy from torch.utils._sympy.functions import make_opaque_bitwise_fn # Generate the bitwise_and function class BitwiseFn_bitwise_and = make_opaque_bitwise_fn("bitwise_and", "and_") # Create an instance of the dynamically generated class x = BitwiseFn_bitwise_and(sympy.Symbol('a'),...
   - Issue: https://github.com/pytorch/pytorch/issues/147841
   - Fix PR #163861 — fix pickling for BitwiseFn
   - PR: https://github.com/pytorch/pytorch/pull/163861
   - Code excerpts:     - test/inductor/test_compile_subprocess.py: +            while True: +                start_stat_compiled_runs = _AsyncFxCompile._stat_compiled_runs +                if _AsyncFxCompile._stat_compiled_runs - start_stat_compiled_runs == 2: +     



8. Issue #156688 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Llama3 workloads from [Intel AI Reference Models](https://github.com/intel/ai-reference-models) failed with PyTorch 2025-06-22 nightly wheel. It seems that there is something wrong with the latest flex attention implementation. The suspected guilty commit: https://github.com/pytorch/pytorch/commit/ccc6279b4086d55cd1f7e2d699473478610d8a7b Error logs: ``` [run_202506220900233]:Traceback (most recent call last): [run_202506220900233]: File...
   - Issue: https://github.com/pytorch/pytorch/issues/156688
   - Fix PR #157519 — [cherry-pick] [fake tensor] fix issue of no attribute tags (#156689)
   - PR: https://github.com/pytorch/pytorch/pull/157519
   - Code excerpts:     - test/test_fake_tensor.py: +    def test_no_tag_func(self): +        import functools + +        from torch.nn.attention.flex_attention import _identity, flex_attention + +        def create_attention(score_mod, block_mask, ena



9. Issue #156261 —  (closed )
   - Issue detail: ### 🐛 Describe the bug In some circumstance, `torch._foreach_copy_` causes illegal cuda memory access. ```python import torch def test_torch(): _buffer =torch.zeros(27000008 * 192, device="cuda", dtype=torch.float32) buffer = _buffer.view(27000008, 192) src = torch.randn(27000008, 192, device="cuda", dtype=torch.bfloat16) torch._foreach_copy_((buffer,), (src,)) torch.cuda.synchronize() if __name__ == '__main__': print(f"{torch.__version__=}") test_torch() ``` Error: ```...
   - Issue: https://github.com/pytorch/pytorch/issues/156261
   - Fix PR #158238 — Fix #156261 _foreach_copy indexing
   - PR: https://github.com/pytorch/pytorch/pull/158238
   - Code excerpts:     - aten/src/ATen/native/cuda/ForeachBinaryOpList.cu: +      int64_t chunk_size, +                Copy<scalar_t, scalar_t>());



10. Issue #158376 —  (closed )
   - Issue detail: ### 🐛 Describe the bug ## To Reproduce Running on A10 ### 1. Install torch 2.8 RC: > python3 -m pip uninstall -y torch torchvision torchaudio && python3 -m pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/test/cu126 ### 2. Install transformers > git clone https://github.com/huggingface/transformers.git && cd transformers && git fetch origin && git checkout 6017f5e8 && pip install -e .[torch,testing] ### 3. Running test > RUN_SLOW=1 python3...
   - Issue: https://github.com/pytorch/pytorch/issues/158376
   - Fix PR #158655 — [cherry-pick] Unify torch.tensor and torch.ops.aten.scalar_tensor behavior (#158537)
   - PR: https://github.com/pytorch/pytorch/pull/158655
   - Code excerpts:     - aten/src/ATen/ScalarOps.cpp: +  scalar_t value{}; + +  if constexpr (std::is_same_v<scalar_t, at::Half> || +                std::is_same_v<scalar_t, at::BFloat16> || +                std::is_same_v<scalar_t, at::Float8_e5m2> || +



11. Issue #157626 —  (closed )
   - Issue detail: ### 🐛 Describe the bug We have identified 5 tests that are failing due to segmentation fault on AAarch64 neoverse-v1. ( neoverse-v2 i.e. aws c8g seems to be unaffected ). How we identified this - Our workflow is to test the unit tests with a manywheel build where as linux-aarch64.yml workflow builds inside a jammy container. This is why these tests are currently passing in CI. ``` test_ops.py::TestCommonCPU::test_noncontiguous_samples_grid_sampler_2d_cpu_float32 Fatal Python error:...
   - Issue: https://github.com/pytorch/pytorch/issues/157626
   - Fix PR #158445 — [cherry-pick] Fix AArch64 segfaults by disabling strict-aliasing in GridSamplerKernel for GCC 12 and above
   - PR: https://github.com/pytorch/pytorch/pull/158445
   - Code excerpts:     - aten/src/ATen/native/cpu/GridSamplerKernel.cpp: +// fixes segfaults for GCC >= 12 on some AArch64 cpus https://github.com/pytorch/pytorch/issues/157626 +#if defined(__GNUC__) && __GNUC__ >= 12 && defined(__aarch64__) +#pragma GCC push_options +#pra



12. Issue #155006 —  (closed )
   - Issue detail: Repro: https://gist.github.com/zou3519/87aa4e42162a5bfd928d915f83aad44c we probably need to escape all the " See https://github.com/pytorch/ao/issues/2239#issuecomment-2935600458 for how we ran into this I think the "autotune_at_compile_time" is required for this because it constructs some outer block string with """ EDIT: Note for the release manager. This is to fix a regression against 2.7.1 ([category 1](https://github.com/pytorch/pytorch/issues/156745)). We changed how vLLM uses...
   - Issue: https://github.com/pytorch/pytorch/issues/155006
   - Fix PR #157454 — [inductor][user triton] sanitize triple-quoted docstrings in kernel definitions
   - PR: https://github.com/pytorch/pytorch/pull/157454
   - Code excerpts:     - test/inductor/test_triton_kernels.py: +from torch.testing._internal.common_utils import ( +    parametrize, +    skipIfRocm, +    skipIfWindows, +    skipIfXpu, +) +    @requires_gpu +    @inductor_config.patch({"triton.autotune_at_compil



13. Issue #146782 —  (closed )
   - Issue detail: Hi torch team, Starting from einops 0.8.1, you can test torch against einops with: ```shell # install numpy, einops, pytest and torch python -m einops.tests.run_tests numpy torch ``` and I suggest having this in torch's CI. There are a couple of motivations: 1. einops tests actually reveal regressions in frameworks (happened several times, not in torch) 2. it is hard within einops to test against more advanced features like torch.compile, because most of engineering/regressions happen on...
   - Issue: https://github.com/pytorch/pytorch/issues/146782
   - Fix PR #157588 — Add einops x torch.compile testing in PyTorch CI (#157416)
   - PR: https://github.com/pytorch/pytorch/pull/157588
   - Code excerpts:     - .ci/pytorch/test.sh: +test_einops() { +  pip install einops==0.6.1 +  time python test/run_test.py --einops --verbose --upload-artifacts-while-running +  pip install einops==0.7.0 +  time python test/run_test.py --einops 



14. Issue #147376 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Multiple days-in-a-row nightly binary builds for windows are broken. https://hud.pytorch.org/hud/pytorch/pytorch/nightly ### Versions nightly cc @malfet @seemethere @ptrblck @msaroufim @eqy
   - Issue: https://github.com/pytorch/pytorch/issues/147376
   - Fix PR #152967 — [ATen][CUDA] Optimize 128 bit vectorization
   - PR: https://github.com/pytorch/pytorch/pull/152967
   - Code excerpts:     - aten/src/ATen/native/cuda/CUDALoops.cuh: +#ifndef USE_ROCM +// To save on binary size of libtorch_cuda.so, we split the vectorized_elementwise_kernel +// into two: one for vec_size=8 and one for vec_size=[2, 4], since vec8 is going to be +//



15. Issue #151188 —  (closed )
   - Issue detail: I think this should go into 2.7.1. This was the reason that sglang had torch.compile caching issues and the fix is very simple. cc @chauhang @penguinwu @ydwu4 @bdhirsh
   - Issue: https://github.com/pytorch/pytorch/issues/151188
   - Fix PR #153304 — Mark auto_functionalized HOPs as cacheable (#151194)
   - PR: https://github.com/pytorch/pytorch/pull/153304
   - Code excerpts:     - test/inductor/test_codecache.py: +    @config.patch({"fx_graph_cache": True}) +    @config.patch({"fx_graph_remote_cache": False}) +    @parametrize("variant", ("v1", "v2")) +    def test_auto_functionalized_caching(self, variant): +



16. Issue #150367 —  (closed )
   - Issue detail: ### 🚀 The feature, motivation and pitch I recently was forced to implement some composite custom ops with CompositeImplicitAutograd on top of another, more general custom op, for ONNX/TRT export purposes(the original op was used for both forward and backward and therefore had sequence output type that neither onnxruntime-extensions nor TRT can handle). The idea was to use custom_translation_table with those composite ops for export. Now it looks like I would need to implement some additional...
   - Issue: https://github.com/pytorch/pytorch/issues/150367
   - Fix PR #153168 — [ONNX] Update decomposition logic to loop over onnx registry
   - PR: https://github.com/pytorch/pytorch/pull/153168
   - Code excerpts:     - test/onnx/exporter/test_api.py: +    def test_custom_translation_table_supports_custom_op_with_its_decomp(self): +        with torch.library._scoped_library("mylib", "FRAGMENT") as lib: +            torch.library.define( +          



17. Issue #149422 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Pip-installed pytorch limits threads to 1 when setting GOMP_CPU_AFFINITY, while a pytorch build from source code will not have this problem. The pip-installed pytorch will use a bundled GOMP. There is a cpp case can reproduce it. ``` #include <stdio.h> #include <omp.h> #include <torch/torch.h> int main() { printf("omp_get_max_threads %d\n", omp_get_max_threads()); printf("at::get_num_threads %d\n", at::get_num_threads()); return 0; } ``` compile command ```g++...
   - Issue: https://github.com/pytorch/pytorch/issues/149422
   - Fix PR #153518 — [CD] Fix the libgomp twice load issue (#150084)
   - PR: https://github.com/pytorch/pytorch/pull/153518
   - Code excerpts:     - .ci/manywheel/build_common.sh: +            # Keep the so number for XPU dependencies and libgomp.so.1 to avoid twice load +            elif [[ "$DESIRED_CUDA" == *"xpu"* || "$filename" == "libgomp.so.1" ]]; then



18. Issue #151157 —  (closed )
   - Issue detail: ### 🐛 Describe the bug `test_distinfo_license` checkes if `LICENSE` file exists under `torch-<version>.dist-info/` in the wheel. After https://github.com/pypa/setuptools/commit/ef9b8e5c5eec50853c4cd2ceeccbf5f963172560 ([setuptools v77.0](https://github.com/pypa/setuptools/releases/tag/v77.0.0)), `<pkg>.dist-info/{LICENSE,NOTICE}` have been renamed to `<pkg>.dist-info/licenses/{LICENSE,NOTICE}`, cause the test to fail. ### Versions - cc @malfet @seemethere @mruberry @ZainRizvi
   - Issue: https://github.com/pytorch/pytorch/issues/151157
   - Fix PR #153581 — Fix license check for setuptools>=77
   - PR: https://github.com/pytorch/pytorch/pull/153581
   - Code excerpts:     - test/test_license.py: +        # setuptools renamed *dist-info/LICENSE to *dist-info/licenses/LICENSE sicne 77.0 +        license_file = os.path.join(distinfo[0], "licenses", "LICENSE") +        if not os.path.exists(licen



19. Issue #148883 —  (closed )
   - Issue detail: The same hardware and software environment, only the versions of PyTorch+ROCm are different. Use ComfyUI to run Hunyuan text to video： ComfyUI：v0.3.24 ComfyUI plugin: teacache 49frames 480x960 20steps CPU：i5-7500 GPU：AMD 7900XT 20GB RAM：32GB PyTorch2.6+ROCm6.2.4 Time taken: 348 seconds 14.7s/it The VAE Decode Tiled node (parameters: 128 64 32 8) takes: 55 seconds PyTorch2.7+ROCm6.3 Time taken: 387 seconds 15.66s/it**（11.21% slower）** The VAE Decode Tiled node (parameters: 128 64 32 8) takes:...
   - Issue: https://github.com/pytorch/pytorch/issues/148883
   - Fix PR #150249 — [ROCm] change preferred blas lib defaults
   - PR: https://github.com/pytorch/pytorch/pull/150249
   - Code excerpts:     - aten/src/ATen/BlasBackend.h: +enum class BlasBackend : int8_t { Default, Cublas, Cublaslt, Ck }; +    case BlasBackend::Default: +      return "at::BlasBackend::Default";



20. Issue #150480 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Observing following failure: https://github.com/pytorch/pytorch/actions/runs/14203257536/job/39804771702 Error: Filename longer than 260 characters: ``` 2025-04-01T21:28:58.8631176Z ninja: error: Stat(C:/Users/runneruser/AppData/Local/Temp/tmpzgzp7pwt/triton/python/build/cmake.win-amd64-cpython-3.10/_deps/spirv-llvm-translator-subbuild/spirv-llvm-translator-populate-prefix/src/spirv-llvm-translator-populate-stamp/spirv-llvm-translator-populate-patch-info.txt): Filename...
   - Issue: https://github.com/pytorch/pytorch/issues/150480
   - Fix PR #150547 — [BE] Fix triton windows build
   - PR: https://github.com/pytorch/pytorch/pull/150547
   - Code excerpts:     - .github/scripts/windows/build_triton.bat: +:: Fix cmake version for issue https://github.com/pytorch/pytorch/issues/150480 +call conda run -n %PYTHON_PREFIX% pip install wheel pybind11 certifi cython cmake==3.31.6 setuptools==72.1.0 ninja



21. Issue #152385 —  (closed )
   - Issue detail: ### 🐛 Describe the bug In Windows 10, Python 3.12.9, Pytorch 2.7.0+cu118, CUDA 12.2, the following code produces an "illegal instruction" causing an immediate crash: ```python import torch src = torch.rand((1, 1, 128, 64), dtype=torch.float64) grid = torch.rand((1, 256, 256, 2), dtype=torch.float64) dst = nn.functional.grid_sample( input=src.contiguous(), grid=grid, mode="bilinear", padding_mode="border", align_corners=False ) ``` This is specific to float64 tensors, float32 tensor format for...
   - Issue: https://github.com/pytorch/pytorch/issues/152385
   - Fix PR #153390 — Revert "Cleanup VS 2019 refs in pytorch (#145863)" (#152613)
   - PR: https://github.com/pytorch/pytorch/pull/153390
   - Code excerpts:     - .ci/pytorch/windows/internal/smoke_test.bat: +if "%VC_YEAR%" == "2019" powershell internal\vs2019_install.ps1 +IF "%VC_YEAR%" == "2019" ( +    set VC_VERSION_LOWER=16 +    set VC_VERSION_UPPER=17 +)



22. Issue #149813 —  (closed )
   - Issue detail: ### 🐛 Describe the bug ```python # bug (Pdb) torch.tril(torch.full((3, 3), float("inf"), device="mps"), diagonal=-1) tensor([[nan, nan, nan], [inf, nan, nan], [inf, inf, nan]], device='mps:0') # working examples # works with non-infs (Pdb) torch.tril(torch.full((3, 3), 1.0, device="mps"), diagonal=-1) tensor([[0., 0., 0.], [1., 0., 0.], [1., 1., 0.]], device='mps:0') # works on the cpu (Pdb) torch.tril(torch.full((3, 3), float("inf"), device="cpu"), diagonal=-1) tensor([[0., 0., 0.], [inf,...
   - Issue: https://github.com/pytorch/pytorch/issues/149813
   - Fix PR #150479 — [MPS] tril op not handling infs correctly
   - PR: https://github.com/pytorch/pytorch/pull/150479
   - Code excerpts:     - aten/src/ATen/native/mps/operations/TriangularOps.mm: +        MPSGraphTensor* zeroTensor = [mpsGraph constantWithScalar:0.0 dataType:getMPSDataType(self)]; +        MPSGraphTensor* mask = [mpsGraph equalWithPrimaryTensor:complementTensor secondaryTensor



23. Issue #149889 —  (closed )
   - Issue detail: ### 🐛 Describe the bug @xuhancn @shunting314 this is a follow up bug to https://github.com/pytorch/pytorch/issues/149310#issuecomment-2745707169 I just came to test the change in https://github.com/pytorch/pytorch/commit/bc1b8730a45e659dca83ec83995c17d4eec9c869 as torch was built on nightly yesterday but torchaudio got built a day later: the bug is solved but a new (similar) one came up. The fix in https://github.com/pytorch/pytorch/commit/bc1b8730a45e659dca83ec83995c17d4eec9c869 does fix the...
   - Issue: https://github.com/pytorch/pytorch/issues/149889
   - Fix PR #150447 — [inductor] Fix inductor windows linker error
   - PR: https://github.com/pytorch/pytorch/pull/150447
   - Code excerpts:     - torch/_inductor/cpp_builder.py: +        python_lib_path = [ +            str( +                ( +                    Path(sysconfig.get_path("include", scheme="nt")).parent / "libs" +                ).absolute() +            ) +  



24. Issue #149806 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Hi, I'm facing an issue when loading torch with CUDA from a PEX file. The function [_preload_cuda_deps](https://github.com/pytorch/pytorch/blob/2b848ab192e51498fb626355aedfd210df7da27e/torch/__init__.py#L282) seems to have a bug that prevents it from locating CUDA dependencies when they are placed in `path/lib_folder` rather than in the usual `path/nvidia/lib_folder`. The problem appears to be in this code snippet: ```python nvidia_path = os.path.join(path, "nvidia") if...
   - Issue: https://github.com/pytorch/pytorch/issues/149806
   - Fix PR #150068 — Fix #149806 : Fix path lookup in _preload_cuda_deps
   - PR: https://github.com/pytorch/pytorch/pull/150068
   - Code excerpts:     - torch/__init__.py: +def _get_cuda_dep_paths(path: str, lib_folder: str, lib_name: str) -> list[str]: +    # Libraries can either be in path/nvidia/lib_folder/lib or path/lib_folder/lib +    nvidia_lib_paths = glob.glob(



25. Issue #149132 —  (closed )
   - Issue detail: ### 🐛 Describe the bug This following python code fails and ends the process on macos 15.3.1 (M1 Pro). ```python import torch import torch.nn.functional as F print(torch.__version__) device = torch.device('mps') B=2 T=3 n_kv_head = 2 n_q_head = 4 dim = 8 attn_mask = torch.ones((T, T)).to(device) q = torch.rand(B, n_q_head, T, dim).to(device) k = torch.rand(B, n_kv_head, T, dim).to(device) v = torch.rand(B, n_kv_head, T, dim).to(device) F.scaled_dot_product_attention(q, k, v,...
   - Issue: https://github.com/pytorch/pytorch/issues/149132
   - Fix PR #150067 — [MPS] fix attention enable_gqa crash on mps
   - PR: https://github.com/pytorch/pytorch/pull/150067
   - Code excerpts:     - aten/src/ATen/native/mps/operations/Attention.mm: +  TORCH_CHECK(query.size(-3) == key.size(-3) && key.size(-3) == value.size(-3), +              "number of heads in query/key/value should match"); +



26. Issue #149550 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Please see: https://github.com/pytorch/pytorch/issues/123649 and https://dev-discuss.pytorch.org/t/pytorch-linux-wheels-switching-to-new-wheel-build-platform-manylinux-2-28-on-november-12-2024/2581/2 Pytorch is using D_GLIBCXX_USE_CXX11_ABI=1 and Manylinux 2.28 Hence we should remove the usage of PRE_CXX11_ABI from the documents Example: https://pytorch.org/cppdocs/installing.html#system-requirements ### Versions 2.7.0 cc @svekars @sekyondaMeta @AlannaBurke
   - Issue: https://github.com/pytorch/pytorch/issues/149550
   - Fix PR #149952 — Removing doc references to PRE_CXX11_ABI.
   - PR: https://github.com/pytorch/pytorch/pull/149952
   - Code excerpts:     - docs/cpp/source/installing.rst: +  - GCC 9 or newer for cxx11



27. Issue #148661 —  (closed )
   - Issue detail: ### 🐛 Describe the bug This commit does not contain the complete availabilities for HPU devices (https://github.com/pytorch/pytorch/pull/148182). We need to add the complete availabilities for HPU devices. ### Versions Collecting environment information... PyTorch version: 2.6.0+hpu.git99dbd97 Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 22.04 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: 14.0.5 CMake...
   - Issue: https://github.com/pytorch/pytorch/issues/148661
   - Fix PR #149115 — [Profiler][HPU] Fix incorrect availabilities for HPU
   - PR: https://github.com/pytorch/pytorch/pull/149115
   - Code excerpts:     - torch/csrc/autograd/init.cpp: +    if (at::hasHPU()) { +      activities.insert(torch::profiler::impl::ActivityType::HPU); +    }



28. Issue #149032 —  (closed )
   - Issue detail: ### 🐛 Describe the bug When a **pin_memory()** is called on a tensor, before the device is initialized, then the **is_pinned()** always return false. I believe this was broken by a #145752 PR and to be more precise by not calling lazyInitDevice in **_pin_memory** function. Reproduction: ``` import torch ifm = torch.tensor([2]) ifm = ifm.pin_memory() print(ifm.is_pinned()) ```` Output: false Expected: True Below code works, as pining memory with a pin_memory param works fine and it initializes...
   - Issue: https://github.com/pytorch/pytorch/issues/149032
   - Fix PR #149183 — [regression] Fix pin_memory() when it is called before device lazy initialization.
   - PR: https://github.com/pytorch/pytorch/pull/149183
   - Code excerpts:     - aten/src/ATen/Context.h: +    auto opt_device_type = +        device_type.has_value() ? device_type : at::getAccelerator(); +    if (opt_device_type) { +      lazyInitDevice(opt_device_type.value()); +    }



29. Issue #148938 —  (closed )
   - Issue detail: ### 🐛 Describe the bug 1. Update triton to `release/3.3.x` https://github.com/triton-lang/triton/tree/release/3.3.x 2. run `python test/inductor/test_aot_inductor.py -vvv -k test_triton_kernel_tma_descriptor_1d_dynamic_False_cuda` Possibly an easier repro is ``` TORCHINDUCTOR_CPP_WRAPPER=1 python test/inductor/test_triton_kernels.py -k test_tma_descriptor_1d_dynamic_False_backend_inductor ``` errors: <details> ``` /home/dberard/local/triton-env2/pytorch/torch/backends/cudnn/__init__.py:108:...
   - Issue: https://github.com/pytorch/pytorch/issues/148938
   - Fix PR #149993 — [inductor][triton 3.3] Fix cpp_wrapper w/ TMA in triton 3.3
   - PR: https://github.com/pytorch/pytorch/pull/149993
   - Code excerpts:     - torch/_inductor/codegen/cpp_wrapper_gpu.py: +            # these args are passed to initNDTMADescriptor, which is NOT a triton kernel +            is_triton_kernel=False, +        self, +        code: Union[IndentedBuffer, Self], +        call_



30. Issue #149310 —  (closed )
   - Issue detail: ### 🐛 Describe the bug i am using the torch library (using not compiling) with torch compile enabled though another library (Zonos). at runtime the code tried to compile some code so i run it though the Visual Studio developer command line. it crashes wiht this error: ``` File "c:\code\.env\lib\site-packages\torch\_inductor\cpp_builder.py", line 349, in run_compile_cmd return _run_compile_cmd(cmd_line, cwd) File "c:\code\.env\lib\site-packages\torch\_inductor\cpp_builder.py", line 343, in...
   - Issue: https://github.com/pytorch/pytorch/issues/149310
   - Fix PR #150448 — [Windows][inductor] fix blank space break windows file path
   - PR: https://github.com/pytorch/pytorch/pull/150448
   - Code excerpts:     - torch/_inductor/cpp_builder.py: +                self._include_dirs_args += f'/I "{inc_dir}" '



31. Issue #146792 —  (closed )
   - Issue detail: ### 🐛 Describe the bug #### **Description** On Raspberry Pi 4, `torch.onnx.export` fails with `Illegal instruction (core dumped)` in `torch 2.6.0`. The same code works fine on `torch 2.5.1`. The issue occurs when using `x.expand(x.shape[0], -1, -1)` inside a `torch.nn.Module`. The crash happens **only during ONNX export**, not during regular inference. #### **Code to Reproduce** ```python import torch class Module(torch.nn.Module): def forward(self, x): return x.expand(x.shape[0], -1, -1) #...
   - Issue: https://github.com/pytorch/pytorch/issues/146792
   - Fix PR #149878 — Fix atomic operation compatibility for ARMv8-A (Raspberry Pi 4) by adjusting compilation flags
   - PR: https://github.com/pytorch/pytorch/pull/149878
   - Code excerpts:     - cmake/Codegen.cmake: +        list(APPEND CPU_CAPABILITY_FLAGS "${OPT_FLAG} -O2 -march=armv8-a+sve -DCPU_CAPABILITY_SVE -msve-vector-bits=256") +        list(APPEND CPU_CAPABILITY_FLAGS "${OPT_FLAG} -march=armv8-a+sve -DC



32. Issue #140318 —  (closed )
   - Issue detail: ### 🐛 Describe the bug When running distributed (or multi-process) jobs on AMD GPU systems with GPU isolation (i.e., the `*_VISIBLE_DEVICES` environment variable), PyTorch still tries to set the seed of all the devices it finds. This causes the following exception to be raised: ``` File "/path/to/torch/random.py", line 46, in manual_seed torch.cuda.manual_seed_all(seed) File "/path/to/torch/cuda/random.py", line 131, in manual_seed_all _lazy_call(cb, seed_all=True) File...
   - Issue: https://github.com/pytorch/pytorch/issues/140318
   - Fix PR #144026 — Respect ROCR_VISIBLE_DEVICES on AMD GPU device discovery
   - PR: https://github.com/pytorch/pytorch/pull/144026
   - Code excerpts:     - test/test_cuda.py: +            {"ROCR_VISIBLE_DEVICES": "1,2,3", "HIP_VISIBLE_DEVICES": "0"}, +            {"ROCR_VISIBLE_DEVICES": "0", "HIP_VISIBLE_DEVICES": None},



33. Issue #143788 —  (closed )
   - Issue detail: The following code is from `_nested_mod_func_adapter` which is a helper function used by `create_nested_block_mask`. Conceptually, it wraps a mod function that operates on individual batch items of a nested tensor and transforms the inputs so it works on a single packed item. However, the below code doesn't appear to update the batch argument (`b`) before calling the original mod function....
   - Issue: https://github.com/pytorch/pytorch/issues/143788
   - Fix PR #144330 — Fix batch-specific attention mod for NJT + Flex
   - PR: https://github.com/pytorch/pytorch/pull/144330
   - Code excerpts:     - test/test_nestedtensor.py: +        # Test with batch-specific score_mod +        batch_size = query.size(0) +        batch_table = torch.randn(batch_size, device=device, dtype=dtype) +        # Keep score the same for batch in



34. Issue #141909 —  (closed )
   - Issue detail: ### 🚀 The feature, motivation and pitch Output size of the matrix multiplication is larger than currently supported by the MPS backend: 72250,72250, needs to be less than 2**32 elements ### Alternatives _No response_ ### Additional context Reported as suggested by the error message. I'm on a Apple M2 Max MacBook Pro with 96GB Ram. cc @ezyang @gchanan @zou3519 @kadeng @msaroufim @kulinseth @albanD @malfet @DenisVieriu97 @jhavukainen
   - Issue: https://github.com/pytorch/pytorch/issues/141909
   - Fix PR #144558 — Extend bmm tiling to work up to 2^32 elem in any single output dim
   - PR: https://github.com/pytorch/pytorch/pull/144558
   - Code excerpts:     - aten/src/ATen/native/mps/operations/LinearAlgebra.mm: +        // if largest supported batch size is zero, we need to split up the computation more +        bool tileEachMatmul = largestSupportedBatchSize == 0; +        uint64_t batchSize = largestSuppor



35. Issue #141770 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Runs in the stable version, does not run in the nightly version: ```python import torch class Model(torch.nn.Module): def __init__(self): super().__init__() def forward(self, x,y): out = torch.meshgrid(x, y, indexing="xy") return out onnx_program = torch.onnx.export(Model(), (torch.tensor(20),torch.tensor(20)), dynamo=True) ``` ~~Without the `indexing="xy"` it gives error:~~ > ~~<class 'TypeError'>: meshgrid() missing 1 required keyword-only argument: 'indexing'~~ I...
   - Issue: https://github.com/pytorch/pytorch/issues/141770
   - Fix PR #144418 — [ONNX] Avoid overwriting overlapped decomposed functions
   - PR: https://github.com/pytorch/pytorch/pull/144418
   - Code excerpts:     - torch/onnx/_internal/exporter/_decomp.py: +        # NOTE: torch._decomp.decomposition_table covers more ops +        # than torch.export.default_decompositions, but the latter is +        # more critical to torch.onnx.export. +        if op_



36. Issue #143838 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Currently, the xpu CD linux wheels have multiple triton pypi packages dependencies, which depends on `triton` and `pytorch-triton-xpu`, refer ``` $ pip install torch==2.6 --index-url https://download.pytorch.org/whl/test/xpu Looking in indexes: https://download.pytorch.org/whl/test/xpu Collecting torch==2.6 Using cached https://download.pytorch.org/whl/test/xpu/torch-2.6.0%2Bxpu-cp310-cp310-linux_x86_64.whl (1027.1 MB) Collecting filelock (from torch==2.6) Using cached...
   - Issue: https://github.com/pytorch/pytorch/issues/143838
   - Fix PR #143983 — [CD] Remove redundant triton dependency for xpu wheels
   - PR: https://github.com/pytorch/pytorch/pull/143983
   - Code excerpts:     - .circleci/scripts/binary_populate_env.sh: +if [[ "$PACKAGE_TYPE" =~ .*wheel.* &&  -n "${PYTORCH_EXTRA_INSTALL_REQUIREMENTS:-}" && ! "$PYTORCH_BUILD_VERSION" =~ .*xpu.* ]]; then



37. Issue #143102 —  (closed )
   - Issue detail: ### 🐛 Describe the bug <p>fp32 inductor_max_autotune dynamic shape multiple thread failures</p><table border="1" class="dataframe table"> <thead> <tr style="text-align: right;"> <th>suite</th> <th>name</th> <th>thread</th> <th>accuracy</th> <th>perf</th> <th>reason(reference only)</th> </tr> </thead> <tbody> <tr> <td>huggingface</td> <td>AllenaiLongformerBase</td> <td>multiple</td> <td>√</td> <td>X</td> <td>AllenaiLongformerBase, LoweringException: TypeError: as_strided(): argument 'size'...
   - Issue: https://github.com/pytorch/pytorch/issues/143102
   - Fix PR #144248 — [inductor][cpu] Fix bmm b_index for dynamic expressions in inductor autotuner
   - PR: https://github.com/pytorch/pytorch/pull/144248
   - Code excerpts:     - test/inductor/test_cpu_select_algorithm.py: +    @patches +    @torch.no_grad +    @unittest.skipIf(not TEST_MKL, "Test requires MKL") +    @parametrize("bs", (5,)) +    @parametrize("Mdim", (384,)) +    @parametrize("Kdim", (96,)) +    @parame



38. Issue #133415 —  (closed )
   - Issue detail: ### 🐛 Describe the bug The new API for checkpointing, e.g. `set_optimizer_state_dict`, calls `_init_optim_state`. https://github.com/pytorch/pytorch/blob/2a4304329be0ee592af0f1d8d0dd9428ed82a0c6/torch/distributed/checkpoint/state_dict.py#L585-L605 This function will initialize optimizer states if they are not already initialized by doing a step with grads as zero. However, this causes problems for stateless optimizers, e.g. SGD. For example, if I have a simple code snippet where I train a...
   - Issue: https://github.com/pytorch/pytorch/issues/133415
   - Fix PR #136000 — [DCP] Fixes the stateless optimizer issue of distributed state_dict (…
   - PR: https://github.com/pytorch/pytorch/pull/136000
   - Code excerpts:     - test/distributed/checkpoint/test_state_dict.py: +        _dist_optim = [dist_optim] if not isinstance(dist_optim, list) else dist_optim +            optim.zero_grad() +            for d_optim in _dist_optim: +                d_optim.zero_grad() + +



39. Issue #133540 —  (closed )
   - Issue detail: Platforms: rocm This test was disabled because it is failing on main branch ([recent examples](https://torch-ci.com/failure?failureCaptures=%5B%22export%2Ftest_export.py%3A%3ATestOneOffModelExportResult%3A%3Atest_scaled_dot_product_attention_cuda%22%5D)). cc @ezyang @gchanan @zou3519 @kadeng @msaroufim @jeffdaily @sunway513 @jithunnair-amd @ROCmSupport @dllehr-amd @jataylo @hongxiayang @avikchaudhuri @gmagogsfm @zhxchen17 @tugsbayasgalan @angelayi @suo @ydwu4 @penguinwu
   - Issue: https://github.com/pytorch/pytorch/issues/133540
   - Fix PR #135869 — [ROCm] Update to AOTriton 0.7b (Cherry-picked)
   - PR: https://github.com/pytorch/pytorch/pull/135869
   - Code excerpts:     - .ci/docker/aotriton_version.txt: +0.7b +9be04068c3c0857a4cfd17d7e39e71d0423ebac2 +3e9e1959d23b93d78a08fcc5f868125dc3854dece32fd9458be9ef4467982291



40. Issue #135223 —  (closed )
   - Issue detail: ### 🐛 Describe the bug When generating a frequency axis using `torch.fft.fftfreq(N)` on the MPS backend, the generated output is different from what the CPU produces. The result should be a tensor of length N, which starts at 0.0 and linearly increases to 0.5 at index N/2, then jumps to -0.5 and increases linearly again until -0.0001. The below example demonstrates the different outputs when being run on CPU vs MPS. ``` import torch device = torch.device('cpu') freq_cpu =...
   - Issue: https://github.com/pytorch/pytorch/issues/135223
   - Fix PR #137215 — [MPS] Add regression test for `fft.fftfreq`
   - PR: https://github.com/pytorch/pytorch/pull/137215
   - Code excerpts:     - test/test_mps.py: +    # Regression test for https://github.com/pytorch/pytorch/issues/135223 +    def test_fftfreq(self): +        freq_cpu = torch.fft.fftfreq(10**4, device='cpu') +        freq_mps = torch.fft.fftfre



41. Issue #135419 —  (closed )
   - Issue detail: `aten._assert_scalar`
   - Issue: https://github.com/pytorch/pytorch/issues/135419
   - Fix PR #137214 — [ONNX] Add assertion nodes to ignoring list
   - PR: https://github.com/pytorch/pytorch/pull/137214
   - Code excerpts:     - test/onnx/exporter/test_api.py: +    def test_zero_output_aten_node(self): +        class Model(torch.nn.Module): +            def forward(self, x): +                torch.ops.aten._assert_async.msg(torch.tensor(True), "assertion fa



42. Issue #127402 —  (closed )
   - Issue detail: ### 🐛 Describe the bug abnormal performance improvement and accuracy drop for huggingface suit static/dynamic quantization in 2024-05-26 nightly release accuracy drop: </head> <body link=blue vlink=purple> model_name | static_quant_new | dynamic_quant_new | static_quant_old | dynamic_quant_old | static_quant(new/old) | dynamic_quant(new/old) -- | -- | -- | -- | -- | -- | -- text-classification+albert-base-v1 | 0.3162 | 0.3162 | 0.5613 | 0.576 | 0.56 | 0.55 text-classification+bert-base-...
   - Issue: https://github.com/pytorch/pytorch/issues/127402
   - Fix PR #128591 — [Port][Quant][Inductor] Bug fix: mutation nodes not handled correctly for QLinearPointwiseBinaryPT2E
   - PR: https://github.com/pytorch/pytorch/pull/128591
   - Code excerpts:     - test/inductor/test_flex_attention.py: +        # TODO: Get rid of this fudge factor +        # We need this fudge factor for now, since +        # 1. For some reason we materialize the output of the attention unnecessarily (it's related t



43. Issue #97409 —  (closed )
   - Issue detail: ### 🐛 Describe the bug **TLDR:** When `nn.MultiheadAttention` is used with a batched `attn_mask` which [should be](https://pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html) shape (N*H, L, S) (where S=L for self-attn) **_and_** fast path is enabled it crashes. _It works as expected when fast path is **not** enabled_ ### Minimal example to reproduce: ```python import torch import torch.nn as nn with torch.no_grad(): B = 8 L = 100 D = 512 H = 8 mha = nn.MultiheadAttention(D, H,...
   - Issue: https://github.com/pytorch/pytorch/issues/97409
   - Fix PR #99092 — Adds 3D attn_mask support to merge_masks() for Multihead Attention fa…
   - PR: https://github.com/pytorch/pytorch/pull/99092
   - Code excerpts:     - test/test_transformers.py: +    @parametrize("device", device_list) +    @parametrize("attn_mask_dim", [2, 3, None]) +    @parametrize("key_padding_mask_dim", [2, None]) +    def test_multiheadattention_fastpath_attn_mask(self,



44. Issue #131701 —  (closed )
   - Issue detail: ### 🐛 Describe the bug `/opt/rocm` is hardcoded in `Caffe2Targets.cmake` in ROCm wheels: ```sh wget https://download.pytorch.org/whl/rocm6.1/torch-2.4.0%2Brocm6.1-cp312-cp312-linux_x86_64.whl unzip torch-2.4.0+rocm6.1-cp312-cp312-linux_x86_64.whl cd torch/share/cmake/Caffe2 ``` You can find below in `Caffe2Targets.cmake`: ```cmake set_target_properties(c10_hip PROPERTIES INTERFACE_INCLUDE_DIRECTORIES "${_IMPORT_PREFIX}/include" INTERFACE_LINK_LIBRARIES "c10;/opt/rocm/lib/libamdhip64.so" ) ```...
   - Issue: https://github.com/pytorch/pytorch/issues/131701
   - Fix PR #136700 — Fix hardcoded ROCm paths in `Caffe2Targets.cmake`
   - PR: https://github.com/pytorch/pytorch/pull/136700
   - Code excerpts:     - c10/hip/CMakeLists.txt: +  target_link_libraries(c10_hip PUBLIC ${C10_LIB} hip::amdhip64)



45. Issue #128130 —  (closed )
   - Issue detail: ### 🐛 Describe the bug I am getting an error while building pytorch for ppc64le The error is : /home/manjulmohan/pytorch_may17/pytorch-3/aten/src/ATen/native/cpu/FlashAttentionKernel.cpp:735:3: required from here /home/manjulmohan/pytorch_may17/pytorch-3/aten/src/ATen/cpu/vec/vec_base.h:632:6: error: use of deleted function ‘double& at::vec::DEFAULT::Vectorized<double>::operator[](int)’ 632 | c[i] = a[i] * b[i]; The error is caused by the commit id: 457b9f7397c83953e7f3124f02738427aaff61cd...
   - Issue: https://github.com/pytorch/pytorch/issues/128130
   - Fix PR #133416 — Fix recent build error on ppc64le 
   - PR: https://github.com/pytorch/pytorch/pull/133416
   - Code excerpts:     - aten/src/ATen/cpu/vec/vec256/vsx/vec256_complex_double_vsx.h: +template <> +Vectorized<ComplexDbl> C10_ALWAYS_INLINE operator+(const Vectorized<ComplexDbl>& a, const Vectorized<ComplexDbl>& b) { +  return Vectorized<ComplexDbl>{vec_add(a.vec0(), b.vec0()), vec_a



46. Issue #130658 —  (closed )
   - Issue detail: ### 🐛 Describe the bug The PyTorch code base contains several uses of `torch.load` internally, but not all of them set `weights_only`, which in PyTorch 2.4 raises a FutureWarning. Since these are internal, the user would see the warning but have no way of acting on it. PyTorch should set `weights_only` in all of its internal uses. Some examples (but there are more if you search the code base):...
   - Issue: https://github.com/pytorch/pytorch/issues/130658
   - Fix PR #133594 — Pass `torch.load(weights_only=)` internally to avoid FutureWarning
   - PR: https://github.com/pytorch/pytorch/pull/133594
   - Code excerpts:     - torch/distributed/checkpoint/default_planner.py: +                torch.load(value, weights_only=False), +            self.state_dict[read_item.dest_index.fqn] = torch.load( +                value, weights_only=False +            )



47. Issue #127055 —  (closed )
   - Issue detail: ### 🐛 Describe the bug It works as expected for shorter sequences and when all past tokens are allowed. ```py import torch model = torch.nn.MultiheadAttention(embed_dim=2, num_heads=1) n = 600 sequence = torch.ones(n, 2) # do not attend to the future and very old tokens full = torch.full((n, n), float("-inf")) mask = torch.triu(full, diagonal=1) + torch.tril(full, diagonal=-10) print(model(sequence, sequence, sequence, attn_mask=mask, need_weights=False)[0]) #tensor([[0.0519, 0.1435], #...
   - Issue: https://github.com/pytorch/pytorch/issues/127055
   - Fix PR #133598 — [cpu][flash attention] fix nan issue
   - PR: https://github.com/pytorch/pytorch/pull/133598
   - Code excerpts:     - aten/src/ATen/native/cpu/FlashAttentionKernel.cpp: +          if (tmp_max == -std::numeric_limits<accum_t>::infinity()) { +            // to avoid `nan = exp2f(-inf - (-inf))` +            fill_stub(conditional_data_ptr(qk_data, qk_reduced_data) + row



48. Issue #130659 —  (closed )
   - Issue detail: ### 🐛 Describe the bug PyTorch 2.4 deprecated the use of `torch.cuda.amp.autocast` in favor of `torch.amp.autocast("cuda", ...)`, but this change has missed updating internal uses in PyTorch. For example in DP here: https://github.com/pytorch/pytorch/blob/3710a7962261f26bf9ad8b768229582bf9f00c94/torch/nn/parallel/parallel_apply.py#L92-L93 ```py import torch model = torch.nn.Linear(10, 10).cuda() model = torch.nn.DataParallel(model, device_ids=[0, 1]) output = model(torch.randn(20, 10).cuda())...
   - Issue: https://github.com/pytorch/pytorch/issues/130659
   - Fix PR #134057 — Avoid autocast deprecation warning in DataParallel (#130660)
   - PR: https://github.com/pytorch/pytorch/pull/134057
   - Code excerpts:     - torch/nn/parallel/parallel_apply.py: +            with torch.cuda.device(device), torch.cuda.stream( +                stream +            ), torch.amp.autocast("cuda", enabled=autocast_enabled):



49. Issue #128756 —  (closed )
   - Issue detail: ### 🐛 Describe the bug NCCL introduced a new ncclResult code (ncclRemoteError). see [here](https://docs.nvidia.com/deeplearning/nccl/archives/nccl_2143/user-guide/docs/api/types.html#ncclresult-t) and [here](https://github.com/NVIDIA/nccl/blob/master/src/nccl.h.in#L37-L45). This new code is not included in the https://github.com/pytorch/pytorch/blob/main/torch/csrc/cuda/nccl.h#L40-L49. This throws a runtime error std::runtime_error("Unconvertible NCCL type") from...
   - Issue: https://github.com/pytorch/pytorch/issues/128756
   - Fix PR #129704 — [distributed] NCCL result code update
   - PR: https://github.com/pytorch/pytorch/pull/129704
   - Code excerpts:     - torch/csrc/cuda/nccl.cpp: +    case torch::cuda::nccl::ncclResult::RemoteError: +      return ncclResult_t::ncclRemoteError; +    case torch::cuda::nccl::ncclResult::NumResults: +      return ncclResult_t::ncclNumResults; +   



50. Issue #129079 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Hey PyTorch team! Thanks for your hard work on the distributed checkpointing, big fan of the work! There seems to have been a regression between `2.2.2` and `2.3.0` that resulted in the optimizer learning rate being loaded incorrectly. It seems like the `lr` key in params group is not loaded from the checkpoint, resulting in the first step having the initialisation learning rate instead of the checkpointed one. This was not the case in `2.2.2` and only occurs after...
   - Issue: https://github.com/pytorch/pytorch/issues/129079
   - Fix PR #129683 — [CherryPick][DCP] Fix Optimizer Learning Rate not being loaded correctly (#129398)
   - PR: https://github.com/pytorch/pytorch/pull/129683
   - Code excerpts:     - test/distributed/checkpoint/e2e/test_e2e_save_and_load.py: +    get_optimizer_state_dict, +    set_state_dict, +class TestInitStateDict(DTensorTestBase): +    @with_temp_dir +    def test_init_state_dict(self): +        temp_dir = self.temp_dir +        model



51. Issue #128444 —  (closed )
   - Issue detail: ### 🐛 Describe the bug PyTorch 2.3.1 (and nightly) ### Versions TLDR: HSDP + DCP monolith checkpointing break. When using DCP + `set_optimizer_state_dict`, the code eventually goes to `_optim_state_dict_to_load_impl` [here](https://github.com/pytorch/pytorch/blob/adb699189b9d2de7cfbd71e59c70d916483b23dd/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1298), which calls `_flatten_optim_state_dict` and in turn `_broadcast_processed_state` defined...
   - Issue: https://github.com/pytorch/pytorch/issues/128444
   - Fix PR #129254 — Support HSDP + Monolith Checkpointing (#128446)
   - PR: https://github.com/pytorch/pytorch/pull/129254
   - Code excerpts:     - torch/distributed/fsdp/_optim_utils.py: +    if dist.get_rank(group) == 0: +    if dist.get_rank(group) == 0: +    if dist.get_rank(group) == 0:



52. Issue #130806 —  (closed )
   - Issue detail: ### 🐛 Describe the bug F.embedding will crash with relatively large tensor input on the AMD GPU: ``` input = torch.randint(low=0, high=16032, size=[131072], device="cuda") w = torch.randn([16032, 16384], device="cuda") torch.nn.functional.embedding(input, w) RuntimeError: HIP error: invalid configuration argument ``` ### Versions top of tree cc @jeffdaily @sunway513 @jithunnair-amd @pruthvistony @ROCmSupport @dllehr-amd @jataylo @hongxiayang
   - Issue: https://github.com/pytorch/pytorch/issues/130806
   - Fix PR #133346 — fix for launching kernel invalid config error when calling embedding …
   - PR: https://github.com/pytorch/pytorch/pull/133346
   - Code excerpts:     - aten/src/ATen/native/cuda/Indexing.cu: +static size_t getSliceSize(const Tensor & dst, +  size_t dstSliceSize = 1; +  size_t srcSliceSize = 1; +  const uint64_t sliceSize = getSliceSize(self_, dim, index, source_); +  const uint64_t source



53. Issue #133520 —  (closed )
   - Issue detail: ### 🐛 Describe the bug In https://github.com/huggingface/diffusers/pull/9133 some inconsistencies was discovered in output from [FLUX](https://huggingface.co/black-forest-labs/FLUX.1-schnell). I was not able to reproduce, but @bghira saw this issue consistently. We chatted offline and discovered we had different versions of PyTorch. @bghira had latest nightly, I had v2.3.1. I updated to the nightly and could also reproduce the issue consistently. Bisect replay log: ```bash git bisect start #...
   - Issue: https://github.com/pytorch/pytorch/issues/133520
   - Fix PR #134121 — [MPS] Gather sliced inputs to batch norm
   - PR: https://github.com/pytorch/pytorch/pull/134121
   - Code excerpts:     - aten/src/ATen/native/mps/operations/Normalization.mm: +    auto inputPlaceholder = Placeholder(cachedGraph->inputTensor_, self, input_shape);



54. Issue #100152 —  (closed )
   - Issue detail: Platforms: asan, linux, win, windows, dynamo, mac, macos This test was disabled because it is failing in CI. See [recent examples](https://hud.pytorch.org/flakytest?name=test_open_device_registration&suite=TestCppExtensionOpenRgistration) and the most recent trunk [workflow logs](https://github.com/pytorch/pytorch/runs/undefined). Over the past 3 hours, it has been determined flaky in 22 workflow(s) with 44 failures and 22 successes. **Debugging instructions (after clicking on the recent...
   - Issue: https://github.com/pytorch/pytorch/issues/100152
   - Fix PR #124712 — Fix & optimize open device registration test
   - PR: https://github.com/pytorch/pytorch/pull/124712
   - Code excerpts:     - test/test_cpp_extensions_open_device_registration.py: +import types +from torch.testing._internal.common_utils import IS_ARM64, skipIfTorchDynamo, TEST_CUDA +def generate_faked_module(): +    # create a new module to fake torch.foo dynamicaly +    foo = 



55. Issue #122792 —  (closed )
   - Issue detail: ``` """ torchrun --standalone --nproc_per_node=2 repro_dcp_compile.py """ import os import torch import torch.nn as nn import torch.distributed as dist from torch.distributed.checkpoint.state_dict import get_model_state_dict, set_model_state_dict class Model(nn.Module): def __init__(self): super().__init__() self.lin1 = nn.Linear(4, 4) self.lin2 = nn.Linear(4, 4) self.register_buffer("buf", torch.randn((4,)), persistent=False) self.weight = nn.Parameter(torch.randn((4, 4))) if __name__ ==...
   - Issue: https://github.com/pytorch/pytorch/issues/122792
   - Fix PR #127219 — [DSD] Fix to remove non_persistent buffer in distributed state dict (#125337)
   - PR: https://github.com/pytorch/pytorch/pull/127219
   - Code excerpts:     - test/distributed/checkpoint/test_state_dict.py: +    @with_comms +    @skip_if_lt_x_gpu(1) +    def test_non_persistent_buffers(self) -> None: +        model = CompositeParamModel(device=torch.device("cuda")) +        model.register_buffer( +      



56. Issue #124546 —  (closed )
   - Issue detail: ### 🐛 Describe the bug With distributed checkpointing + FSDP, and with `use_orig_params = False` and activation checkpointing, when loading the optimizer state through the `torch.distributed.checkpoint.load()` function, resuming from checkpoint throws the following error: ``` │ /usr/lib/python3/dist-packages/torch/distributed/checkpoint/state_dict.py:83 │ │ 4 in set_optimizer_state_dict │ │ │ │ 831 │ │ info = _verify_options(model, optimizers, optim_only=True, op │ │ 832 │ │ │ │ 833 │ │...
   - Issue: https://github.com/pytorch/pytorch/issues/124546
   - Fix PR #126559 — Remove activation checkpointing tag to get correct FQNs (#124698)
   - PR: https://github.com/pytorch/pytorch/pull/126559
   - Code excerpts:     - torch/distributed/checkpoint/state_dict.py: + +    # Remove the checkpoint prefix, if it exists. +    name = name.replace(_CHECKPOINT_PREFIX, "") +        return {name}



57. Issue #121258 —  (closed )
   - Issue detail: ### 🚀 The feature, motivation and pitch We are releasing ONNX 1.16.0. A release branch is created (https://github.com/onnx/onnx/tree/rel-1.16.0). The planned release date is March 25, 2024. Release candidates are also available from TestPyPI: `pip install -i https://test.pypi.org/simple/ --pre onnx` It is important to integrate ONNX release branch ASAP so that any issues and incompatibilities can be detected and resolved before the ONNX release. Key updates: * ai.onnx Opset 21 * Update to...
   - Issue: https://github.com/pytorch/pytorch/issues/121258
   - Fix PR #123387 — update submodule onnx==1.16.0
   - PR: https://github.com/pytorch/pytorch/pull/123387
   - Code excerpts:     - third_party/onnx: +Subproject commit 990217f043af7222348ca8f0301e17fa7b841781



58. Issue #120899 —  (closed )
   - Issue detail: ### 🐛 Describe the bug I have encountered an issue with the torch.clamp function in PyTorch when it is used on tensors that reside on the Metal Performance Shaders (MPS) device. Specifically, the function behaves differently with NaN values on tensors across different devices (mps vs. cpu/cuda). This inconsistency can lead to unexpected results when working with NaN values on MPS devices. When using torch.clamp on a tensor with NaN values on an MPS device, If both min and max parameters are...
   - Issue: https://github.com/pytorch/pytorch/issues/120899
   - Fix PR #122785 — Fix torch.clamp in MPS to handle NaN correctly
   - PR: https://github.com/pytorch/pytorch/pull/122785
   - Code excerpts:     - aten/src/ATen/native/mps/operations/TensorCompare.mm: +  auto minTensor = cachedGraph->minTensor; +  auto maxTensor = cachedGraph->maxTensor; +  auto outputTensor = cachedGraph->inputTensor; + +  // clampWithTensor doesn't propagate NaN through so simula



59. Issue #118849 —  (closed )
   - Issue detail: ### 🚀 The feature, motivation and pitch as titled, things like `device_mesh["dp"]` should be cached and reused, instead of creating new one again everytime we call it. ### Alternatives _No response_ ### Additional context _No response_ cc @mrshenli @pritamdamania87 @zhaojuanmao @satgera @rohan-varma @gqchen @aazzolini @osalpekar @jiayisuse @H-Huang @kwen2501 @awgu @penguinwu @fegin @XilunWu @fduwjj @wz337 @tianyu-l @wconstab @yf225
   - Issue: https://github.com/pytorch/pytorch/issues/118849
   - Fix PR #123073 — [Cherrypick][DeviceMesh] Cache and reuse sliced result (#122975)
   - PR: https://github.com/pytorch/pytorch/pull/123073
   - Code excerpts:     - test/distributed/test_device_mesh.py: +    _world, +    @with_comms +    @run_with_both_funcol_impls +    def test_cache_and_reuse_submesh_slice_result(self): +        mesh = init_device_mesh(self.device_type, (2, 4), mesh_dim_names=("dp"



60. Issue #122016 —  (closed )
   - Issue detail: ### 🐛 Describe the bug I've been using a pytorch model daily through transformers (https://github.com/kha-white/manga-ocr) and MPS. Everything was fine with latest PyTorch and latest Transformers until the Sonoma 14.4 update which made it start crashing on startup (I was running 14.3 before and am on a M1 Max mac, for reference). Since CPU mode worked fine, I also tried older versions of PyTorch and I found anything before 2.2.0 worked fine. Bisecting it I found this commit is causing it:...
   - Issue: https://github.com/pytorch/pytorch/issues/122016
   - Fix PR #123385 — Fix for MPS regression in #122016 and #123178
   - PR: https://github.com/pytorch/pytorch/pull/123385
   - Code excerpts:     - aten/src/ATen/native/mps/operations/ConstantOps.mm: +    MPSGraphTensor* inputTensor_ = nil; +      MPSGraphTensor* inputTensor = mpsGraphScalarPlaceHolder(mpsGraph, getMPSDataType(self.scalar_type())); +      newCachedGraph->inputTensor_ = inputTensor



61. Issue #115922 —  (closed )
   - Issue detail: If you have a question or would like help and support, please ask at our [forums](https://discuss.pytorch.org/). If you are submitting a feature request, please preface the title with [feature request]. If you are submitting a bug report, please fill in the following details. ## Issue description Pytorch build from source fails Provide a short description. ## Code example `` Please try to provide a minimal example to repro the bug. Error messages and stack traces are also helpful. ## System...
   - Issue: https://github.com/pytorch/pytorch/issues/115922
   - Fix PR #122120 — Fix MSVC 14.38 - VS 2022 Build
   - PR: https://github.com/pytorch/pytorch/pull/122120
   - Code excerpts:     - aten/src/ATen/cpu/vec/vec_base.h: +    return VECTOR_WIDTH / sizeof(T);



62. Issue #120788 —  (closed )
   - Issue detail: ### 🐛 Describe the bug I implemented a naive attention block with matmul and softmax, then compared its performance with that of torch.nn.functional.scaled_dot_product_attention. I found a very strange phenomenon. torch 2.1.2： repeat：100 times naive attn total time:9.351994514465332s, avg time: 0.09351994514465332s scaled_dot_product_attention total time:10.712503671646118s, avg time: 0.10712503671646117s torch 2.2.1： repeat：100 times naive attn total time:262.39105248451233s, avg time:...
   - Issue: https://github.com/pytorch/pytorch/issues/120788
   - Fix PR #122645 — Fix lower precision check for MKLDNN on Windows
   - PR: https://github.com/pytorch/pytorch/pull/122645
   - Code excerpts:     - aten/src/ATen/native/mkldnn/Utils.h: +#if defined(__x86_64__) || (defined(_M_X64) && !defined(_M_ARM64EC)) +#if defined(__x86_64__) || (defined(_M_X64) && !defined(_M_ARM64EC))



63. Issue #118837 —  (closed )
   - Issue detail: ### 📚 The doc issue https://pytorch.org/docs/stable/distributed.checkpoint.html One example: the example code and the return type of ```get_state_dict``` are not showing up correctly. Need to fix this by 2.2.1. ![image](https://github.com/pytorch/pytorch/assets/31293777/8925b37e-72bd-4687-8146-39a031ad5d46) ### Suggest a potential alternative/fix _No response_ cc @mrshenli @pritamdamania87 @zhaojuanmao @satgera @rohan-varma @gqchen @aazzolini @osalpekar @jiayisuse @H-Huang @kwen2501 @awgu...
   - Issue: https://github.com/pytorch/pytorch/issues/118837
   - Fix PR #119804 — Correctly formatting the example in get_state_dict (#119532)
   - PR: https://github.com/pytorch/pytorch/pull/119804
   - Code excerpts:     - torch/distributed/checkpoint/state_dict.py: +        >>> # xdoctest: +SKIP +        >>> import torch +        >>> from torch.distributed.fsdp import FullyShardedDataParallel as FSDP +        >>> from torch.nn.parallel import DistributedDataPara



64. Issue #120044 —  (closed )
   - Issue detail: ### 🐛 Describe the bug When building PyTorch v2.2.0 from source, "make triton" cannot find matching distribution for Triton: ``` pip3 uninstall -y triton WARNING: Skipping triton as it is not installed. Looking in indexes: https://download.pytorch.org/whl/nightly/ ERROR: Could not find a version that satisfies the requirement pytorch-triton==2.2.0+bcad9dabe1 (from versions: 2.0.0+0d7e753227, 2.0.0+3aa3d7024e, 2.0.0+af76c989eb, 2.0.0+b8b470bc59, 2.0.0+c8bfe3f548, 2.0.0+d54c04abe2, 2.1.0,...
   - Issue: https://github.com/pytorch/pytorch/issues/120044
   - Fix PR #121229 — Fix make triton command on release branch (#121169)
   - PR: https://github.com/pytorch/pytorch/pull/121229
   - Code excerpts:     - scripts/install_triton_wheel.sh: +BRANCH=$(git rev-parse --abbrev-ref HEAD) +TRITON_VERSION="pytorch-triton==$(cat .ci/docker/triton_version.txt)" +DOWNLOAD_PYTORCH_ORG="https://download.pytorch.org/whl" + +if [[ "$BRANCH" =~ .*relea



65. Issue #118429 —  (closed )
   - Issue detail: ### 📚 The doc issue [`torch.nn.functional.pad`](https://pytorch.org/docs/stable/generated/torch.nn.functional.pad.html) refers to `torch.nn.CircularPad2d`, which does not seem to exist at all in the docs. `help(torch.nn.CircularPad2d)` shows that the docstring exists. It just doesn't seem to get built. ### Suggest a potential alternative/fix Integrate `torch.nn.CircularPad2d` (and related modules) into the docs. cc @svekars @brycebortree
   - Issue: https://github.com/pytorch/pytorch/issues/118429
   - Fix PR #119313 — Missing docs for CircularPad2d
   - PR: https://github.com/pytorch/pytorch/pull/119313
   - Code excerpts:     - docs/source/nn.rst: +    nn.CircularPad1d +    nn.CircularPad2d +    nn.CircularPad3d



66. Issue #114345 —  (closed )
   - Issue detail: ### 📚 The doc issue As per the documentation on `frombuffer` method of `torch`: ``` torch.frombuffer(buffer, *, dtype, count=-1, offset=0, requires_grad=False) → [Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor) ``` As per the documentation, either of the following conditions should be true: ``` 1. count is a positive non-zero number, and the total number of bytes in the buffer is less than offset plus count times the size (in bytes) of...
   - Issue: https://github.com/pytorch/pytorch/issues/114345
   - Fix PR #119388 — Fix typo on torch.frombuffer() documentation
   - PR: https://github.com/pytorch/pytorch/pull/119388
   - Code excerpts:     - torch/_torch_docs.py: +in the buffer is more than :attr:`offset` plus :attr:`count` times the size



67. Issue #73963 —  (closed )
   - Issue: https://github.com/pytorch/pytorch/issues/73963
   - Fix PR #74029 — Emit std::string instead of c10::string_view for Lazy IR class
   - PR: https://github.com/pytorch/pytorch/pull/74029
   - Code excerpts:     - tools/codegen/dest/lazy_ir.py: +        scalar_decls = "\n  ".join([f"std::string {t.name};" if t.cpp_type() == "c10::string_view" else f"{t.cpp_type()} {t.name};" +                                    for t in scalar_types])



68. Issue #118269 —  (closed )
   - Issue detail: ### 📚 The doc issue https://pytorch.org/docs/stable/generated/torch.randn.html does not clearly specify behavior on complex data types `torch.complex64` and `torch.complex128`. The current notation $\textrm{out}_{i} \sim \mathcal{N} (0, 1)$ may lead to users thinking that both the real and imaginary parts are sampled from a unit Gaussian, but in fact they are each i.i.d. sampled from $\mathcal{N} (0, 1/2)$, leading to the complex signal being (correctly, for a large class of applications)...
   - Issue: https://github.com/pytorch/pytorch/issues/118269
   - Fix PR #119315 — Clarified sampling process of torch.randn for complex dtypes. (#118315)
   - PR: https://github.com/pytorch/pytorch/pull/119315
   - Code excerpts:     - torch/_torch_docs.py: +For complex dtypes, the tensor is i.i.d. sampled from a `complex normal distribution`_ with zero mean and +unit variance as + +.. math:: +    \text{{out}}_{{i}} \sim \mathcal{{CN}}(0, 1) + +This is e



69. Issue #113646 —  (closed )
   - Issue detail: ### 📚 The doc issue Not sure it is the good place for reporting this, but the documentation at : https://pytorch.org/docs/stable/generated/torch.set_default_tensor_type.html doesn't state that torch.set_default_tensor_type() has been **depreciated** as of torch 2.1. ### Suggest a potential alternative/fix Redirect to torch.set_default_dtype() (https://pytorch.org/docs/stable/generated/torch.set_default_dtype.html) cc @svekars @carljparker
   - Issue: https://github.com/pytorch/pytorch/issues/113646
   - Fix PR #119316 — Updated docs for deprecated `torch.set_default_tensor_type` (#115041)
   - PR: https://github.com/pytorch/pytorch/pull/119316
   - Code excerpts:     - torch/__init__.py: +    r""" +    .. warning:: + +        This function is deprecated as of PyTorch 2.1, please use :func:`torch.set_default_dtype()` and +        :func:`torch.set_default_device()` as alternatives. + + 



70. Issue #72612 —  (closed )
   - Issue detail: ### 🐛 Describe the bug At least this test triggers an internal assert when running debug python build. ``` test_custom_function_save_for_forward (__main__.TestAutograd) ... /home/alban/local/installs/python3.8/debug/install/include/python3.8d/object.h:541: _Py_NegativeRefcount: Assertion failed: object has negative ref count Enable tracemalloc to get the memory block allocation traceback object address : 0x7ffd894af4b0 object refcount : -1 object type : 0x5555558d3ac0 object type name: tuple...
   - Issue: https://github.com/pytorch/pytorch/issues/72612
   - Fix PR #72656 — Fix refcounting in access of saved for forward attribute (#72627)
   - PR: https://github.com/pytorch/pytorch/pull/72656
   - Code excerpts:     - torch/csrc/autograd/python_function.cpp: +    Py_INCREF(self->saved_for_forward);



71. Issue #119427 —  (closed )
   - Issue detail: ### 📚 The doc issue There is a typo on the [Contribution Guide](https://pytorch.org/docs/stable/community/contribution_guide.html), in the Frequently Asked Questions. It says: > CI tests failed, what does it mean? Maybe your PR is based off a broken main bracnh? Is that mean to be a joke (broken branch), or an actual typo? If it is meant to be a joke, please ignore this issue. ### Suggest a potential alternative/fix I will be submitting a PR with the fix for the typo.
   - Issue: https://github.com/pytorch/pytorch/issues/119427
   - Fix PR #119505 — Fix typo on Contribution Guide (#119428)
   - PR: https://github.com/pytorch/pytorch/pull/119505
   - Code excerpts:     - docs/source/community/contribution_guide.rst: +   off a broken main branch? You can try to rebase your change on top



72. Issue #118737 —  (closed )
   - Issue detail: ### 🐛 Describe the bug The CI of Optuna integration, which uses Torch as a dependency, fails since the torch version was updated to v2.2.0. Please check [here](https://github.com/optuna/optuna/actions/runs/7722855986/job/21051777682) for the error message. With the version constraint `torch<2.2.0`, the same failure completely disappeared (Please check [here](https://github.com/optuna/optuna/actions/runs/7723123991/job/21052570860?pr=5217)). ### Versions The environment is described in the...
   - Issue: https://github.com/pytorch/pytorch/issues/118737
   - Fix PR #119769 — Fix TCP Store Windows (#118860)
   - PR: https://github.com/pytorch/pytorch/pull/119769
   - Code excerpts:     - torch/csrc/distributed/c10d/TCPStoreBackend.cpp: +      addMiscellaneousSocket(rawSocket);



73. Issue #112997 —  (closed )
   - Issue detail: ### 🚀 The feature, motivation and pitch Enable support for Flash Attention Memory Efficient and SDPA kernels for AMD GPUs. At present using these gives below warning with latest nightlies (torch==2.2.0.dev20231105+rocm5.6, pytorch-triton-rocm==2.1.0+34f8189eae): > model.py:187: UserWarning: 1Torch was not compiled with flash attention. (Triggered internally at ../aten/src/ATen/native/transformers/hip/sdp_utils.cpp:253.) y = F.scaled_dot_product_attention(q, k, v, attn_mask=mask,...
   - Issue: https://github.com/pytorch/pytorch/issues/112997
   - Fix PR #114309 — Initial Flash Attention support on ROCM
   - PR: https://github.com/pytorch/pytorch/pull/114309
   - Code excerpts:     - CMakeLists.txt: +# TODO: Merge this into cmake_dependent_option as "NOT MSVC AND (USE_CUDA OR USE_ROCM)" +#       once cmake_minimum_required is bumped to 3.22 +#       See https://cmake.org/cmake/help/latest/policy/



74. Issue #114591 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Hi, [torch.utils.tensorboard requires "packaging"](https://github.com/pytorch/pytorch/blob/fa1ccc34c4f65756bc50c3e3ab135c88b175b18c/torch/utils/tensorboard/__init__.py#L2C1-L3C1) to be installed but that dependency is [missing on torch 2.1.x](https://github.com/pytorch/pytorch/blob/v2.1.2-rc1/requirements.txt). Here's some example code: ```python from torch.utils.tensorboard import SummaryWriter ``` The links above point to a RC version of 2.1.2 but this is also the...
   - Issue: https://github.com/pytorch/pytorch/issues/114591
   - Fix PR #116517 — Fix missing dependency in torch.utils.tensorboard (#115598)
   - PR: https://github.com/pytorch/pytorch/pull/116517
   - Code excerpts:     - torch/utils/tensorboard/__init__.py: +from torch._vendor.packaging.version import Version



75. Issue #114628 —  (closed )
   - Issue detail: ### 🐛 Describe the bug After running `run_decompositions`, the exported program is not the same. https://github.com/pytorch/pytorch/blob/e0d2a24967218d7c39e24f66bb6c4836c9d1d427/torch/export/exported_program.py#L351-L361 However, `the state_dict` is also updated. https://github.com/pytorch/pytorch/blob/e0d2a24967218d7c39e24f66bb6c4836c9d1d427/torch/export/exported_program.py#L458-L472 Should decomposition happen in-place, instead of creating a whole new one? ### Versions main branch cc...
   - Issue: https://github.com/pytorch/pytorch/issues/114628
   - Fix PR #115753 — [export] Do not copy state_dict in run_decomp (#115269)
   - PR: https://github.com/pytorch/pytorch/pull/115753
   - Code excerpts:     - test/export/test_export.py: +        state_dict = ep.state_dict +        self.assertEqual(id(state_dict), id(ep.state_dict))



76. Issue #110832 —  (closed )
   - Issue detail: ### 🐛 Describe the bug When calling `torch.compile` on a module that uses `nn.functional.scaled_dot_product_attention(q, k, v, ...)`, backward passes do not work unless `q`, `k`, and `v` all have the same shape. This error only happens if CUDA is used; CPU appears to be fine. ```python import torch from torch import nn class BadModule(nn.Module): def __init__(self): super().__init__() self.l = nn.Linear(8, 16, bias=False) def forward(self, x): return...
   - Issue: https://github.com/pytorch/pytorch/issues/110832
   - Fix PR #112792 — Fix the meta func for mem_eff_backward (#110893)
   - PR: https://github.com/pytorch/pytorch/pull/112792
   - Code excerpts:     - torch/_meta_registrations.py: +    head_dim_v = value.size(3) +        (batch_size, num_heads, max_k, head_dim_v),



77. Issue #112577 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Hi @drisspg, after more hours of debugging than I am comfortable to admit, I noticed the following breaking change between PyTorch 2.0.1 and PyTorch 2.1. The issue can be reproduced both with `torch-2.1.0+cu118` & `2.2.0.dev20231030+cu118`. There is no issue on 2.0.1 For fp32 inputs to SDPA on CUDA device & passing a custom `attn_mask`, we have the following: * PyTorch 2.0.1: dispatches to math (`RuntimeError: No available kernel. Aborting execution.` for other...
   - Issue: https://github.com/pytorch/pytorch/issues/112577
   - Fix PR #112796 — Fix mem eff bias bug (#112673)
   - PR: https://github.com/pytorch/pytorch/pull/112796
   - Code excerpts:     - aten/src/ATen/native/transformers/attention.cpp: +  auto needs_contig = [](const c10::SymInt& stride) { +    return (stride % 16 != 0) || (stride == 0); +  }; +  if (needs_contig(attn_mask.sym_stride(0)) || +      needs_contig(attn_mask.sym_stride(1



78. Issue #109793 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Hi! We've been fuzzing PyTorch project with [sydr-fuzz](https://github.com/ispras/oss-sydr-fuzz). We've found a hcrash at `flatbuffer_loader.cpp:298` in jit module. The crash occurs because of null pointer dereference when accessing some fields of malformed flatbuffers-module. PyTorch version: cdf7f3e78032a17600f701e9153e9bb49fad8ce7 OS: Ubuntu 20.04 How to reproduce 1. Build docker from [here](https://github.com/ispras/oss-sydr-fuzz/tree/master/projects/pytorch) and...
   - Issue: https://github.com/pytorch/pytorch/issues/109793
   - Fix PR #112165 — Verify flatbuffer module fields are initialized (#109794)
   - PR: https://github.com/pytorch/pytorch/pull/112165
   - Code excerpts:     - torch/csrc/jit/mobile/flatbuffer_loader.cpp: +      ivalues && module->object_types(), +      "Parsing flatbuffer module: Corrupted ivalues/object_types field"); +  TORCH_CHECK( +      reinterpret_cast<const char*>(ivalues) < end, "Corrupted iva



79. Issue #108869 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Sharded checkpointing (particularly with FSDP for the optimizer state) uses ChunkShardingSpec to save/load tensors. ChunkShardingSpec's behavior is similar to torch.chunk and will result in some chunks of size 0. This can be reproduced by trying to save a tensor of size 6 with 4 gpus. This tensor is sharded across the first 3 gpus. The resulting size of the chunks will look like [2, 2, 2, 0]. On save, it seems like ChunkShardingSpec is aware of which gpus contain...
   - Issue: https://github.com/pytorch/pytorch/issues/108869
   - Fix PR #111151 — Update chunk_sharding_spec.py (#108915)
   - PR: https://github.com/pytorch/pytorch/pull/111151
   - Code excerpts:     - torch/distributed/_shard/sharding_spec/chunk_sharding_spec.py: +            shard_size = list(tensor_sizes) +            current_offsets = [0] * tensor_num_dim +            current_offsets[self.dim] = split_size * idx  # type: ignore[index] +            shard_siz



80. Issue #109186 —  (closed )
   - Issue detail: ### 🐛 Describe the bug torch.var ``` x = torch.arange(12, dtype=torch.float32).reshape(1,3,2,2) torch.var(x, dim=2, correction=3) ``` output: ``` >>> torch.var(x, dim=2, correction=3) tensor([[[inf, inf], [inf, inf], [inf, inf]]]) >>> ``` In above N=2 because dim=2 and above example dim=2 is 2 Now if we increase the correction value greater than dim value i.e. 2 in this case then it result in inf for all element. But as per formula https://pytorch.org/docs/stable/generated/torch.var.html . it...
   - Issue: https://github.com/pytorch/pytorch/issues/109186
   - Fix PR #110969 — Improved the docs for torch.std, torch.var, torch.std_mean, torch.var…
   - PR: https://github.com/pytorch/pytorch/pull/110969
   - Code excerpts:     - torch/_torch_docs.py: +The sample covariance of the variables :math:`x` and :math:`y` is given by: +    \text{cov}(x,y) = \frac{\sum^{N}_{i = 1}(x_{i} - \bar{x})(y_{i} - \bar{y})}{\max(0,~N~-~\delta N)} +where :math:`\bar{



81. Issue #110643 —  (closed )
   - Issue detail: ### 🚀 The feature, motivation and pitch Please add CUDA 12.x official images. ### Alternatives _No response_ ### Additional context https://github.com/pytorch/pytorch/issues/91122#issuecomment-1749534410
   - Issue: https://github.com/pytorch/pytorch/issues/110643
   - Fix PR #110705 — Move Docker official builds to Cuda 12.1.1 (#110703)
   - PR: https://github.com/pytorch/pytorch/pull/110705
   - Code excerpts:     - docker.Makefile: +CUDA_VERSION              = 12.1.1



82. Issue #109387 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Consider following trivial sample: ```python import torch def foo(x: torch.Tensor) -> torch.Tensor: return torch.sin(x) + torch.cos(x) if __name__=="__main__": x = torch.rand(3, 3, device="cuda") x_eager = foo(x) x_pt2 = torch.compile(foo)(x) print(torch.allclose(x_eager, x_pt2)) ``` Following sample can be executed on vanilla `ubuntu:20.04` using 2.0.1, but fails with 2.1 release candidate, due to the spurious dependencies: ```shell % python3 foo.py ... File...
   - Issue: https://github.com/pytorch/pytorch/issues/109387
   - Fix PR #109608 — [release-2.1] Make numpy dependency optional for torch.compile
   - PR: https://github.com/pytorch/pytorch/pull/109608
   - Code excerpts:     - torch/_dynamo/variables/constant.py: +        if np is not None and isinstance(value, np.number):



83. Issue #108472 —  (closed )
   - Issue detail: ### 🐛 Describe the bug This is already fixed on main by https://github.com/pytorch/pytorch/pull/108168 ``` def test_adding_tensor_offsets(self): @torch.compile(fullgraph=True) def fn(x): return x[16:32] with torch.no_grad(): x = torch.randn(1024, device=self.device) self.assertEqual(fn(x[0:]), x[16:][:16]) self.assertEqual(fn(x[128:]), x[128 + 16 :][:16]) ``` Fails with ``` Traceback (most recent call last): File "/home/jansel/conda/envs/pytorch/lib/python3.10/unittest/case.py", line 59, in...
   - Issue: https://github.com/pytorch/pytorch/issues/108472
   - Fix PR #108259 — [inductor] Fix inputs with existing offsets
   - PR: https://github.com/pytorch/pytorch/pull/108259
   - Code excerpts:     - test/inductor/test_cpp_wrapper.py: +        BaseTest("test_adding_tensor_offsets"), +        BaseTest("test_adding_tensor_offsets"),



84. Issue #106085 —  (closed )
   - Issue detail: ### 📚 The doc issue The RNN, LSTM, and GRU classes are initialized with *args and **kwargs, despite the docstring specifying a list of possible arguments. This can be a mild annoyance for those using editors with signature helpers and may confuse users about PyTorch's implementation of RNNs. Additionally, there is no documentation of the RNNBase class to explain its purpose in the PyTorch codebase. ### Suggest a potential alternative/fix Trivial changes to the...
   - Issue: https://github.com/pytorch/pytorch/issues/106085
   - Fix PR #108385 — Update to RNN documentation (#106222)
   - PR: https://github.com/pytorch/pytorch/pull/108385
   - Code excerpts:     - torch/nn/modules/rnn.py: +    r"""Base class for RNN modules (RNN, LSTM, GRU). + +    Implements aspects of RNNs shared by the RNN, LSTM, and GRU classes, such as module initialization +    and utility methods for parameter s



85. Issue #97737 —  (closed )
   - Issue detail: Slack thread: https://pytorch.slack.com/archives/GEEQ2K4MD/p1679962409906099 I was seeing some massive (~2x) slowdowns on a job after running it on PyTorch 2.0. From some profiling in `py-spy` it looked like the pin_memory thread was doing a lot more work than before. Looking at a trace in `nsys` I saw the thread doing the forward pass having a bunch of `pthread_cond_timedwait` with GIL reacquire calls in it’s call stack, and it seemed like the thread doing the forward pass was getting...
   - Issue: https://github.com/pytorch/pytorch/issues/97737
   - Fix PR #98055 — [release v2.0.1] Revisit `torch._six.string_classes` removal (#97737, #97789, #97863)
   - PR: https://github.com/pytorch/pytorch/pull/98055
   - Code excerpts:     - test/distributed/test_store.py: +        if not isinstance(key, (str, bytes)):



86. Issue #61835 —  (closed )
   - Issue detail: ## 🐛 Bug Broadcasting documentation diverges from implementation. ## To Reproduce The [broadcasting documentation](https://pytorch.org/docs/stable/notes/broadcasting.html#general-semantics) stipulates two conditions to determine if two tensors are broadcastable: > 1. Each tensor has at least one dimension. > 2. When iterating over the dimension sizes, starting at the trailing dimension, the dimension sizes must either be equal, one of them is 1, or one of them does not exist. The first rule...
   - Issue: https://github.com/pytorch/pytorch/issues/61835
   - Fix PR #66029 — broadcasting doc fix
   - PR: https://github.com/pytorch/pytorch/pull/66029
   - Code excerpts:     - docs/source/notes/broadcasting.rst: +Two tensors are "broadcastable" if when iterating over the dimension sizes, +starting at the trailing dimension, the dimension sizes must either be equal, +one of them is 1, or one of them does not e



87. Issue #97720 —  (closed )
   - Issue detail: ### 🐛 Describe the bug When writing a custom module which implements the __getitem__ method dynamo fails with AssertionError. For more context on this (e.g. why a custom module for this) see: https://github.com/pytorch/pytorch/issues/71203 and https://github.com/ludwig-ai/ludwig/blob/master/ludwig/features/feature_utils.py#L150 cc @ezyang @soumith @msaroufim @wconstab @ngimel @bdhirsh @voznesenskym @penguinwu @anijain2305 @EikanWang @jgong5 @Guobing-Chen @XiaobingSuper @zhuhaozhe @blzheng...
   - Issue: https://github.com/pytorch/pytorch/issues/97720
   - Fix PR #98381 — Support Modules with custom __getitem__ method through inlining (#97932)
   - PR: https://github.com/pytorch/pytorch/pull/98381
   - Code excerpts:     - test/dynamo/test_modules.py: +class CustomGetItemModuleList(torch.nn.Module): +    def __init__(self): +        super().__init__() +        self.layers = torch.nn.ModuleList( +            [ +                torch.nn.Linear(10, 10



88. Issue #7278 —  (closed )
   - Issue detail: ## Issue description Python segfaults if torch.tensor is created from the pandas series slice. ## Code example ``` import torch import pandas as pd seq = pd.Series([0.1, 0.2, 0.3]) print(seq) # outputs: #0 0.1 #1 0.2 #2 0.3 #dtype: float64 print(torch.tensor(seq)) # OK # outputs: #tensor([ 0.1000, 0.2000, 0.3000]) torch.tensor(seq[1:]) # SEGFAULT ``` ## System Info ``` PyTorch version: 0.4.0 Is debug build: No CUDA used to build PyTorch: None OS: Ubuntu 16.04.3 LTS GCC version: (Ubuntu...
   - Issue: https://github.com/pytorch/pytorch/issues/7278
   - Fix PR #7583 — Throw error on tensor creation when sequence shape cannot be determined
   - PR: https://github.com/pytorch/pytorch/pull/7583
   - Code excerpts:     - test/test_torch.py: +    def test_tensor_from_sequence(self): +        class MockSequence(object): +            def __init__(self, lst): +                self.lst = lst + +            def __len__(self): +                



89. Issue #95958 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Running `compile()` on a function that builds an attention mask and passes a tensor through a `TransformerEncoder` results in the dtype of the mask getting changed, triggering an exception: ``` import torch import torch.nn as nn def transformer_encoder(inputs, input_seq_len): encoder_layer = nn.TransformerEncoderLayer( d_model=16, nhead=2, dim_feedforward=32, dropout=0.1, activation='relu', batch_first=True, ) encoder_norm = nn.LayerNorm(16) encoder =...
   - Issue: https://github.com/pytorch/pytorch/issues/95958
   - Fix PR #96462 — [inductor] use triu ref instead of lowering (#96040)
   - PR: https://github.com/pytorch/pytorch/pull/96462
   - Code excerpts:     - test/inductor/test_torchinductor_opinfo.py: +    "triu",



90. Issue #91516 —  (closed )
   - Issue detail: ### 🐛 Describe the bug The use of `np.greater(counts, 0, dtype=np.int32)` in `add_histogram` is deprecated a while ago, and the deprecation expired in Numpy 1.24+: > The `dtype=` argument to comparison ufuncs is now applied correctly. That > means that only `bool` and `object` are valid values and `dtype=object` is > enforced. Source: https://numpy.org/doc/stable/release/1.24.0-notes.html#expired-deprecations Minimal example: ```python from torch.utils.tensorboard import SummaryWriter import...
   - Issue: https://github.com/pytorch/pytorch/issues/91516
   - Fix PR #96452 — Fix expired deprecation of comparison dtype for NumPy 1.24+ (#91517)
   - PR: https://github.com/pytorch/pytorch/pull/96452
   - Code excerpts:     - torch/utils/tensorboard/summary.py: +    cum_counts = np.cumsum(np.greater(counts, 0))



91. Issue #95523 —  (closed )
   - Issue detail: ### 🐛 Describe the bug See description in https://github.com/pytorch/builder/issues/1318#issuecomment-1444635570 We need to make sure examples would work even in absence of "export CUDA_HOME=/usr/local/cuda-11.7". ### Versions v2.0.0-rc2.
   - Issue: https://github.com/pytorch/pytorch/issues/95523
   - Fix PR #95577 — Cherry pick triton cuda.h fix
   - PR: https://github.com/pytorch/pytorch/pull/95577
   - Code excerpts:     - .github/ci_commit_pins/triton.txt: +b8b470bc597c1c5bd03682c09fe3e6b7c53787fd



92. Issue #95266 —  (closed )
   - Issue detail: ### 🐛 Describe the bug I ran into a strange error where the compiler failed to identify/match the signature of the function. ```python import torch import torch.nn as nn class Model(nn.Module): def __init__(self, n_embd=768, bias=False): super().__init__() self.n_head = 6 self.embd = nn.Embedding(50257, 768) self.c_attn = nn.Linear(in_features=n_embd, out_features=3 * n_embd, bias=bias) self.dropout = 0 def forward(self, x): x = self.embd(x) (B, T, C) = x.size() q, k, v =...
   - Issue: https://github.com/pytorch/pytorch/issues/95266
   - Fix PR #95397 — Cherrypick for 2.0: [SDPA] Fix bug in parsing scaled_dot_product_attention arguments 
   - PR: https://github.com/pytorch/pytorch/pull/95397
   - Code excerpts:     - test/dynamo/test_dynamic_shapes.py: +unittest.expectedFailure( +    DynamicShapesMiscTests.test_parsing_sdpa_dynamic_shapes +    # Cannot call sizes() on tensor with symbolic sizes/strides +) +



93. Issue #95082 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Trying the nightlies today (20230217) on RTX 4090 I get the following error when attempting to use `compile()`: ``` RuntimeError: Internal Triton PTX codegen error: ptxas /tmp/filelSnH8K, line 6; error : PTX .version 7.4 does not support .target sm_89 ptxas fatal : Ptx assembly aborted due to errors ``` As mentioned in #95081, the resolved nightly is `2.0.0.dev20230213+cu118`. Repeating the same test with the cuda 11.7 wheels, the behavior is identical. ### Error logs...
   - Issue: https://github.com/pytorch/pytorch/issues/95082
   - Fix PR #95285 — Update triton hash (#95247)
   - PR: https://github.com/pytorch/pytorch/pull/95285
   - Code excerpts:     - .github/ci_commit_pins/triton.txt: +d54c04abe2c3e67b2139c68cdbda87b59e8dd01b



94. Issue #87313 —  (closed )
   - Issue detail: ### 🐛 Describe the bug I have spotted improper model conversion to ONNX when using `torch.onnx.OperatorExportTypes.ONNX_ATEN` flag with `PyTorch >=1.12.0` My understanding from the [documentation](https://pytorch.org/docs/stable/onnx.html#aten-operators) > OperatorExportTypes.ONNX_ATEN: All ATen ops (in the TorchScript namespace “aten”) are exported as ATen ops (in opset domain “org.pytorch.aten”). [ATen](https://pytorch.org/cppdocs/#aten) is PyTorch’s built-in tensor library, so this...
   - Issue: https://github.com/pytorch/pytorch/issues/87313
   - Fix PR #90104 — Fix ATen Fallback for BUILD_CAFFE2=0 for ONNX-only ops (#88504)
   - PR: https://github.com/pytorch/pytorch/pull/90104
   - Code excerpts:     - test/onnx/test_pytorch_onnx_no_runtime.py: +import numpy as np + +from torch.onnx import OperatorExportTypes, symbolic_helper, utils +from torch.testing._internal import common_quantization, common_utils +    def test_caffe2_aten_fallback_must



95. Issue #88049 —  (closed )
   - Issue detail: ### 🐛 Describe the bug This is an installation issue. Poetry parses the endpoint at `https://pypi.org/pypi/torch/1.13/json` to get dependency metadata. The endpoint returns: ``` "requires_dist": [ "typing-extensions", "nvidia-cuda-runtime-cu11 (==11.7.99)", "nvidia-cudnn-cu11 (==8.5.0.96)", "nvidia-cublas-cu11 (==11.10.3.66)", "nvidia-cuda-nvrtc-cu11 (==11.7.99)", "opt-einsum (>=3.3) ; extra == 'opt-einsum'" ], ``` However, the packages `nvidia-cuda-runtime-cu11` , `nvidia-cudnn-cu11`,...
   - Issue: https://github.com/pytorch/pytorch/issues/88049
   - Fix PR #89924 — Add platform markers for linux only extra_install_requires (#88826)
   - PR: https://github.com/pytorch/pytorch/pull/89924
   - Code excerpts:     - .github/scripts/generate_binary_build_matrix.py: +                        "nvidia-cuda-runtime-cu11; platform_system == 'Linux' | " +                        "nvidia-cudnn-cu11==8.5.0.96; platform_system == 'Linux' | " +                        "nvidi



96. Issue #87595 —  (closed )
   - Issue detail: ### 🐛 Describe the bug This problem only occurs when I use RTX4090. ```python import torch a = torch.tensor([2, 2, 3]).cuda(0) print(a.prod()) ``` ``` Traceback (most recent call last): File "xxxxxxx.py", line 3, in <module> print(a.prod()) RuntimeError: #define POS_INFINITY __int_as_float(0x7f800000) #define INFINITY POS_INFINITY #define NEG_INFINITY __int_as_float(0xff800000) #define NAN __int_as_float(0x7fffffff) typedef long long int int64_t; typedef unsigned int uint32_t; typedef signed...
   - Issue: https://github.com/pytorch/pytorch/issues/87595
   - Fix PR #87618 — attempted fix for nvrtc with lovelace (#87611)
   - PR: https://github.com/pytorch/pytorch/pull/87618
   - Code excerpts:     - aten/src/ATen/native/cuda/jit_utils.cpp: +  } else if (nvrtc_major == 11 && nvrtc_minor < 8) { +    max_dev_version = CUDAVersion(8, 6);



97. Issue #44964 —  (closed )
   - Issue detail: Maybe some simpler type annotations can be introduced. Currently it's `kernel_size: Union[T, Tuple[T, ...]], stride: Optional[Union[T, Tuple[T, ...]]]`, and it's hard to parse, especially since it's so comon and clutters the signatures. Can we introduce some type alias `int_or_inttuple` or something in this spirit? ![image](https://user-images.githubusercontent.com/1041752/93633775-c8d31c80-f9ef-11ea-81ce-4e8d11b1aff3.png) cc @jlin27 @ezyang @malfet @rgommers @xuzhao9 @gramster
   - Issue: https://github.com/pytorch/pytorch/issues/44964
   - Fix PR #86851 — [DOC] Use type hints to show annotation in the docs
   - PR: https://github.com/pytorch/pytorch/pull/86851
   - Code excerpts:     - docs/source/conf.py: +# Show type hints in the description +autodoc_typehints = 'description' + +# Add parameter types if the parameter is documented in the docstring +autodoc_typehints_description_target = 'documented_pa



98. Issue #86325 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Here, onnx.export fails if called on a ScriptedModule that has been frozen: ```python import torch class Inner(torch.nn.Module): def forward(self, x): if x > 0 : return x else: return x*x class Outer(torch.nn.Module): def __init__(self): super().__init__() i = Inner() self.inner = torch.jit.script(i) def forward(self, x): return self.inner(x) x = torch.zeros(1) o=Outer() o.eval() m = torch.jit.trace_module(o, { 'forward' : (x)}) # borisf: passes if you comment this line...
   - Issue: https://github.com/pytorch/pytorch/issues/86325
   - Fix PR #87457 — [ONNX] Reland: Update training state logic to support ScriptedModule …
   - PR: https://github.com/pytorch/pytorch/pull/87457
   - Code excerpts:     - test/onnx/test_utility_funs.py: +import warnings +import parameterized +from torch.onnx import _constants, OperatorExportTypes, TrainingMode, utils +@parameterized.parameterized_class( +    [ +        {"opset_version": opset} +     



99. Issue #81 —  (closed )
   - Issue detail: Two problems: 1. The Python extension is compiled without OpenMP support even though TH is built with it, so set_num_threads is incorrectly a no-op / warning 2. Python is complaining about the return value ``` python >>> torch.set_num_threads(1) __main__:1: RuntimeWarning: set_num_threads is a no-op - torch was compiled without OpenMP support Traceback (most recent call last): File "<stdin>", line 1, in <module> SystemError: <built-in function set_num_threads> returned NULL without setting an...
   - Issue: https://github.com/pytorch/pytorch/issues/81
   - Fix PR #132 — Use THSetNumThreads instead of omp_set_num_threads
   - PR: https://github.com/pytorch/pytorch/pull/132
   - Code excerpts:     - torch/csrc/Module.cpp: +  return PyLong_FromLong(THGetNumThreads()); +  THSetNumThreads((int)THPUtils_unpackLong(arg)); +  Py_RETURN_NONE;



100. Issue #2002 —  (closed )
   - Issue detail: I build pytorch from source. All distributed tests failed on MAC: Running distributed tests for the TCP backend Process process 0: Process process 1: Process process 2: Traceback (most recent call last): File "/usr/local/anaconda3/envs/pytorch-dev/lib/python3.6/multiprocessing/process.py", line 249, in _bootstrap self.run() File "/usr/local/anaconda3/envs/pytorch-dev/lib/python3.6/multiprocessing/process.py", line 93, in run self._target(*self._args, **self._kwargs) File...
   - Issue: https://github.com/pytorch/pytorch/issues/2002
   - Fix PR #2004 — Skip distributed tests if not supported
   - PR: https://github.com/pytorch/pytorch/pull/2004
   - Code excerpts:     - test/test_distributed.py: +if not dist.is_available(): +    print('Distributed not available, skipping tests') +    sys.exit(0) + +



101. Issue #81129 —  (closed )
   - Issue detail: ### 🐛 Describe the bug The following code, which runs on torch 1.11 cpu, doesn't anymore on torch 1.12: ```python import torch model = torch.nn.TransformerEncoderLayer(d_model=512, nhead=8, batch_first=True) src = torch.rand(32, 10, 512) src_mask = torch.zeros(10, 10).to(torch.bool) model.eval() with torch.no_grad(): print(model(src, src_mask)) ``` It raises ``` Traceback (most recent call last): File "/Users/adm/Desktop/main.py", line 9, in <module> print(model(src, src_mask)) File...
   - Issue: https://github.com/pytorch/pytorch/issues/81129
   - Fix PR #81952 — 1.12.1/bt fix
   - PR: https://github.com/pytorch/pytorch/pull/81952
   - Code excerpts:     - aten/src/ATen/native/nested/NestedTensorMath.cpp: +  auto target_size = NestedTensor_get_max_size_from_size_tensor(sizes); +  // There may be extra padding on padded beyond the max size in the nested tensor. +  // Make the mask size match. +  const s



102. Issue #2348 —  (closed )
   - Issue detail: When both PyTorch and Pandas are imported, calling `loss.backward()` results in a segfault. The issue was originally reported by @EthanRosenthal [here](https://github.com/maciejkula/spotlight/issues/42) It looks like calling `PyThreadState_GET()` returns a null pointer here: https://github.com/python/cpython/blob/5fd33b5926eb8c9352bf5718369b4a8d72c4bb44/Python/errors.c#L28 Examining in GDB: ``` (gdb) down #0 PyErr_Restore (type=0x0, value=<optimised out>, traceback=0x0) at Python/errors.c:42...
   - Issue: https://github.com/pytorch/pytorch/issues/2348
   - Fix PR #2581 — Ensure GIL is held in ObjectPtrAllocators
   - PR: https://github.com/pytorch/pytorch/pull/2581
   - Code excerpts:     - torch/csrc/allocators.cpp: +#include "torch/csrc/utils/auto_gil.h" +  { +    AutoGIL gil; +    object = nullptr; +  } +  { +    AutoGIL gil; +    PyObject_SetAttrString(object.get(), "cdata", Py_None); +    object = nullptr; + 



103. Issue #80898 —  (closed )
   - Issue detail: ### This issue is placeholder for the list of MPS cherry picks for 1.12.1 release MPS cherry picks for 1.12.1, please list all PR's that needs to be cherry-picked for 1.12.1 that fixes MPS issues: ### Versions 1.12.0 cc @kulinseth @albanD
   - Issue: https://github.com/pytorch/pytorch/issues/80898
   - Fix PR #81976 — MPS cherry picks for 1.12.1
   - PR: https://github.com/pytorch/pytorch/pull/81976
   - Code excerpts:     - .github/workflows/_mac-test-arm64.yml: +          conda create -yp "${ENV_NAME}" "python=${PY_VERS}" numpy expecttest pyyaml



104. Issue #80733 —  (closed )
   - Issue detail: ### 🐛 Describe the bug In PyTorch version 1.12.0, `model.share_memory()` on a CUDA tensor no longer no-ops and instead crashes with error `RuntimeError: _share_fd_: only available on CPU`. Version 1.11.0 correctly no-ops ``` import torch model = torch.nn.Linear(3, 1) model.to(torch.device('cuda:0')) model.share_memory() ``` Running above gets the output ``` Traceback (most recent call last): File "/home/andrew_huggingface_co/test.py", line 5, in <module> model.share_memory() File...
   - Issue: https://github.com/pytorch/pytorch/issues/80733
   - Fix PR #81867 — Fix `Module.share_memory` error (#80843) (#80843)
   - PR: https://github.com/pytorch/pytorch/pull/81867
   - Code excerpts:     - test/test_torch.py: +    @onlyCUDA +    def test_module_share_memory(self): +        # Test fix for issue #80733 +        # See https://github.com/pytorch/pytorch/issues/80733 +        model = torch.nn.Linear(3, 1) +    



105. Issue #78490 —  (closed )
   - Issue detail: ### 🐛 Describe the bug The issue appears on MacOS py3.8, it started after updating to the latest nightly `1.13.0.dev20220525-py3.8_0` from core (previously I was at `1.12.0.dev20220309-py3.8_0`, so the issue could have been introduced earlier than May 25th). I'm receiving the following after importing numpy and pytorch together: ``` $ python -c "import numpy;import torch" OMP: Error pytorch/vision#15: Initializing libiomp5.dylib, but found libomp.dylib already initialized. OMP: Hint This...
   - Issue: https://github.com/pytorch/pytorch/issues/78490
   - Fix PR #81873 — Don't include libiomp with conda install on MacOS (#78632) (#78632)
   - PR: https://github.com/pytorch/pytorch/pull/81873
   - Code excerpts:     - setup.py: +package_type = os.getenv('PACKAGE_TYPE', 'wheel') + +        if IS_DARWIN and package_type != 'conda': +            self._embed_libiomp()



106. Issue #81106 —  (closed )
   - Issue detail: ### 🐛 Describe the bug Code to reproduce bug: ``` import gc import torch import torchvision def bench(model, device, memory_format): model = model.to(device=device, dtype=torch.float, memory_format=memory_format, non_blocking=False) model.eval() batch = torch.rand(8,3,256,256, device=device).to(device=device, dtype=torch.float, memory_format=memory_format, non_blocking=False) gc.collect() torch.cuda.empty_cache() torch.cuda.synchronize() with torch.inference_mode(): with...
   - Issue: https://github.com/pytorch/pytorch/issues/81106
   - Fix PR #81888 — Cudnn conv cache key patch (#81418) (#81418)
   - PR: https://github.com/pytorch/pytorch/pull/81888
   - Code excerpts:     - aten/src/ATen/native/cudnn/ConvShared.cpp: +    << "    memory_format = " << params.memory_format << "\n" +    int64_t groups, bool deterministic, bool allow_tf32, at::MemoryFormat memory_format) { +  params->memory_format = memory_format;



107. Issue #79449 —  (closed )
   - Issue detail: https://github.com/pytorch/pytorch/blob/c10908cd41f6fe18a4d61704d7013d46bb05aeaf/torch/utils/data/dataloader.py#L261 `ws` is not defined within the elif statement. cc @VitalyFedyunin @ejguan @NivekT
   - Issue: https://github.com/pytorch/pytorch/issues/79449
   - Fix PR #79550 — [Release 1.12][DataLoader] Fix the world_size when distributed sharding MapDataPipe (#79524)
   - PR: https://github.com/pytorch/pytorch/pull/79550
   - Code excerpts:     - torch/utils/data/dataloader.py: +            ws, rank = _get_distributed_settings()



108. Issue #74016 —  (closed )
   - Issue detail: ### 🐛 Describe the bug https://github.com/pytorch/pytorch/pull/66970#issuecomment-1063643284 produces these warnings ``` (/home/ezyang/local/pytorch-tmp-env) [ezyang@devvm066.ash0 ~/local/labs] MASTER_ADDR=localhost MASTER_PORT=29500 python worker0.py tensor([-0.6383, 0.2935, 0.6883, -0.9899], requires_grad=True) Exception ignored in: <function StorageWeakRef.__del__ at 0x7f15538914c0> Traceback (most recent call last): File "/data/users/ezyang/pytorch-...
   - Issue: https://github.com/pytorch/pytorch/issues/74016
   - Fix PR #79315 — Fix `_free_weak_ref` error (#78575)
   - PR: https://github.com/pytorch/pytorch/pull/79315
   - Code excerpts:     - test/distributed/rpc/test_share_memory.py: +#!/usr/bin/env python3 +# Owner(s): ["oncall: distributed"] + +import torch +import torch.distributed as dist + +if not dist.is_available(): +    print("Distributed not available, skipping tests", fi



109. Issue #79583 —  (closed )
   - Issue detail: ### 🐛 Describe the bug > File "/home/sacha/.local/lib/python3.10/site-packages/torch/jit/_serialization.py", line 162, in load > cpp_module = torch._C.import_ir_module(cu, str(f), map_location, _extra_files) > RuntimeError: expected ) but found 'number' here: > Serialized File "code/__torch__/backbone/sacha.py", line 189 > softmax2_blocks : __torch__.torch.nn.modules.container.___torch_mangle_550.Sequential > last_blocks : __torch__.backbone.common.___torch_mangle_558.sacha_IR > def...
   - Issue: https://github.com/pytorch/pytorch/issues/79583
   - Fix PR #79983 — [JIT] Imbue stringbuf with C locale (#79929)
   - PR: https://github.com/pytorch/pytorch/pull/79983
   - Code excerpts:     - torch/csrc/jit/ir/ir.cpp: +#include <locale> +#ifndef _WIN32 +      // Protect 12345 integer from becoming "1,2345" if some other process sets +      // global locale For more details see +      // https://github.com/pytorch/p



110. Issue #79828 —  (closed )
   - Issue detail: ### 🐛 Describe the bug After this https://github.com/pytorch/pytorch/pull/78765 is landed, when running training script in multi-GPUs environment with `DataLoader` + `DataPipe`, there will an Error raised `RuntimeError: Tensors must be CUDA and dense` See the user reported issue: https://fburl.com/teyw5gen ### Versions nightly cc @SsnL @VitalyFedyunin @ejguan @NivekT @pietern @mrshenli @pritamdamania87 @zhaojuanmao @satgera @rohan-varma @gqchen @aazzolini @osalpekar @jiayisuse @SciPioneer...
   - Issue: https://github.com/pytorch/pytorch/issues/79828
   - Fix PR #79890 — [Release 1.12][DataLoader] Share seed via Distributed Store to get rid of CUDA dependency
   - PR: https://github.com/pytorch/pytorch/pull/79890
   - Code excerpts:     - torch/utils/data/dataloader.py: +            _shared_seed = torch.empty((), dtype=torch.int64).random_(generator=self.generator).item() +                ws = dist.get_world_size() +                store = dist.distributed_c10d._get_



111. Issue #73989 —  (closed )
   - Issue: https://github.com/pytorch/pytorch/issues/73989
   - Fix PR #74133 — [LT] Make lazy_bench.py regconize detectron2 outputs
   - PR: https://github.com/pytorch/pytorch/pull/74133
   - Code excerpts:     - lazy_tensor_core/lazy_bench.py: +import traceback +    try: +        import detectron2.structures +        if ( +            isinstance(tensors, detectron2.structures.instances.Instances) +        ): +            # an Instances is a



112. Issue #72501 —  (closed )
   - Issue detail: ### 📚 The doc issue ![image](https://user-images.githubusercontent.com/19503980/152934194-21e04bea-c153-48e0-812c-d3ced6eb9d6d.png) Ref: https://pytorch.org/docs/master/generated/torch.nn.Conv3d.html#torch.nn.Conv3d cc: @jbschlosser ### Suggest a potential alternative/fix _No response_ cc @brianjo @mruberry @albanD @jbschlosser @walterddr @kshitij12345
   - Issue: https://github.com/pytorch/pytorch/issues/72501
   - Fix PR #73049 — Fix doc regressions for various modules and functional forms (#73014)
   - PR: https://github.com/pytorch/pytorch/pull/73049
   - Code excerpts:     - torch/nn/functional.py: +      additional dimensions, including none +    r"""multi_margin_loss(input, target, p=1, margin=1, weight=None, size_average=None, reduce=None, reduction='mean') -> Tensor



113. Issue #74182 —  (closed )
   - Issue: https://github.com/pytorch/pytorch/issues/74182
   - Fix PR #74183 — [LT] Skip tacotron2 and demucs in lazy_bench.py
   - PR: https://github.com/pytorch/pytorch/pull/74183
   - Code excerpts:     - lazy_tensor_core/lazy_bench.py: +    "densenet121": "Disabled by torchbench upstream due to OOM on T4 CI machine", +    "timm_nfnet": "Disabled by torchbench upstream due to OOM on T4 CI machine", +    "tacotron2": "Disabled by torc



114. Issue #65576 —  (closed )
   - Issue detail: Using the prototype #64104 to code-gen all IRs and TorchScript lowerings needed by running full TorchBench. This issue will also keep tracking improvement needed/made over the prototype. ### Tasks (grouped by models) hf_Bert: - [x] _copy_from (N.A., see doc) - [x] add (#66912) - [x] addcdiv_ (#66895) - [x] bmm (@wconstab #66998) - [x] div ((#67044)) - [x] embedding_dense_backward (#67044) - [ ] expand (@alanwaketan, non-trivial, save for later) - [ ] fill_ (@alanwaketan, non-trivial, save for...
   - Issue: https://github.com/pytorch/pytorch/issues/65576
   - Fix PR #70018 — [LTC] Code-gen nll_loss2d_forward
   - PR: https://github.com/pytorch/pytorch/pull/70018
   - Code excerpts:     - lazy_tensor_core/lazy_tensor_core/csrc/LazyShapeInference.cpp: +std::vector<Shape> compute_shape_nll_loss2d_forward( +    const at::Tensor& self, const at::Tensor& target, +    const c10::optional<at::Tensor>& weight, int64_t reduction, +    int64_t ignore_index)



115. Issue #70886 —  (closed )
   - Issue detail: ### 🚀 The feature, motivation and pitch Get "RuntimeError: Exporting the operator nan_to_num to ONNX opset version 9 is not supported. Please feel free to request support or submit a pull request on PyTorch GitHub." when using `torch.nan_to_num()` ```python import torch import pytorch_lightning as pl class SimpleModel(pl.LightningModule): def __init__(self): super().__init__() self.l1 = torch.nn.Linear(in_features=64, out_features=4) def forward(self, x): y = self.l1(x.view(x.size(0), -1)) y...
   - Issue: https://github.com/pytorch/pytorch/issues/70886
   - Fix PR #72090 — [ONNX] Add torch.nan_to_num and torch.maximum/minimum symbolic
   - PR: https://github.com/pytorch/pytorch/pull/72090
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +    @skipIfUnsupportedMinOpsetVersion(10)  # ONNX IsNaN, IsInf op is added in opset 9, 10 respectively. +    def test_nan_to_num(self): +        class NoParams(torch.nn.Module): +            def forw



116. Issue #48303 —  (closed )
   - Issue detail: ## 🐛 Bug ```torch.nn.functional.cosine_similarity``` is not ONNX-exportable. Pytorch told me to open an issue. ## To Reproduce ``` class exampleNet(nn.Module): def __init__(self): super(exampleNet, self).__init__() def forward(self, x1, x2): return F.cosine_similarity(x1, x2, dim=-1) n = exampleNet().eval() x1 = torch.rand((1, 32, 32, 256)) x2 = torch.rand((1, 32, 32, 256)) r = n(x1,x2) torch.onnx.export(n, (x1, x2,), "model.onnx", export_params=True, opset_version=12) ``` If you run the...
   - Issue: https://github.com/pytorch/pytorch/issues/48303
   - Fix PR #72128 — [ONNX] Add symbolic support for torch.nn.cosinesimilarity
   - PR: https://github.com/pytorch/pytorch/pull/72128
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +    @skipIfUnsupportedMinOpsetVersion(9) +    def test_cosine_similarity(self): +        x = torch.randn(5, 3, 2) +        y = torch.randn(5, 3, 2) +        self.run_test(torch.nn.CosineSimilarity(di



117. Issue #72399 —  (closed )
   - Issue detail: ### 🐛 Describe the bug The following code export runnable onnx until PyTorch 1.10 (tested and still work in 1.8 & 1.9), the exported onnx no longer work after that. ``` import torch import torch.nn as nn class testModel(nn.Module): def __init__(self): super(testModel, self).__init__() self.rnn1 = nn.LSTM(8, 8, bidirectional=True, batch_first=True) self.linear1 = nn.Linear(8 * 2, 8) self.rnn2 = nn.LSTM(8, 8, bidirectional=True, batch_first=True) self.linear2 = nn.Linear(8 * 2, 8) def...
   - Issue: https://github.com/pytorch/pytorch/issues/72399
   - Fix PR #72734 — [ONNX] Fix lstm reshape shape inference regression
   - PR: https://github.com/pytorch/pytorch/pull/72734
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +    @skipIfUnsupportedMinOpsetVersion(9) +    def test_lstm_sequence(self): +        class LstmNet(torch.nn.Module): +            def __init__(self): +                super().__init__() +            



118. Issue #72693 —  (closed )
   - Issue detail: ### 🚀 The feature, motivation and pitch We have onboarded XLA testing as part of one of the existing Linux workflows. This has created some issues due to diverging test environments, where the same set of tests pass in the downstream, but fails in the upstream due to dependency conflicts and environment setup, etc. This happens because XLA testing was piggybacking on the existing ciflow (config) and image that were mainly built for PyTorch tests. To avoid this and do so unobtrusively, it...
   - Issue: https://github.com/pytorch/pytorch/issues/72693
   - Fix PR #72938 — [release/1.11] Create a CI workflow for XLA tests using the XLA test image
   - PR: https://github.com/pytorch/pytorch/pull/72938
   - Code excerpts:     - .circleci/docker/build.sh: +# Use the same pre-built XLA test image from PyTorch/XLA +if [[ "$image" == *xla* ]]; then +  echo "Using pre-built XLA test image..." +  exit 0 +fi +



119. Issue #64423 —  (closed )
   - Issue detail: ## 🐛 Bug Models containing torch.addcmul operator cannot be exported to opset11 of onnx. When attempted, the following error is produced: ``` RuntimeError: Exporting the operator addcmul to ONNX opset version 11 is not supported. Please feel free to request support or submit a pull request on PyTorch GitHub. ``` ## To Reproduce Steps to reproduce the behavior: 1. run the following code: ```python class Affine(nn.Module): def __init__(self, dim): super().__init__() self.alpha =...
   - Issue: https://github.com/pytorch/pytorch/issues/64423
   - Fix PR #72126 — [ONNX] Add symbolic for torch.addcmul
   - PR: https://github.com/pytorch/pytorch/pull/72126
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +    def test_addcmul(self): +        class AddcmulModel(torch.nn.Module): +            def forward(self, x, t1, t2): +                return torch.addcmul(x, t1, t2), torch.addcmul(x, t1, t2, value=2



120. Issue #72653 —  (closed )
   - Issue detail: ### 🐛 Describe the bug **test.cpp:** ``` #include "torch/script.h" int main() { return 0; } ``` **Building:** (libtorch 1.10.1 Linux, CPU, C++, cxx11 ABI) ``` g++-8 -o test-binary test.cpp -Ilibtorch/include -D_GLIBCXX_USE_CXX11_ABI=1 -Llibtorch/lib -lfbgemm -lasmjit -lnnapi_backend -lcaffe2_observers -lcaffe2_detectron_ops -lbackend_with_compiler -ltorch -ltorch_global_deps -ltorch_cpu -ltorch_python -ltorchbind_test -lXNNPACK -lmkldnn -ljitbackend_test -lcaffe2_module_test_dynamic -lshm...
   - Issue: https://github.com/pytorch/pytorch/issues/72653
   - Fix PR #72959 — Set `BLAS_LIBRARIES` to `${MKL_LIBRARIES}` for MKL case (#72806)
   - PR: https://github.com/pytorch/pytorch/pull/72959
   - Code excerpts:     - cmake/Dependencies.cmake: +    set(BLAS_LIBRARIES ${MKL_LIBRARIES})



121. Issue #42470 —  (closed )
   - Issue detail: ##Bug RuntimeError: Exporting the operator softshrink to ONNX opset version 9 is not supported. I tried to export a simple model having SoftShrink/HardShrink Activation layer but it give the error: ``` Traceback (most recent call last): File "activations.py", line 19, in <module> torch.onnx.export(model, dummy_input, "activation.onnx", opset_version=12) File "/usr/local/lib/python3.6/dist-packages/torch/onnx/__init__.py", line 168, in export custom_opsets, enable_onnx_checker,...
   - Issue: https://github.com/pytorch/pytorch/issues/42470
   - Fix PR #66969 — [ONNX] Add support for shrink ops
   - PR: https://github.com/pytorch/pytorch/pull/66969
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +    def test_tanhshrink(self): +        model = torch.nn.Tanhshrink() + +        x = torch.rand(3, 3).to(dtype=torch.float32) +        self.run_test(model, x) + +    @skipIfUnsupportedMinOpsetVersion



122. Issue #66786 —  (closed )
   - Issue detail: ## 🐛 Bug <!-- A clear and concise description of what the bug is. --> When exporting ONNX format for BERT of Hugging Face implementation, some weight names will become numbers instead of a meaningful name. (but the inference result is correct) E.g., for the [`nn.Linear` in `BertSelfAttention`](https://github.com/huggingface/transformers/blob/4334095c3269d5cd08d9353e67f5f1dec2aae459/src/transformers/models/bert/modeling_bert.py#L239-L241), `bias` can be generated correctly, such as...
   - Issue: https://github.com/pytorch/pytorch/issues/66786
   - Fix PR #68140 — [ONNX] Relax constant_fold gather with indices rank > 1
   - PR: https://github.com/pytorch/pytorch/pull/68140
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +                # torch.nn.Embedding is converted to ONNX::Gather. +                # Constant folding will be triggerred for constant inputs. +                # This pattern is common for constant m



123. Issue #65837 —  (closed )
   - Issue detail: ## 🚀 Feature These are 3 Fusion examples (forward and backward) from Bert to illustrate Fusions that should be supported with Lazy Tensor Cores. I am **only going through the forward examples**, for now. You can find them here: https://github.com/kevinstephano/FusionMicroBenchmarks/tree/main/LazyTensorCore ## Example 1 - Bias+Gelu https://github.com/kevinstephano/FusionMicroBenchmarks/blob/main/LazyTensorCore/bias_gelu.py ``` PYTORCH_JIT_LOG_LEVEL=">>>graph_fuser" LTC_TS_CUDA=1 python...
   - Issue: https://github.com/pytorch/pytorch/issues/65837
   - Fix PR #66192 — [LTC] Code-gen native_layer_norm
   - PR: https://github.com/pytorch/pytorch/pull/66192
   - Code excerpts:     - aten/src/ATen/templates/LazyIr.h: +static lazy_tensors::Shape convertShape(const std::vector<at::ScalarType>& dtypes, +    const std::vector<std::vector<int64_t>>& shapes) +{ +  LTC_CHECK_EQ(dtypes.size(), shapes.size()); +  if (dtype



124. Issue #65853 —  (closed )
   - Issue detail: ## 🐛 Bug torch.onnx.export() fails to export the model that contains customized function. According to the following documentation, the custom operator should be exported as is if operator_export_type is set to ONNX_FALLTHROUGH: [torch doc](https://pytorch.org/docs/stable/onnx.html#onnx-fallthrough) ## To Reproduce Steps to reproduce the behavior: 1. Run the following simplified python code: ``` import torch class MyRelu(torch.autograd.Function): @staticmethod def forward(ctx, input):...
   - Issue: https://github.com/pytorch/pytorch/issues/65853
   - Fix PR #66172 — [ONNX] Relax check on Prim::PythonOp nodes for ONNX_FALLTHROUGH
   - PR: https://github.com/pytorch/pytorch/pull/66172
   - Code excerpts:     - test/onnx/test_utility_funs.py: +    def test_autograd_onnx_fallthrough(self): +        class CustomFunction(torch.autograd.Function): +            @staticmethod +            def forward(ctx, input): +                ctx.save_for_ba



125. Issue #65817 —  (closed )
   - Issue detail: ## 🐛 Bug When I use the torch.all function with the dim parameter I get the following error during the Onnx translation: _all() takes 2 positional arguments but 4 were given ## To Reproduce ``` import torch from torch import nn class TorchAll(nn.Module): def forward(self, tensor): tensor = torch.all(tensor, dim=1) return tensor X = torch.ones((3, 300, 300), dtype=torch.int32) torch.onnx.export( TorchAll(), (X), # Dummy input for shape "torch_all_model.onnx", opset_version=12,...
   - Issue: https://github.com/pytorch/pytorch/issues/65817
   - Fix PR #66093 — [ONNX] Add dim argument to all symbolic
   - PR: https://github.com/pytorch/pytorch/pull/66093
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +        class MDim(torch.nn.Module): +            def forward(self, x): +                return x.any(dim=1) + +        x = torch.rand(3, 4).bool() +        self.run_test(MDim(), (x, )) + +        cl



126. Issue #65221 —  (closed )
   - Issue detail: ## 🐛 Bug I was adding the following line to prevent in-place modification of the data from source DataPipe. https://github.com/pytorch/pytorch/blob/d37c02be08dfc022daf2ee1ddeda2a37b4551cac/torch/utils/data/datapipes/iter/callable.py#L102-L103 But, in fact, this would break when input includes file handle, because file handle can not be serialized. So, in order to support file handle, we need to remove deepcopy. But, for the sake of preventing in-place modification, we need to add...
   - Issue: https://github.com/pytorch/pytorch/issues/65221
   - Fix PR #65924 — [DataPipe] Fix deepcopy for Mapper and in-place modification for IterableWrapper
   - PR: https://github.com/pytorch/pytorch/pull/65924
   - Code excerpts:     - test/test_datapipe.py: +import copy +        numbers_dp = dp.iter.IterableWrapper(source_numbers) +    @suppress_warnings  # Suppress warning for lambda fn +    def test_map_with_col_file_handle_datapipe(self): +        tem



127. Issue #63609 —  (closed )
   - Issue detail: ## 🐛 Bug After #63026 is landed, the generator for Sampler is attached to the instance, which helps to serialize the state of Sampler. But, it brings a problem that it will prevent Sampler's generator being seeded before each epoch. ## To Reproduce Check https://github.com/pytorch/pytorch/pull/63026#issuecomment-902234490 User would expect same result for the sampler without specifying generator input when set seed for each epoch. ```py sampler = RandomSampler(ds) torch.manual_seed(0) l1 =...
   - Issue: https://github.com/pytorch/pytorch/issues/63609
   - Fix PR #65926 — Convert generator attached to Sampler back to lazily construction
   - PR: https://github.com/pytorch/pytorch/pull/65926
   - Code excerpts:     - test/test_dataloader.py: +        for sampler in ( +            RandomSampler(self.dataset, num_samples=5, replacement=True), +            RandomSampler(self.dataset, replacement=False), +            WeightedRandomSampler(wei



128. Issue #59179 —  (closed )
   - Issue detail: ## 🐛 Bug I'm trying to export Mozilla TTS Tacotron2 model into ONNX using TorchScript. Here is my current progress: https://github.com/lasa01/TTS/tree/onnx. Here is the export script: https://github.com/lasa01/TTS/blob/onnx/TTS/bin/convert_tacotron2_torch_to_onnx.py. However, the export fails with the following error: ``` python -m TTS.bin.convert_tacotron2_torch_to_onnx.py --config_path ".\TTS\tts\configs\config.json" --output_path ".\data\converted_models\tts_model.onnx" Warning: ONNX...
   - Issue: https://github.com/pytorch/pytorch/issues/59179
   - Fix PR #60534 — [ONNX] Support tensorList when Infers shape and type uninitialized output
   - PR: https://github.com/pytorch/pytorch/pull/60534
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +    @skipIfUnsupportedMinOpsetVersion(14)  # Need onnx::Identity of sequence in opset 14 +    @skipIfUnsupportedMinOpsetVersion(14)  # Need onnx::Identity of sequence in opset 14 +    # onnx::Identit



129. Issue #64811 —  (closed )
   - Issue detail: ## 🐛 Bug Onnx export of a softplus module with beta!=1 is currently not supported. Are there plans to implement this in the future? ## To Reproduce ```python import torch beta, threshold = 13, 7 x=torch.linspace(-4,6,1000) s=torch.nn.Softplus(beta=beta,threshold=threshold) torch.onnx.export(s,x,'test.onx') ``` fails with ``` UserWarning: ONNX export failed on beta because has to be 1 not supported warnings.warn("ONNX export failed on " + op + " because " + msg + " not supported")...
   - Issue: https://github.com/pytorch/pytorch/issues/64811
   - Fix PR #65001 — [ONNX] Modify softplus symbolic to support beta!=1
   - PR: https://github.com/pytorch/pytorch/pull/65001
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +    def test_softplus(self): +        class BetaOneModel(torch.nn.Module): +            def forward(self, x): +                return torch.nn.functional.softplus(x) + +        x = torch.randn(3, 4, 



130. Issue #60053 —  (closed )
   - Issue detail: Hi, thank you very much for pytorch 1.9! I'm trying to update SpeechBrain (https://github.com/speechbrain/speechbrain) to support pytorch 1.9. Everything seems to work, but I noticed an annoying warning when using nn.MaxPool2d: ``` import torch import torch.nn as nn m = nn.MaxPool2d(3, stride=2) m = nn.MaxPool2d((3, 2), stride=(2, 1)) input = torch.randn(20, 16, 50, 32) output = m(input) ``` ``` UserWarning: Named tensors and all their associated APIs are an experimental feature and subject...
   - Issue: https://github.com/pytorch/pytorch/issues/60053
   - Fix PR #64616 — [Release-1.9] Stop warning on .names() access in max_pool2d and max_pool2d_backward
   - PR: https://github.com/pytorch/pytorch/pull/64616
   - Code excerpts:     - aten/src/ATen/native/DilatedMaxPool2d.cpp: +  DimnameList maybe_names = input.has_names() ? input.names() : DimnameList{}; +    set_output(0, {nInputPlane, outputHeight, outputWidth}, {}, input.options().memory_format(memory_format), maybe_nam



131. Issue #63610 —  (closed )
   - Issue detail: Tests to consider adding are: 1) test_ptltc, C++ unit tests. (CPU is done. GPU is under consideration.) 2) example.py (https://github.com/pytorch/pytorch/blob/lazy_tensor_staging/lazy_tensor_core/example.py). Needed to cover some python scripts. 3) test_ops.py (https://github.com/pytorch/xla/blob/master/test/test_ops.py). Needs to change the device to lazy and run it with the TS backend. 4) other tests in the above folder could be useful too, like training MNIST end to end. This one should be...
   - Issue: https://github.com/pytorch/pytorch/issues/63610
   - Fix PR #65008 — [LTC] Enable CI for building and testing
   - PR: https://github.com/pytorch/pytorch/pull/65008
   - Code excerpts:     - .jenkins/pytorch/build.sh: + +# Test Lazy Tensor Core. Don't merge to master. +# Restrict lazy tensor to cuda environments to limit potential breakages for the feature branch. +if [[ "$BUILD_ENVIRONMENT" == *linux-xenial-cuda11



132. Issue #61345 —  (closed )
   - Issue detail: ## 🐛 Bug I get an error - reigster_buffer in Module - onnxruntime on onnx from torch.onnx.export ## To Reproduce Steps to reproduce the behavior: 1. code example ```python3 import torch # init module class MyModule(torch.nn.Module): def __init__(self): super(MyModule, self).__init__() self.register_buffer("rb", torch.randn(1, 1, 3, 1, 1)) # you can run with the workaround # self.rb = torch.randn(1, 1, 3, 1, 1) def forward(self, x): x += self.rb[0] return x torch_model = MyModule().eval() #...
   - Issue: https://github.com/pytorch/pytorch/issues/61345
   - Fix PR #63588 — [ONNX] Fix gather squeeze axis in constant folding
   - PR: https://github.com/pytorch/pytorch/pull/63588
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +        class GatherModule(torch.nn.Module): +            def __init__(self): +                super(GatherModule, self).__init__() +                self.register_buffer("rb", torch.randn(1, 1, 3, 1,



133. Issue #62431 —  (closed )
   - Issue detail: ## 🚀 Feature Support more ops in LazyTensor to TorchScript lowering ## Motivation Currently Lazy Tensor lowers [a limited set of ops](https://github.com/pytorch/pytorch/blob/lazy_tensor_staging/lazy_tensor_core/ts_native_functions.yaml ) to TorchScript IR. For those are not supported yet, Lazy Tensor will fall back to the Eager execution. From the correctness perspective, this works fine. But various backends optimizers would rely on Lazy Tensor to capture larger IR graph for more aggressive...
   - Issue: https://github.com/pytorch/pytorch/issues/62431
   - Fix PR #63105 — [LTC] Add _log_softmax TorchScript lowering
   - PR: https://github.com/pytorch/pytorch/pull/63105
   - Code excerpts:     - lazy_tensor_core/lazy_tensor_core/csrc/ts_backend/aten_ltc_ts_type.cpp: +at::Tensor LazyNativeFunctions::_log_softmax(const at::Tensor& self, int64_t dim, +                                         bool /* half_to_float */) { +  LTC_FN_COUNTER("lazy::"); +  return bridge::



134. Issue #60179 —  (closed )
   - Issue detail: ## 🐛 Bug When one exports a simple `nn.Module` containing `F.pad` to ONNX, and then runs that ONNX model via onnxruntime, one gets different results. The issue is that the produced .onnx file has the padding dimensions in the wrong order. I have verified that the bug is in `torch.onnx.export` not in onnxruntime. Firstly, I've looked at the .onnx file. Second, I've compared the outputs produced by onnxruntime and [onnx2pytorch](https://github.com/ToriML/onnx2pytorch) -- which both agree with...
   - Issue: https://github.com/pytorch/pytorch/issues/60179
   - Fix PR #64230 — [ONNX] Fix remainder export
   - PR: https://github.com/pytorch/pytorch/pull/64230
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +        x = torch.arange(-2, 4).reshape(2, 3, 1) +        x = torch.arange(-2, 4).reshape(2, 3, 1) +        modules = [TrueDivModule(), TruncDivModule(), FloorDivModule()] +    @skipIfUnsupportedMinO



135. Issue #61332 —  (closed )
   - Issue detail: ## 🐛 Bug When we use LogmelFilterBank from torchlibrosa.stft, we use log10 operator. But log10 operator is not one of supported operators in torch.onnx. Thus, when we convert torch model which contains LogmelFilterBank layer to onnx, we will meet the error. Hope to add log10 operator in supported operators in torch.onnx. cc @BowenBao @neginraoof
   - Issue: https://github.com/pytorch/pytorch/issues/61332
   - Fix PR #63418 — [ONNX] Add log10 symbolic
   - PR: https://github.com/pytorch/pytorch/pull/63418
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +    def test_log10(self): +        class Log10(torch.nn.Module): +            def forward(self, input): +                return torch.log10(input) +        x = torch.rand(2, 3, 4) +        model = Lo



136. Issue #27723 —  (closed )
   - Issue detail: ## 🐛 Bug I run this code on [Colab](https://colab.research.google.com/drive/1zRUeHSid0PEbZULODFowxOqxc5R6dvja) Running torch.onnx.export gives this error. > /content/DeOldify/deoldify/unet.py:56: TracerWarning: Converting a tensor to a Python boolean might cause the trace to be incorrect. We can't record the data flow of Python values, so this value will be treated as a constant in the future. This means that the trace might not generalize to other inputs! > if ssh != up_out.shape[-2:]: >...
   - Issue: https://github.com/pytorch/pytorch/issues/27723
   - Fix PR #62596 — [ONNX] Suppport torch.dot and torch.nn.utils.spectral_norm
   - PR: https://github.com/pytorch/pytorch/pull/62596
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +    @skipIfUnsupportedMinOpsetVersion(9)  # MatMul long inputs is added in ONNX opset 9. +    def test_dot(self): +        class MatmulModel(torch.nn.Module): +            def forward(self, input, ot



137. Issue #58733 —  (closed )
   - Issue detail: I download the source code of v1.9.0-rc1 and using "python setup.py install" to install this version. I want to export onnx format of my model which contain op "repeat_interleave" **I tried "torch.onnx.export(model, ....)", get following error:** File "/data/xxxx/software/anaconda3/lib/python3.6/site-packages/torch/onnx/__init__.py", line 313, in _run_symbolic_function return utils._run_symbolic_function(*args, **kwargs) File "/data/xxxx/software/anaconda3/lib/python3.6/site-...
   - Issue: https://github.com/pytorch/pytorch/issues/58733
   - Fix PR #59979 — [ONNX] Update repeat_interleave for dynamic repeats
   - PR: https://github.com/pytorch/pytorch/pull/59979
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +    @skipIfUnsupportedMinOpsetVersion(13) +        class SingleDynamicModelFloat(torch.nn.Module): +        x = torch.tensor([[1.1, 2.1], [3.1, 4.1]]) +        another_x = torch.tensor([[7.1, 8.1], [



138. Issue #60741 —  (closed )
   - Issue detail: ## Bug Running `tools/linter/clang_tidy.py` with the `--dry-run` option doesn't print anything. ## To Reproduce Run the following command ``` python3 tools/linter/clang_tidy.py --paths torch/csrc/fx --dry-run ``` Output: ``` ``` Expected Output: ``` clang-tidy -p build -config '{"InheritParentConfig": true, "Checks": " bugprone-*, -bugprone-forward-declaration-namespace, -bugprone-macro-parentheses, -bugprone-lambda-function-name, -bugprone-reserved-identifier, cppcoreguidelines-*,...
   - Issue: https://github.com/pytorch/pytorch/issues/60741
   - Fix PR #60743 — Fix --dry-run option in tools/linter/clang_tidy.py
   - PR: https://github.com/pytorch/pytorch/pull/60743
   - Code excerpts:     - tools/linter/clang_tidy.py: +    if options.dry_run: +        print(clang_tidy_output)



139. Issue #50153 —  (closed )
   - Issue detail: ## 🐛 Bug libtorch_cuda.so is missing fast kernels from libcudnn_static.a, therefore statically linked cuDNN could be much slower than dynamically linked. People at NVIDIA found that the following code is much slower on backward when running with statically linked cuDNN compared to dynamically linked one: ```python import torch from torch import nn import time import pandas as pd n_trials = 100 warmup_iters = 100 torch.backends.cudnn.benchmark = False convs = [ # === Input dimensions === ===...
   - Issue: https://github.com/pytorch/pytorch/issues/50153
   - Fix PR #59873 — [Release/1.9] Link whole CuDNN for CUDA-11.1
   - PR: https://github.com/pytorch/pytorch/pull/59873
   - Code excerpts:     - .circleci/scripts/binary_populate_env.sh: +USE_WHOLE_CUDNN="OFF" +# Link whole cuDNN for CUDA-11.1 to include fp16 fast kernels +if [[  "$(uname)" == "Linux" && "${DESIRED_CUDA}" == "cu111" ]]; then +  USE_WHOLE_CUDNN="ON" +fi + +export USE_G



140. Issue #53730 —  (closed )
   - Issue detail: ## 🐛 Bug hey, in `torch version 1.7.0`, I was successfully able to export the T5 decoder to onnx. as shown below. ```python _ = torch.onnx.export(decoder_with_lm_head_init, (input_ids_dec, attention_mask, enc_out), f"{output_prefix}-decoder-with-lm-head_initial.onnx", export_params=True, opset_version=12, input_names=['input_ids', 'encoder_attention_mask', 'encoder_hidden_states'], output_names=['logits', 'past_key_values'], dynamic_axes={ 'input_ids': {0:'batch', 1: 'sequence'}, #...
   - Issue: https://github.com/pytorch/pytorch/issues/53730
   - Fix PR #54019 — [1.8.1][ONNX] Update assign output shape for nested structure and dict output
   - PR: https://github.com/pytorch/pytorch/pull/54019
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +    @disableScriptTest() +    def test_dict_output(self): +        class DictModelOutput(OrderedDict): +            tensor_out: torch.Tensor +            tuple_out: Optional[Tuple[torch.Tensor]] = No



141. Issue #54051 —  (closed )
   - Issue detail: Hi, I have updated the PytorchMobile for my Android application from 1.7.1 to 1.8.0 but doing so caused an error in the inference phase. Somehow the tensor dimensions became not valid anymore for PixelShuffle layer. Here is the error: ``` Process: com.example.pytorchtutorial, PID: 14078 java.lang.RuntimeException: The following operation failed in the TorchScript interpreter. Traceback of TorchScript, serialized code (most recent call last): File...
   - Issue: https://github.com/pytorch/pytorch/issues/54051
   - Fix PR #54178 — [fix] Dimension out of range in pixel_shuffle / pixel_unshuffle
   - PR: https://github.com/pytorch/pytorch/pull/54178
   - Code excerpts:     - aten/src/ATen/native/PixelShuffle.cpp: +  std::iota(permutation.begin(), permutation.end(), 0); +  std::iota(permutation.begin(), permutation.end(), 0);



142. Issue #53507 —  (closed )
   - Issue detail: ## 🐛 Bug This is a sibling issue for https://github.com/microsoft/onnxruntime/issues/6910 as they suggested to report here too. It seems that Tensor indexing is not fully supported once exported to ONNX: ## To Reproduce ```py import io import torch from torch import Tensor import onnxruntime def f() -> Tensor: mask = torch.zeros(100, dtype=torch.bool) indices = (torch.rand(25) * mask.shape[0]).to(torch.int64) mask[indices] = True # offending line return mask class Module(torch.nn.Module): def...
   - Issue: https://github.com/pytorch/pytorch/issues/53507
   - Fix PR #53690 — [ONNX] Improve index_put symbolic to handle singular Bool updates
   - PR: https://github.com/pytorch/pytorch/pull/53690
   - Code excerpts:     - test/onnx/test_pytorch_onnx_onnxruntime.py: +    @skipIfUnsupportedMinOpsetVersion(11) +    def test_index_put_singular(self): +        class IndexPutBoolModel(torch.nn.Module): +            def forward(self, mask, indices): +                ma



143. Issue #54245 —  (closed )
   - Issue detail: ## 🐛 Bug ## To Reproduce runing test.py: ```python import torch from torchvision.models.detection import fasterrcnn_resnet50_fpn def main(): # get devices device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu") print("using {} device.".format(device)) init_img = torch.zeros((1, 3, 512, 512), device=device) target = [{"boxes": torch.as_tensor([[1, 2, 3, 4]], device=device), "labels": torch.as_tensor([1], device=device)}] model = fasterrcnn_resnet50_fpn(pretrained=False,...
   - Issue: https://github.com/pytorch/pytorch/issues/54245
   - Fix PR #54537 — [1.8.1] Replace thrust with cub in randperm
   - PR: https://github.com/pytorch/pytorch/pull/54537
   - Code excerpts:     - aten/src/ATen/native/cuda/TensorFactories.cu: +#include <cub/cub.cuh> +#include <limits> +      TORCH_CHECK(n <= std::numeric_limits<int>::max(), +        "randperm of tensors larger than INT_MAX is not supported yet in pytorch"); + +      auto r



144. Issue #45860 —  (closed )
   - Issue detail: ## 🐛 Bug Segfault on master (built Oct 4) with the following code (which is perhaps not expected to be scriptable): ```python from typing import Any import torch class A: def __init__(self, t): self.t = t @staticmethod def f(a: torch.Tensor): return A(a + 1) class B(A): def __init__(self, t): self.t = t + 10 @staticmethod def f(a: torch.Tensor): return A(a + 1) x = A(torch.tensor([3])) def fun(x: Any): if isinstance(x, A): return A.f(x.t) else: return B.f(x.t) print(torch.__version__) sc =...
   - Issue: https://github.com/pytorch/pytorch/issues/45860
   - Fix PR #46422 — [v1.7][JIT] Improve class type annotation inference
   - PR: https://github.com/pytorch/pytorch/pull/46422
   - Code excerpts:     - test/jit/test_class_type.py: +from typing import Any + +    def test_class_inheritance_implicit(self): +        """ +        Test that inheritance is detected in +        implicit scripting codepaths (e.g. try_ann_to_type). +    



145. Issue #41047 —  (closed )
   - Issue detail: ## 🐛 Bug When the output tensor is permuted (by `permute()`), many operators don't produce correct results. ## To Reproduce Use `floor` as an example. ``` In [1]: import torch In [2]: a=torch.arange(0, 300000*3*3, dtype=float) In [3]: res = torch.rand(3, 3, 300000).permute(2, 0, 1) In [4]: a Out[4]: tensor([0.0000e+00, 1.0000e+00, 2.0000e+00, ..., 2.7000e+06, 2.7000e+06, 2.7000e+06], dtype=torch.float64) In [5]: a.floor() Out[5]: tensor([0.0000e+00, 1.0000e+00, 2.0000e+00, ..., 2.7000e+06,...
   - Issue: https://github.com/pytorch/pytorch/issues/41047
   - Fix PR #41160 — 1.6 Port: Disables unary op casting to output dtype
   - PR: https://github.com/pytorch/pytorch/pull/41160
   - Code excerpts:     - aten/src/ATen/native/TensorIterator.cpp: +    .cast_common_dtype_to_outputs(false) +    .enforce_safe_casting_to_output(false) +    .check_all_same_dtype(true)



146. Issue #38034 —  (closed )
   - Issue detail: ## 🐛 Bug Torch.jit.trace fails if model slicing is used anywhere within the model functions. Steps to reproduce the behavior: Say you have VGG16 model like below - ```python3 class VGG16_frontend(nn.Module): def __init__(self,block_num=5,decode_num=0,load_weights=True,bn=False,IF_freeze_bn=False): super(VGG16_frontend,self).__init__() self.block_num = block_num self.load_weights = load_weights self.bn = bn self.IF_freeze_bn = IF_freeze_bn self.decode_num = decode_num block_dict = [[64, 64,...
   - Issue: https://github.com/pytorch/pytorch/issues/38034
   - Fix PR #40538 — Allow slicing sequential container
   - PR: https://github.com/pytorch/pytorch/pull/40538
   - Code excerpts:     - test/test_jit.py: +    def test_script_sequential_sliced_iteration(self): +        class seq_mod(nn.Module): +            def __init__(self): +                super(seq_mod, self).__init__() +                self.layer



147. Issue #38439 —  (closed )
   - Issue detail: In early versions of RPC, all threads on server side are block-waiting until the request is fully processed. Hence we use a guard to clear the `thread_local` autograd context. https://github.com/pytorch/pytorch/blob/3d0279862db2602d684ec246e18424c405582f5d/torch/csrc/distributed/rpc/request_callback_impl.cpp#L563-L564 However, since we gradually making the RPC non-blocking on server side, the above guard is no longer correct. For example, in `FORWARD_AUTOGRAD_REQ`, the bottom half of the...
   - Issue: https://github.com/pytorch/pytorch/issues/38439
   - Fix PR #39109 — [v1.5.1 patch] Restore thread_local states in continuation thread on RPC servers
   - PR: https://github.com/pytorch/pytorch/pull/39109
   - Code excerpts:     - torch/csrc/distributed/autograd/context/container.cpp: +void DistAutogradContainer::forceCurrentContextId(int64_t contextId) { +  current_context_id_ = contextId; +} + +int64_t DistAutogradContainer::currentContextId() { +  return current_context_id_; +} 



148. Issue #31468 —  (closed )
   - Issue detail: ## 🐛 Bug when I run https://pytorch.org/tutorials/advanced/dynamic_quantization_tutorial.html can't get DynamicQuantizedLSTM weight , bias , scale, zero_point ``` >>print(quantized_model.rnn.state_dict()) OrderedDict() >>print(quantized_model.state_dict()) OrderedDict([('encoder.weight', tensor([[-0.2349, 0.4934, -0.3151, ..., 0.4456, 0.4912, 0.1553], [-0.0710, 0.5101, -0.2940, ..., 0.1747, 0.5764, 0.3247], [-0.0229, 0.0302, 0.0874, ..., 0.0390, 0.0736, -0.0558], ..., [-0.0049, -0.0769,...
   - Issue: https://github.com/pytorch/pytorch/issues/31468
   - Fix PR #36286 — [v1.5.0] repr and _*state_dict for qRNN (#31540)
   - PR: https://github.com/pytorch/pytorch/pull/36286
   - Code excerpts:     - torch/nn/quantized/dynamic/modules/rnn.py: +from collections import OrderedDict +import numbers + +    def _save_to_state_dict(self, destination, prefix, keep_vars): +        super(PackedParameter, self)._save_to_state_dict(destination, prefix



149. Issue #35014 —  (closed )
   - Issue detail: ## 🐛 Bug When concatenating tensors of different dtypes, the result is unexpected (and often incorrect). This could be fixed by using type promotion. ## To Reproduce ```python >>> xt = torch.ones((2, 1, 3), dtype=torch.int8) >>> yt = torch.ones((2, 1, 3), dtype=torch.int32) >>> torch.cat([xt, yt]) tensor([[[1, 1, 1]], [[1, 1, 1]], [[1, 0, 0]], [[0, 1, 0]]], dtype=torch.int8) >>> torch.cat([yt, xt]) tensor([[[ 1, 1, 1]], [[ 1, 1, 1]], [[ 16843009, 257, 180739632]], [[ 1, 10605347,...
   - Issue: https://github.com/pytorch/pytorch/issues/35014
   - Fix PR #35477 — [v1.5.0] Making sure all tensors in `torch.cat` sequence have the same dtype. …
   - PR: https://github.com/pytorch/pytorch/pull/35477
   - Code excerpts:     - aten/src/ATen/native/TensorShape.cpp: +  // Dtypes should be the same +  const auto first_in_cat = tensors[0]; +  for (int64_t i = 1; i < tensors.size(); i++) { +    TORCH_CHECK(first_in_cat.dtype() == tensors[i].dtype(), +              "



150. Issue #35213 —  (closed )
   - Issue detail: ## 🐛 Bug Type checking any code adding a float or integer to a tensor (`__radd__` method) results in a type checking error when using nightly build (but not in release). This is causing type checking failures for downstream applications, particularly in Captum. ## To Reproduce Run mypy on any code applying radd, such as: ``` import torch ten = torch.tensor([1.0, 2.0, 3.0]) print(7 + ten) ``` Mypy Error: `test_file.py:4: error: Unsupported operand types for + ("int" and "Tensor") ` ## Expected...
   - Issue: https://github.com/pytorch/pytorch/issues/35213
   - Fix PR #35405 — [1.5.0] Fix Tensor __radd__ type hint issue (#35231)
   - PR: https://github.com/pytorch/pytorch/pull/35405
   - Code excerpts:     - tools/pyi/gen_pyi.py: +              'matmul', 'floordiv', 'floor_divide',



151. Issue #5041 —  (closed )
   - Issue detail: - PyTorch version: 0.3.0 - Python version: 3.5 - GPU models and configuration: 8x NVIDIA Titan I found that requires_grad setting in module is ignored when module is wrapped with nn.DataParallel. For example, ```python import torch from torch.nn import DataParallel from torchvision.models.resnet import resnet50 module_ = resnet50() for name, param in module_.named_parameters(): if name.startswith('conv1') or name.startswith('bn1'): param.requires_grad = False if name.startswith('layer1') or...
   - Issue: https://github.com/pytorch/pytorch/issues/5041
   - Fix PR #5061 — Broadcast output requires_grad only if corresponding input requires_grad
   - PR: https://github.com/pytorch/pytorch/pull/5061
   - Code excerpts:     - test/common.py: +        elif isinstance(x, bool) and isinstance(y, bool): +            super(TestCase, self).assertEqual(x, y, message)



152. Issue #7956 —  (closed )
   - Issue detail: Seems like `torch/nn/parallel/scatter_gather.py > Gather.apply(...)` is broken by dim=0 outputs. ``` python >>> import torch >>> torch.__version__ '0.4.0' >>> class Foo(torch.nn.Module): ... def forward(self, x): ... return x.mean() # this gives a scalar output ... # return x.mean().view(1) # this is a quick fix ... >>> foo = torch.nn.DataParallel(Foo(),[0,1]).cuda() >>> x = torch.zeros(2,2) >>> foo(x) ``` ``` Traceback (most recent call last): File "<input>", line 1, in <module> File...
   - Issue: https://github.com/pytorch/pytorch/issues/7956
   - Fix PR #7973 — Support modules that output scalar in Gather (and data parallel)
   - PR: https://github.com/pytorch/pytorch/pull/7973
   - Code excerpts:     - test/test_nn.py: +            torch.randn(2, 4, device='cuda:0', requires_grad=True), +            torch.randn(2, 4, device='cuda:1', requires_grad=True), +        # test scalar inputs, should stack into a vector in t



153. Issue #28515 —  (closed )
   - Issue detail: I finally have a good reason to merge libc10.so into libtorch.so (and corresponding libc10_cuda.so into libtorch_cuda.so, etc.): I am trying to devirtualize access to AutogradMeta, but because TensorImpl lives in c10 and AutogradMeta lives in torch, I cannot do this as the destructor would have to cross a dynamic library boundary. By absorbing c10 into torch I will be able to do this. Some dangers: putting c10 into libtorch might push Windows build over max library size. See...
   - Issue: https://github.com/pytorch/pytorch/issues/28515
   - Fix PR #28525 — Merge libc10{,_cuda,_hip}.so libraries into libtorch.so
   - PR: https://github.com/pytorch/pytorch/pull/28525
   - Code excerpts:     - .circleci/scripts/binary_ios_upload.sh: +target_libs=(libclog.a libcpuinfo.a libeigen_blas.a libpytorch_qnnpack.a libtorch.a)



154. Issue #3851 —  (closed )
   - Issue detail: I run RNN sucessfully with the code. ``` rnn = nn.RNN(features, hidden_size, num_layers) o, hidden = rnn(x, hidden) ``` and I run embedding example. Then, got RuntimeError. ``` RuntimeError: inconsistent tensor size, expected r_ [5 x 25], t [5 x 25] and src [2 x 25] to have thesame number of elements, but got 125, 125 and 50 elements respectively at /opt/conda/conda-bld/pytorch_1503970438496/work/torch/lib/TH/generic/THTensorMath.c:887 ``` I set `batch_first=True` to use `Embedding` ```...
   - Issue: https://github.com/pytorch/pytorch/issues/3851
   - Fix PR #3925 — Add rnn args check
   - PR: https://github.com/pytorch/pytorch/pull/3925
   - Code excerpts:     - test/test_nn.py: +    def test_rnn_args_check(self): +        input_size = 3 +        hidden_size = 5 +        num_layers = 2 +        batch_size = 4 +        seq_len = 6 +        num_directions = 1 + +        def tes



155. Issue #2517 —  (closed )
   - Issue detail: **Summary by @ezyang.** If you are using multiprocessing code, and are in Python 3, you can work around this problem by adding `mp.set_start_method('spawn')` to your script. Otherwise, to work around, you need to make sure there are no CUDA calls prior to starting your subprocesses; `torch.cuda.is_available()` and `torch.manual_seed` both count as a CUDA calls in PyTorch 0.2.0. ---- Run <https://github.com/ikostrikov/pytorch-a3c> using pytorch 0.2.0, python 2.7 with error ``` terminate called...
   - Issue: https://github.com/pytorch/pytorch/issues/2517
   - Fix PR #2811 — Lazier CUDA initialization
   - PR: https://github.com/pytorch/pytorch/pull/2811
   - Code excerpts:     - torch/__init__.py: +    if not torch.cuda._in_bad_fork:



156. Issue #8485 —  (closed )
   - Issue detail: Dear community, i encountered a build error i can not resolve. I'm trying to build pytorch with the specs below. The error i'm encountering is this one: ![img](https://s1.imagebanana.com/file/180614/bqRUhDP0.PNG) ## Issue description Obviously it's lacking a dubious lib.obj for linking. The question is why it is searching for it in the standard Nvidea folder. Shouldn't the files compiled not be safed somewhere else. Furthermore there is no other error before this one in the build process. Can...
   - Issue: https://github.com/pytorch/pytorch/issues/8485
   - Fix PR #8743 — Minor fixes for finding CUDNN
   - PR: https://github.com/pytorch/pytorch/pull/8743
   - Code excerpts:     - tools/setup_helpers/cudnn.py: +from .env import IS_WINDOWS, IS_CONDA, CONDA_DIR, check_negative_env_flag, gather_paths, lib_paths_from_base +        os.getenv('CUDNN_LIB_DIR') +    ] + lib_paths_from_base(CUDA_HOME) + [ +    # Add



157. Issue #5671 —  (closed )
   - Issue detail: I've tested a few other norms as well: ``` x = torch.randn(1024, 256) y = torch.randn(1024, 256) In [12]: %timeit torch.norm(x-y, 1, 1) 2.55 ms ± 253 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) In [13]: %timeit (x-y).sum(1) 339 µs ± 699 ns per loop (mean ± std. dev. of 7 runs, 1000 loops each) In [14]: %timeit torch.norm(x-y, 2, 1) 2.42 ms ± 33.7 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) In [15]: %timeit torch.sqrt((x-y).pow(2).sum(1)) 736 µs ± 2.3 µs per loop...
   - Issue: https://github.com/pytorch/pytorch/issues/5671
   - Fix PR #5722 — Add optimization to norm for common norms
   - PR: https://github.com/pytorch/pytorch/pull/5722
   - Code excerpts:     - aten/src/TH/generic/THTensorMath.c: +  #define DIM_REDUCE(reduce, transform) \ +    TH_TENSOR_DIM_APPLY2(real, t, real, r_, dimension,      \ +                         accreal sum = 0;                   \ +                         int64



158. Issue #773 —  (closed )
   - Issue detail: They sometimes give NaNs or infs.
   - Issue: https://github.com/pytorch/pytorch/issues/773
   - Fix PR #1026 — Fixes for Prod and Expand functions
   - PR: https://github.com/pytorch/pytorch/pull/1026
   - Code excerpts:     - test/test_autograd.py: +def prod_zeros(dim_size): +    result = torch.randn(dim_size, dim_size, dim_size) +    result[0, 1] = 0 +    result[2, 3] = 0 +    result[4, 3] = 0 +    return Variable(result, requires_grad=True) + 



159. Issue #2009 —  (closed )
   - Issue detail: Torchvision is considered a basic requirement of the tutorials. Perhaps it makes sense to include it in the docker build. ``` # python Python 3.5.2 |Continuum Analytics, Inc.| (default, Jul 2 2016, 17:53:06) [GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux Type "help", "copyright", "credits" or "license" for more information. >>> import torchvision Traceback (most recent call last): File "<stdin>", line 1, in <module> ImportError: No module named 'torchvision' ```
   - Issue: https://github.com/pytorch/pytorch/issues/2009
   - Fix PR #2090 — install vision in devel dockerfile, minor fixes to dockerfile
   - PR: https://github.com/pytorch/pytorch/pull/2090
   - Code excerpts:     - Dockerfile: +FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04  +         vim \ +         libpng-dev &&\ +RUN git clone https://github.com/pytorch/vision.git && cd vision && pip install -v . +



160. Issue #1482 —  (closed )
   - Issue detail: b = Variable(torch.zeros(1)) if b[0]: print 'true' else: print 'false' above code outputs 'true', is this a bug?
   - Issue: https://github.com/pytorch/pytorch/issues/1482
   - Fix PR #1491 — Raise error when Variable is converted to bool. Fixes #1482.
   - PR: https://github.com/pytorch/pytorch/pull/1491
   - Code excerpts:     - test/common.py: +    def unwrapVariables(self, x, y): +        if isinstance(x, Variable) and isinstance(y, Variable): +            return x.data, y.data +        elif isinstance(x, Variable) or isinstance(y, Variabl



161. Issue #5062 —  (closed )
   - Issue detail: Hi, I would like to sample from a categorical distribution where the probabilities passed are the columns of a tensor p_dG: ``` G = 3 D = 2 p_dG = torch.Tensor(G, D) p_dG[:, 0] = torch.Tensor([0.1, 0.8, 0.1]) p_dG[:, 1] = torch.Tensor([0.1, 0.8, 0.1]) z_list = [] p_dg = p_dG[:, 0] print(p_dg) dis_Z = dis.Categorical(p_dg) for _ in range(250): z = dis_Z.sample() z_list.append(z) z = torch.cat(z_list, dim=0) true_z_np = z.numpy() v, c = np.unique(true_z_np, return_counts=True) print(v) print(c)...
   - Issue: https://github.com/pytorch/pytorch/issues/5062
   - Fix PR #5093 — Fix CPU torch.multinomial with noncontiguous prob tensor
   - PR: https://github.com/pytorch/pytorch/pull/5093
   - Code excerpts:     - aten/src/TH/generic/THStorage.c: +        storage->data = NULL; +        storage->data = storage->allocator->malloc( +            storage->allocatorContext, +            sizeof(real)*size); +        ptrdiff_t copy_size = old_size; + 



162. Issue #7213 —  (closed )
   - Issue detail: Suggested in #7175. Creating new issue to track.
   - Issue: https://github.com/pytorch/pytorch/issues/7213
   - Fix PR #7632 — Improve number formatting in tensor print
   - PR: https://github.com/pytorch/pytorch/pull/7632
   - Code excerpts:     - test/expect/TestTorch.test_print-bigint.expect: +tensor(2341234123412341)



163. Issue #7518 —  (closed )
   - Issue detail: <img width="655" alt="screen shot 2018-05-11 at 10 53 52 pm" src="https://user-images.githubusercontent.com/123560/39952895-5ba78ba0-556e-11e8-8f62-133485adf465.png">
   - Issue: https://github.com/pytorch/pytorch/issues/7518
   - Fix PR #7537 — Documentation improvements
   - PR: https://github.com/pytorch/pytorch/pull/7537
   - Code excerpts:     - docs/source/nn.rst: +:hidden:`GroupNorm` +~~~~~~~~~~~~~~~~~~~ +~~~~~~~~~~~~~~~~~~~~~~~ +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



164. Issue #789 —  (closed )
   - Issue: https://github.com/pytorch/pytorch/issues/789
   - Fix PR #873 — Add support for variable length sequences in RNNs
   - PR: https://github.com/pytorch/pytorch/pull/873
   - Code excerpts:     - docs/source/nn.rst: +.. currentmodule:: torch.nn.utils.rnn + +:hidden:`PackedSequence` +~~~~~~~~~~~~~~~~~~~~~~~~ + +.. autofunction:: torch.nn.utils.rnn.PackedSequence + + +:hidden:`pack_padded_sequence` +~~~~~~~~~~~~~~~



165. Issue #5801 —  (closed )
   - Issue detail: Pytorch Version: '0.3.0' Code: ``` import torch import torch.nn as nn from torch.autograd import Variable import sys batchsize = 8 nclass = 5 if sys.argv[1] == "cuda": cuda = True else: cuda = False print("Cuda: " + str(cuda)) def make_prob(): if cuda: pr = torch.cuda.FloatTensor(batchsize, nclass) else: pr = torch.FloatTensor(batchsize, nclass) pr.uniform_() pr /= pr.sum(dim=1).view(batchsize, 1) return pr def loss_kl(pi, targets): pi_var = Variable(pi, requires_grad=True) logsoftmax =...
   - Issue: https://github.com/pytorch/pytorch/issues/5801
   - Fix PR #5814 — Fix kldiv backward on CUDA
   - PR: https://github.com/pytorch/pytorch/pull/5814
   - Code excerpts:     - aten/src/THCUNN/DistKLDivCriterion.cu: +      return y > 0 ? norm * (-y) * gradOutput : ScalarConvert<int, Dtype>::to(0);



166. Issue #4348 —  (closed )
   - Issue detail: For `torch.nn.InstanceNorm1d` the docs say: *At evaluation time (.eval()), the default behaviour of the InstanceNorm module stays the same i.e. running mean/variance is NOT used for normalization. One can force using stored mean and variance with .train(False) method.* However, the source for `.eval()` shows that it simply calls `.train(False)`.
   - Issue: https://github.com/pytorch/pytorch/issues/4348
   - Fix PR #4444 — Fix setting using running stats in InstanceNorm*d
   - PR: https://github.com/pytorch/pytorch/pull/4444
   - Code excerpts:     - torch/nn/modules/instancenorm.py: +        self.use_running_stats = False +            not self.use_running_stats, self.momentum, self.eps) +    def use_running_stats(self, mode=True): +        r"""Set using running statistics or inst



167. Issue #306 —  (closed )
   - Issue detail: If you try to restrict torch to not see any CUDA devices it will still find it and break on the first call `with no CUDA-capable device is detected`. ``` zagoruys@rio:~$ CUDA_VISIBLE_DEVICES= ipython In [1]: import torch.cuda In [2]: torch.cuda.is_available() Out[2]: True In [3]: if torch.cuda.is_available(): ...: x = torch.cuda.FloatTensor() ...: THCudaCheck FAIL file=/home/zagoruys/rocks/pytorch/torch/lib/THC/THCGeneral.c line=62 error=38 : no CUDA-capable device is detected terminate...
   - Issue: https://github.com/pytorch/pytorch/issues/306
   - Fix PR #290 — Allow returning changed gradients from the hooks
   - PR: https://github.com/pytorch/pytorch/pull/290
   - Code excerpts:     - docs/tensor.md: + 0 + 0 + 0 + 0 + 0 + 0 + 0 +[torch.FloatTensor of dimension 5] +>>> # same thing can be achieved with slice indexing +>>> x[1:3] = 2 +>>> print(x) + 0 + 2 + 2 + 0 +the tensor and is of type `torch.Si



168. Issue #4353 —  (closed )
   - Issue detail: Right now it seeds only if you call `_set_rng_seed` which means it's easy to forget to call it, leading to a nondeterministic test. Instead, we should modify `setUp` in `common.py` and have it seed Numpy as well as Torch: ``` class TestCase(unittest.TestCase): precision = 1e-5 maxDiff = None def setUp(self): torch.manual_seed(SEED) ``` CC @fritzo
   - Issue: https://github.com/pytorch/pytorch/issues/4353
   - Fix PR #4357 — Implement OneHotCategorical distribution
   - PR: https://github.com/pytorch/pytorch/pull/4357
   - Code excerpts:     - docs/source/distributions.rst: + +:hidden:`OneHotCategorical` +~~~~~~~~~~~~~~~~~~~~~~~~~~~ + +.. autoclass:: OneHotCategorical +    :members: + +:hidden:`Uniform` +~~~~~~~~~~~~~~~~~~~~~~~ + +.. autoclass:: Uniform +    :members:



169. Issue #4299 —  (closed )
   - Issue detail: Reported here: https://discuss.pytorch.org/t/torch-diag-of-a-non-square-matrix-backward-error/11426 MWE: (tested on master) ``` import torch aa = torch.nn.functional.log_softmax(torch.autograd.Variable(torch.randn(4, 3), requires_grad=1), 1) b = torch.diag(aa, 1) c = torch.sum(b) c.backward() >>>Traceback (most recent call last): File "<stdin>", line 1, in <module> File "/home/rzou/pytorch/torch/autograd/variable.py", line 110, in backward torch.autograd.backward(self, gradient, retain_graph,...
   - Issue: https://github.com/pytorch/pytorch/issues/4299
   - Fix PR #4538 — Fix torch.diag backward with non-square matrix
   - PR: https://github.com/pytorch/pytorch/pull/4538
   - Code excerpts:     - test/test_autograd.py: +    ('diag', (3, 5), NO_ARGS, '2d_wide'), +    ('diag', (3, 5), (2,), '2d_wide_pos'), +    ('diag', (3, 5), (-2,), '2d_wide_neg'), +    ('diag', (5, 3), NO_ARGS, '2d_tall'), +    ('diag', (5, 3), (2,



170. Issue #4974 —  (closed )
   - Issue detail: The `torch.sum()` function writes its outputs in erroneous locations when the out `kwarg` is used. Repro: ```python import torch i = 1 a = torch.zeros(5, 3) b = torch.randn(3, 5) ac = a.clone() ac[:, i].copy_(b.sum(0)) print(ac) ac = a.clone() b.sum(0, out=ac[:, i]) print(ac) ``` Output: ```bash lvdmaaten-mbp:Desktop lvdmaaten$ python bug.py 0.0000 -0.1515 0.0000 0.0000 1.8761 0.0000 0.0000 -1.7563 0.0000 0.0000 0.5194 0.0000 0.0000 1.5322 0.0000 [torch.FloatTensor of size 5x3] 0.0000 -0.1515...
   - Issue: https://github.com/pytorch/pytorch/issues/4974
   - Fix PR #4995 — Fix reduction functions to respect the stride of the output
   - PR: https://github.com/pytorch/pytorch/pull/4995
   - Code excerpts:     - aten/src/TH/generic/THTensorMath.c: + +// Helper function to be used in a reduction operation. +// Due to resize semantics of outputs, if the specified output tensor r_ has +// same size as the output of the reduction operation, then an



171. Issue #2790 —  (closed )
   - Issue detail: failure case: ``` import torch x = torch.zeros(300, 100001).cuda(); u, s, v = torch.svd(x, some=True); print(u); ``` Context: https://discuss.pytorch.org/t/segmentation-fault-for-svd-implementation-in-gpu-for-large-matrices/7557/4
   - Issue: https://github.com/pytorch/pytorch/issues/2790
   - Fix PR #3470 — Fix overflow when using magma
   - PR: https://github.com/pytorch/pytorch/pull/3470
   - Code excerpts:     - aten/src/THC/generic/THCTensorMathMagma.cu: +  int64_t n = a_->size[0]; +  int64_t nrhs = b_->size[1]; +  int64_t m = a->size[0]; +  int64_t n = a->size[1]; +  int64_t nrhs = b->size[1]; +  int64_t n = a->size[0]; +  int64_t lda = n; +  int64_t



172. Issue #8484 —  (closed )
   - Issue detail: `rrelu` is affected by this and (probably) gives incorrect behavior (I have not verified this) ``` func: rrelu(Tensor self, Scalar lower=0.125, Scalar upper=0.3333333333333333, bool training=false, Generator* generator=nullptr) -> Tensor variants: function func: rrelu_(Tensor self, Scalar lower=0.125, Scalar upper=0.3333333333333333, bool training=false, Generator* generator=nullptr) -> Tensor variants: function ``` I gdb'ed into `rrelu` and printed out "lower": ``` (gdb) p upper $1 = {tag =...
   - Issue: https://github.com/pytorch/pytorch/issues/8484
   - Fix PR #8681 — Fix parsing of floating point defaults in python_arg_parser
   - PR: https://github.com/pytorch/pytorch/pull/8681
   - Code excerpts:     - torch/csrc/utils/python_arg_parser.cpp: +      default_scalar = as_integer.has_value() ? at::Scalar(as_integer.value()) : +                                                at::Scalar(atof(str.c_str()));



173. Issue #6090 —  (closed )
   - Issue detail: Cannot find the docs on website
   - Issue: https://github.com/pytorch/pytorch/issues/6090
   - Fix PR #8166 — Docs for gradcheck and gradgradcheck; expose gradgradcheck
   - PR: https://github.com/pytorch/pytorch/pull/8166
   - Code excerpts:     - docs/source/autograd.rst: +.. _grad-check: + +Numerical gradient checking +^^^^^^^^^^^^^^^^^^^^^^^^^^^ + +.. autofunction:: gradcheck + +.. autofunction:: gradgradcheck +



174. Issue #7805 —  (closed )
   - Issue detail: https://github.com/pytorch/pytorch/blob/master/aten/src/THCUNN/generic/SpatialDepthwiseConvolution.cu#L59
   - Issue: https://github.com/pytorch/pytorch/issues/7805
   - Fix PR #7952 — Fix THCUNN SpatialDepthwiseConvolution assuming contiguity
   - PR: https://github.com/pytorch/pytorch/pull/7952
   - Code excerpts:     - aten/src/THCUNN/generic/SpatialDepthwiseConvolution.cu: +  input = THCTensor_(newContiguous)(state, input); +  weight = THCTensor_(newContiguous)(state, weight); +  bias = bias ? THCTensor_(newContiguous)(state, bias) : bias; + +  // Create THCDeviceTensor



175. Issue #7039 —  (closed )
   - Issue detail: This behavior is missing from the documentation.
   - Issue: https://github.com/pytorch/pytorch/issues/7039
   - Fix PR #7654 — Document dtype arg for reduce ops
   - PR: https://github.com/pytorch/pytorch/pull/7654
   - Code excerpts:     - torch/_tensor_docs.py: +cumprod(dim, dtype=None) -> Tensor +cumsum(dim, dtype=None) -> Tensor +prod(dim=None, keepdim=False, dtype=None) -> Tensor +sum(dim=None, keepdim=False, dtype=None) -> Tensor



176. Issue #6461 —  (closed )
   - Issue detail: OS: Ubuntu 18.04 PyTorch version: 0.3.1.post2 Python version: 3.6.5 How you installed PyTorch: conda install pytorch-cpu torchvision -c pytorch Script to reproduce the bug: the tutorial script for cifar10 classification: http://pytorch.org/tutorials/_downloads/cifar10_tutorial.py At the end of the script execution, I have the following error message: ``` Exception ignored in: <bound method DataLoaderIter.__del__ of <torch.utils.data.dataloader.DataLoaderIter object at 0x7f0b579b8470>>...
   - Issue: https://github.com/pytorch/pytorch/issues/6461
   - Fix PR #6671 — Fix import error sometimes happening in dataloader when exiting Python
   - PR: https://github.com/pytorch/pytorch/pull/6671
   - Code excerpts:     - torch/utils/data/dataloader.py: +                for q in self.index_queues: +                    q.put(None) +                # if some workers are waiting to put, make place for them +                    while not self.worker_resu



177. Issue #6217 —  (closed )
   - Issue detail: PyTorch master Currently, indexing a tensor by a zero-dim tensor creates a copy. We should make it return an alias. ```python idx = torch.tensor(0, dtype=torch.int64) x = torch.arange(9).reshape(3, 3) x[idx].zero_() # no effect since x[idx] copies; it should slice instead print(x) ``` ``` 0 1 2 3 4 5 6 7 8 [torch.FloatTensor of size (3,3)] ``` Reported by lvdmaaten
   - Issue: https://github.com/pytorch/pytorch/issues/6217
   - Fix PR #6426 — Slice (instead of copy) when indexing by a zero-dim tensor
   - PR: https://github.com/pytorch/pytorch/pull/6426
   - Code excerpts:     - test/test_indexing.py: +        # indexing by a scalar should slice (not copy) +        self.assertEqual(a[0, 1].data_ptr(), a[zero, one].data_ptr()) +        self.assertEqual(a[1].data_ptr(), a[one.int()].data_ptr()) +    



178. Issue #6011 —  (closed )
   - Issue detail: @script doesn't insert expand nodes, but our fuser assumes that point-wise operators cannot broadcast, which is unsafe. We need to fix this in a way makes the fuser safe, while still having it produce good fusions for @script nodes. This can be a modification to shape analysis that is aware of the (relatively small) set of point-wise operators that do broadcasting. ``` # before analysis y = rand(1,4) z = rand(4,4) x = exp(add(y, z)) # broadcasting add # using the result of shape analysis, we...
   - Issue: https://github.com/pytorch/pytorch/issues/6011
   - Fix PR #6084 — Handle broadcasting in the JIT
   - PR: https://github.com/pytorch/pytorch/pull/6084
   - Code excerpts:     - test/expect/TestJit.test_shape_analysis_broadcast.expect: +graph(%a : Double(3, 1, 5) +      %b : Double(4, 1, 8, 5)) { +  %3 : Double(4!, 3!, 8!, 5) = aten::expand[size=[4, 3, 8, 5]](%a) +  %4 : Double(4!, 3!, 8, 5) = aten::expand[size=[4, 3, 8, 5]](%b) +  



179. Issue #4386 —  (closed )
   - Issue detail: odd difference between cuda Tensor and Variable: ```python import torch from torch.autograd import Variable a = Variable(torch.randn(8,6).cuda()) b = Variable(torch.randn(8,6).cuda()) print('passes') b.data[a.data == 0] == 0 print('fails') b[a == 0] = 0 ``` encountered in torch.distributions.Categorical, built yesterday from master
   - Issue: https://github.com/pytorch/pytorch/issues/4386
   - Fix PR #4486 — Fix handling of empty indices in CUDA Tensor.put_
   - PR: https://github.com/pytorch/pytorch/pull/4486
   - Code excerpts:     - aten/src/THC/generic/THCTensorIndex.cu: +  if (numIndices == 0) { +    return; +  }



180. Issue #4403 —  (closed )
   - Issue detail: In pytorch docs，torch.nn.RNN parts show that variable **weight_ih_l[k]** has shape of input_size x hidden_size，however it should be hidden_size x input_size.
   - Issue: https://github.com/pytorch/pytorch/issues/4403
   - Fix PR #4407 — fix documentation of RNN weight_ih_l[k] shape
   - PR: https://github.com/pytorch/pytorch/pull/4407
   - Code excerpts:     - torch/nn/modules/rnn.py: +            of shape `(hidden_size x input_size)` for k=0. Otherwise, the shape is +            `(hidden_size x hidden_size)`



181. Issue #3880 —  (closed )
   - Issue detail: `torch.utils.data.DataLoader` can use multiprocessing to load and preprocess the data. It is commonly used to overlap the GPU computation and data loading. It has a minor flaw, though. On Unix, the processes are by default created with `fork`, so the global random state is copied. If each worker does something pseudo-randomly (common in data augmentation), their actions are all the same. For example, random crop is commonly used in image classification task, and in this case, all `DataLoader`...
   - Issue: https://github.com/pytorch/pytorch/issues/3880
   - Fix PR #4018 — Add default PyTorch seeding and worker_init_fn to DataLoader
   - PR: https://github.com/pytorch/pytorch/pull/4018
   - Code excerpts:     - test/test_dataloader.py: +class SeedDataset(Dataset): + +    def __init__(self, size): +        self.size = size + +    def __getitem__(self, idx): +        return torch.initial_seed() + +    def __len__(self): +        retur



182. Issue #3554 —  (closed )
   - Issue: https://github.com/pytorch/pytorch/issues/3554
   - Fix PR #3555 — Raise exception when Variable.reinforce is called
   - PR: https://github.com/pytorch/pytorch/pull/3555
   - Code excerpts:     - torch/autograd/variable.py: +        def trim(str): +            return '\n'.join([line.strip() for line in str.split('\n')]) + +        raise RuntimeError(trim(r"""reinforce() was removed. +            Use torch.distributions i



183. Issue #3264 —  (closed )
   - Issue detail: 0.2.0+dc6510f `F.normalize(p=1)` gives NaN gradients. Manually dividing by the sum works. ### Code ```py import torch from torch.autograd.variable import Variable import torch.nn.functional as F a = Variable(torch.FloatTensor([[0,0,0,0,0.1996]]),requires_grad=True) # b = F.normalize(a, p=1, dim=1) # nan nan nan nan 0 # b = a / a.sum().clamp(min=1e-12) # 0 0 0 0 0 b.sum().backward() print(a.grad.data) ``` ### Output ``` nan nan nan nan 0 ``` or ``` 0 0 0 0 0 ```
   - Issue: https://github.com/pytorch/pytorch/issues/3264
   - Fix PR #3481 — Fix and speed-up norm_backwards
   - PR: https://github.com/pytorch/pytorch/pull/3481
   - Code excerpts:     - test/test_autograd.py: +            input.norm(norm_deg).backward() +        run_test((10,), 1) +        run_test((10,), 1.5) +    ('norm', (S, S), (2,)), +    ('norm', (S, S), (0,), '0'), +    ('norm', (S, S), (0.5,), '0_5



184. Issue #3367 —  (closed )
   - Issue detail: This causes `get_device` to not work properly on newly created empty sparse tensors. In the example below, both `get_device` should print 1 instead. ``` >>> with torch.cuda.device(1): ... x = torch.cuda.sparse.FloatTensor() # has to be empty size ... >>> x.get_device() -1 >>> x FloatTensor of size with indices: [torch.cuda.LongTensor with no dimension] and values: [torch.cuda.FloatTensor with no dimension] >>> x.get_device() 0 ```
   - Issue: https://github.com/pytorch/pytorch/issues/3367
   - Fix PR #3381 — Make sparse (new) functions conform that storage is not NULL
   - PR: https://github.com/pytorch/pytorch/pull/3381
   - Code excerpts:     - test/test_sparse.py: +    def _test_new_device(self, size, device): +        with torch.cuda.device(device): +            x = torch.cuda.sparse.DoubleTensor(*size) +        self.assertEqual(x.get_device(), device) +      



185. Issue #1356 —  (closed )
   - Issue detail: ``` import torch import torch.nn as nn from torch.autograd import Variable c = nn.Conv2d(3, 3, 3) c(None) ``` Segmentation fault: 11 @colesbury
   - Issue: https://github.com/pytorch/pytorch/issues/1356
   - Fix PR #1589 — Check for required non-None arguments in C++ autograd functions
   - PR: https://github.com/pytorch/pytorch/pull/1589
   - Code excerpts:     - test/test_nn.py: +    def test_Conv2d_missing_argument(self): +        c = nn.Conv2d(3, 3, 3) +        self.assertRaises(RuntimeError, lambda: c(None)) +



186. Issue #1455 —  (closed )
   - Issue detail: For replication, I use [word_language_model](https://github.com/pytorch/examples/tree/master/word_language_model) ``` python main.py --cuda --emsize 1500 --nhid 1500 --dropout 0.65 --epochs 40 ``` Errors ``` THCudaCheck FAIL file=/home/mktran/pytorch/torch/lib/THC/generic/THCStorage.cu line=66 error=2 : out of memory Traceback (most recent call last): File "main.py", line 163, in <module> train() File "main.py", line 136, in train loss.backward() File...
   - Issue: https://github.com/pytorch/pytorch/issues/1455
   - Fix PR #1464 — Fix memory leak introduced by 72e8190
   - PR: https://github.com/pytorch/pytorch/pull/1464
   - Code excerpts:     - torch/csrc/autograd/python_function.cpp: +  Py_INCREF((PyObject*)self);



187. Issue #1371 —  (closed )
   - Issue detail: Currently not supported. See: https://discuss.pytorch.org/t/how-do-use-logical-not-on-bytetensor/2074
   - Issue: https://github.com/pytorch/pytorch/issues/1371
   - Fix PR #1403 — added logical not operator for ByteTensor
   - PR: https://github.com/pytorch/pytorch/pull/1403
   - Code excerpts:     - test/test_torch.py: +        invert_result = ~x +        for idx in iter_indices(x): +            self.assertEqual(1 - x[idx], invert_result[idx]) +



188. Issue #1342 —  (closed )
   - Issue detail: "Randomly zeroes some of the elements of the input tensor. The elements to zero are randomized on every forward call." This is incorrect; the function also scales up by 1/(1-p), which the implementation correctly does.
   - Issue: https://github.com/pytorch/pytorch/issues/1342
   - Fix PR #1404 — corrected docstring for Dropout
   - PR: https://github.com/pytorch/pytorch/pull/1404
   - Code excerpts:     - torch/nn/modules/dropout.py: +    r"""During training, randomly zeroes some of the elements of the input +    tensor with probability *p* using samples from a bernoulli distribution. +    This has proven to be an effective techni



189. Issue #1188 —  (closed )
   - Issue detail: As Arthur Szlam reports, fb-internal cudnn is still lagging behind, and giving batch-size > 1024 with batchnorm is raising an error from cudnn. Need to check for compile-time version and disable this codepath
   - Issue: https://github.com/pytorch/pytorch/issues/1188
   - Fix PR #1199 — dont use cudnn batchnorm for cudnn < 5.1.10
   - PR: https://github.com/pytorch/pytorch/pull/1199
   - Code excerpts:     - torch/csrc/autograd/functions/batch_normalization.cpp: +               && weight && bias +               && cudnn_enabled && CUDNN_VERSION >= 5110L); +               && weight && bias && training +               && cudnn_enabled && CUDNN_VERSION >= 5110L)



190. Issue #556 —  (closed )
   - Issue detail: Currently, CMake 3.0 or higher is required for THPP. https://github.com/pytorch/pytorch/blob/master/torch/lib/THPP/CMakeLists.txt#L1 This is annoying for building from source on Ubuntu 14.04 systems, as default CMake is 2.8, and updating it requires either compiling from source or adding some random repos: http://askubuntu.com/questions/610291/how-to-install-cmake-3-2-on-ubuntu-14-04 ``` sudo apt-get install software-properties-common sudo add-apt-repository ppa:george-edison55/cmake-3.x sudo...
   - Issue: https://github.com/pytorch/pytorch/issues/556
   - Fix PR #559 — fixing THPP cmake for cmake < 3.1
   - PR: https://github.com/pytorch/pytorch/pull/559
   - Code excerpts:     - torch/lib/THPP/CMakeLists.txt: +CMAKE_MINIMUM_REQUIRED(VERSION 2.8) +     +if(${CMAKE_VERSION} VERSION_LESS "2.8.12") +  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11") +else(${CMAKE_VERSION} VERSION_LESS "2.8.12") +  if(${CMA



191. Issue #483 —  (closed )
   - Issue detail: For NeuralStyle and DeepDream.
   - Issue: https://github.com/pytorch/pytorch/issues/483
   - Fix PR #539 — Port LBFGS from Lua optim
   - PR: https://github.com/pytorch/pytorch/pull/539
   - Code excerpts:     - docs/source/optim.rst: +.. autoclass:: LBFGS +    :members:



192. Issue #484 —  (closed )
   - Issue detail: Repro: ```python import torch import numpy as np x = np.zeros((125,)) for i in range(125): x[i] = i x.shape = (5, 5, 5) x = x[:,1] print(x) print(torch.from_numpy(x)) ``` Strides seem to be copied correctly, and the first row is also ok. All other rows are garbage.
   - Issue: https://github.com/pytorch/pytorch/issues/484
   - Fix PR #489 — Fix for non-contiguous from_numpy
   - PR: https://github.com/pytorch/pytorch/pull/489
   - Code excerpts:     - test/test_torch.py: +        # check storage offset +        x = np.linspace(1, 125, 125) +        x.shape = (5, 5, 5) +        x = x[1] +        expected = torch.range(1, 125).view(5, 5, 5)[1] +        self.assertEqual(



193. Issue #219 —  (closed )
   - Issue detail: Right now, only Conv2d is wrapped to be so.
   - Issue: https://github.com/pytorch/pytorch/issues/219
   - Fix PR #226 — Add cuDNN bindings for 2D transposed convolution
   - PR: https://github.com/pytorch/pytorch/pull/226
   - Code excerpts:     - test/test_nn.py: +        constructor_args=(3, 4, 3, (2, 2), 1, (1, 1), 1, False),



194. Issue #153 —  (closed )
   - Issue detail: right now if libcudart.so is not in LD_LIBRARY_PATH, though it was found at compile-time, these lines will fail: https://github.com/pytorch/pytorch/blob/master/torch/cuda/__init__.py#L39-L43 Avoid this, by idk doing something... I think i have a few good ideas.
   - Issue: https://github.com/pytorch/pytorch/issues/153
   - Fix PR #195 — Look for libcudart in default CUDA installation paths
   - PR: https://github.com/pytorch/pytorch/pull/195
   - Code excerpts:     - setup.py: +CUDA_HOME = os.getenv('CUDA_HOME', '/usr/local/cuda') +WITH_CUDA = os.path.exists(CUDA_HOME) +    cuda_lib_dirs = ['lib64', 'lib'] +    cuda_include_path = os.path.join(CUDA_HOME, 'include') +    for



195. Issue #5552 —  (closed )
   - Issue detail: My code run well under torch 0.2, however, the following error occurs when I use torch 0.3.1, why? Traceback (most recent call last): File "../train.py", line 149, in <module> loss.backward() File "/home/jxliu/.local/lib/python3.6/site-packages/torch/autograd/variable.py", line 167, in backward torch.autograd.backward(self, gradient, retain_graph, create_graph, retain_variables) File "/home/jxliu/.local/lib/python3.6/site-packages/torch/autograd/__init__.py", line 99, in backward variables,...
   - Issue: https://github.com/pytorch/pytorch/issues/5552
   - Fix PR #5819 — Fix error message for cat-ing zero-dim tensors
   - PR: https://github.com/pytorch/pytorch/pull/5819
   - Code excerpts:     - aten/src/ATen/WrapDimUtils.h: +static inline int64_t maybe_wrap_dim(int64_t dim, const std::vector<std::vector<int64_t>> & tensor_sizes) { +  if (tensor_sizes.size() == 0) { +    // can't wrap empty list; rely on underlying implem



196. Issue #657 —  (closed )
   - Issue detail: Hi! It is not a major fix, however I think that x.transpose(-1,-3) should be valid, as it is in numpy: ``` x=np.zeros((3,5,7)) x.transpose(-1,0,-2).shape ``` > (7,3,5) ``` x=torch.FloatTensor(3,5,7) x.transpose(-1,-2) ``` >Traceback (most recent call last): > File "<stdin>", line 1, in <module> >RuntimeError: out of range at /data/users/soumith/miniconda2/conda-bld/pytorch- >cuda80-0.1.7_1485449073235/work/torch/lib/TH/generic/THTensor.c:398 Best, EO
   - Issue: https://github.com/pytorch/pytorch/issues/657
   - Fix PR #792 — Add negative dimension to transpose
   - PR: https://github.com/pytorch/pytorch/pull/792
   - Code excerpts:     - test/test_torch.py: +from itertools import product, combinations +    def test_transpose_neg(self): +        x = torch.randn(10, 20, 30) +        ndim = 3 + +        for i, j in combinations(range(ndim), 2): +           



197. Issue #7705 —  (closed )
   - Issue detail: I have a MultivariateNormal distribution with loc defined as output of neural net (given input) and diagonal covariance matrix with trainable parameters (but does not depending on some input). If I sample via `distr.rsample().detach()` and optimise sum of log_probs, `.backward()` provides correct gradients w.r.t. both loc and cov matrix params. But if I sample via `distr.sample()`, `.backward()` sets `None` gradients for cov matrix params. Here is a minimal reproducing code: ``` import torch...
   - Issue: https://github.com/pytorch/pytorch/issues/7705
   - Fix PR #7708 — [distributions] Always enable grad when calculating lazy_property
   - PR: https://github.com/pytorch/pytorch/pull/7708
   - Code excerpts:     - test/test_distributions.py: +from torch.distributions.utils import _finfo, probs_to_logits, softmax, lazy_property +    def test_lazy_property_grad(self): +        x = torch.randn(1, requires_grad=True) + +        class Dummy(ob



198. Issue #6397 —  (closed )
   - Issue detail: The readme suggests using nvidia-docker run --rm -ti --ipc=host pytorch/pytorch:latest However doing so provides quite an old version of pytorch. In [1]: import torch In [2]: torch.__version__ Out[2]: '0.2.0_2' Perhaps a new version should be built, a warning should be offered or the suggestion should be removed.
   - Issue: https://github.com/pytorch/pytorch/issues/6397
   - Fix PR #6434 — Note that the Docker Hub image is not up-to-date.
   - PR: https://github.com/pytorch/pytorch/pull/6434
   - Code excerpts:     - README.md: +You can also pull a pre-built docker image from Docker Hub and run with nvidia-docker, +but this is not currently maintained and will pull PyTorch 0.2.



199. Issue #3743 —  (closed )
   - Issue detail: The following code: ``` class Network(nn.Module): def __init__(self): super(Network, self).__init__() self.main = nn.Sequential( nn.Conv2d(1, 1, 1, 1), nn.ReLU(), nn.Conv2d(1, 1, 1, 1), ) def forward(self, v_x): return self.main(v_x).view(v_x.size(0), 1) net = Network() net.cuda() v_in = Variable(torch.Tensor(2,1,1,1).cuda(), requires_grad=True) grad_out = Variable(torch.ones(2,1,1,1).cuda()) gradient = autograd.grad(outputs=net(v_in), inputs=v_in, grad_outputs=grad_out, create_graph=True,...
   - Issue: https://github.com/pytorch/pytorch/issues/3743
   - Fix PR #3799 — Always define outputs of ConvBackwardBackward
   - PR: https://github.com/pytorch/pytorch/pull/3799
   - Code excerpts:     - torch/csrc/autograd/functions/convolution.cpp: +  // grad_output is in N, C, H, W, we re-shape and reduce over spatial dims and batches + +  if (should_compute_output(0) && !ggO.defined()) ggO = at::zeros_like(gO); +  if (should_compute_output(1) 



200. Issue #3039 —  (closed )
   - Issue detail: This snippet ``` from torch import Tensor from torch.autograd import Variable from torch.nn.functional import conv2d k = Variable(Tensor([[1]])) x = Variable(Tensor(1, 1, 1, 1)) conv2d(x, k) ``` seg faults on my install.
   - Issue: https://github.com/pytorch/pytorch/issues/3039
   - Fix PR #3052 — More shape checking for ConvNd
   - PR: https://github.com/pytorch/pytorch/pull/3052
   - Code excerpts:     - torch/csrc/autograd/functions/convolution.cpp: +				      const at::Tensor& weight, const at::Tensor& bias, +  int k = input.ndimension(); + +  if (weight.ndimension() != k) { +      std::stringstream ss; +      ss << "Expected " << k << "-dimensi



201. Issue #8282 — Loaded network with load_state_dict has different shape but works anyway (closed 2018-06-19T03:16:35Z)
   - Issue detail: After it was verified on [discuss.pytorch](https://discuss.pytorch.org/t/loaded-network-has-different-shape-but-works-anyway/19398) that this is indeed unwanted behaviour, I am forwarding this to you: ## Issue description I trained a model with among others had the following layer: `final_layer.append(nn.Conv2d(64, 1, kernel_size=1))` and then saved it to a file with state_dict and torch.save. Then, when I wanted to load that model using load_state_dict, by accident the same layer was setup...
   - Issue: https://github.com/pytorch/pytorch/issues/8282
   - Fix PR #8619 — check for exact shape match before loading
   - PR: https://github.com/pytorch/pytorch/pull/8619
   - Code excerpts:
     - torch/nn/modules/module.py: + +                if input_param.shape != param.shape: +                    # local shape should match the one in checkpoint +                    error_msgs.append('Size mismatch: copying a param of 

202. Issue #3475 — CUDA tensor allows negative values in torch.multinomial (closed 2017-12-18T07:20:27Z)
   - Issue detail: ```python import torch t = torch.rand(10) #create CPU tensor t.multinomial(1) #returns a result, as expected tn = -t tn.multinomial(1) # throws an exception, as per the documentation tn = tn.cuda() tn.multinomial(1) # returns a value, don't know from what distribution tn.multinomial(1000, True) # returns a tensor of 1000 zeros ``` Looking at the values returned from tn.multinomial(1) and counting them, it seems like it returns the values of the multinomial distribution taken from t, i.e. that...
   - Issue: https://github.com/pytorch/pytorch/issues/3475
   - Fix PR #4009 — Fix CUDA Multinomial checks
   - PR: https://github.com/pytorch/pytorch/pull/4009
   - Code excerpts:
     - aten/src/TH/generic/THTensorRandom.c: +    "cannot sample n_sample <= 0 samples"); +    double val; +      val = THStorage_(get)( \ +      THArgCheckWithCleanup((val >= 0), +                            THCleanup(THDoubleTensor_free(cum_di