# sst/opencode resolved bug issues with explicit PR/commit links
- entries: 18

1. Issue #4586 — $EDITOR keystrokes/redraw lag (closed 2025-11-21T18:36:14Z)
   - Issue: https://github.com/sst/opencode/issues/4586
   - Fix: PR #4595 https://github.com/sst/opencode/pull/4595
   - Code excerpts:     - packages/opencode/src/cli/cmd/tui/util/editor.ts: +     +    // Explicitly disable raw mode to ensure editor can read input properly +    if (process.stdin.isTTY && process.stdin.setRawMode) { +      process.stdin.setRawMode(false) +    } + + +    //

2. Issue #4568 — opentui: fatal: props.input.content?.split is not a function. (In 'props.input.content?.split(`
`)', 'props.input.content?.split' is undefined) (closed 2025-11-21T04:34:18Z)
   - Issue: https://github.com/sst/opencode/issues/4568
   - Fix: Commit 5413b16b5733 https://github.com/sst/opencode/commit/5413b16b573320f0626d93e701b783ce986750e3
   - Code excerpts:     - packages/opencode/src/cli/cmd/tui/routes/session/index.tsx: +    const lines = createMemo( +      () => (typeof props.input.content === "string" ? props.input.content.split("\n") : []), +      [] as string[], +    )

3. Issue #4523 — Unable to reference files mid sentence when typing @ after a space (closed 2025-11-20T16:37:46Z)
   - Issue: https://github.com/sst/opencode/issues/4523
   - Fix: PR #4121 https://github.com/sst/opencode/pull/4121
   - Code excerpts:     - packages/opencode/src/cli/cmd/tui/component/prompt/autocomplete.tsx: +    return props.input().getTextRange(store.index + 1, props.input().cursorOffset) +      onInput(value) { +          if ( +            // Typed text before the trigger +            props.input().cur

4. Issue #4365 — opentui: fatal: undefined is not an object (evaluating 'c3[mode2]') when using custom theme. (closed 2025-11-16T07:44:16Z)
   - Issue: https://github.com/sst/opencode/issues/4365
   - Fix: Commit e728b94bcaac https://github.com/sst/opencode/commit/e728b94bcaac1f019b3a03f04465b3c00d3fdc3a
   - Code excerpts:     - packages/opencode/src/cli/cmd/tui/context/theme.tsx: +    if (typeof c === "string") { +      if (c === "transparent" || c === "none") return RGBA.fromInts(0, 0, 0, 0) +      return c.startsWith("#") ? RGBA.fromHex(c) : resolveColor(defs[c]) +    }

5. Issue #4348 — Selecting text during an active response results in unresponsive UI (closed 2025-11-20T04:13:07Z)
   - Issue: https://github.com/sst/opencode/issues/4348
   - Fix: PR #285 https://github.com/sst/opencode/pull/285
   - Code excerpts:     - packages/tui/internal/theme/themes/matrix.json: +{ +  "$schema": "https://opencode.ai/theme.json", +  "defs": { +    "matrixInk0": "#0a0e0a", +    "matrixInk1": "#0e130d", +    "matrixInk2": "#141c12", +    "matrixInk3": "#1e2a1b", +    "rainGreen"

6. Issue #4259 — Bug: Configured Models No Longer Listed (closed 2025-11-12T19:55:32Z)
   - Issue: https://github.com/sst/opencode/issues/4259
   - Fix: Commit 8addaa7e084f https://github.com/sst/opencode/commit/8addaa7e084f8bb9a838610b311aa1110dada659
   - Code excerpts:     - packages/opencode/src/provider/provider.ts: +import { iife } from "@/util/iife" +        const name = iife(() => { +          if (model.name) return model.name +          if (model.id && model.id !== modelID) return modelID +          return ex

7. Issue #4145 — do not crash on bad user config, or if we must at least provide better feedback (closed 2025-11-10T02:36:57Z)
   - Issue: https://github.com/sst/opencode/issues/4145
   - Fix: PR #4058 https://github.com/sst/opencode/pull/4058
   - Code excerpts:     - packages/opencode/src/cli/cmd/tui/context/sync.tsx: +import { useToast } from "../ui/toast" +    const toast = useToast() +          sdk.client.lsp +            .status({ throwOnError: true }) +            .then((x) => setStore("lsp", x.data!)) +      

8. Issue #4080 — The percentage on the primary agent is always at 0% (closed 2025-11-12T16:54:36Z)
   - Issue: https://github.com/sst/opencode/issues/4080
   - Fix: Commit c5e096c76a14 https://github.com/sst/opencode/commit/c5e096c76a1435473667c4a2e99dc5c10b8fd6cb
   - Code excerpts:     - packages/opencode/src/cli/cmd/models.ts: +import type { Argv } from "yargs" +import { UI } from "../ui" +import { EOL } from "os" +  command: "models [provider]", +  builder: (yargs: Argv) => { +    return yargs +      .positional("provider"

9. Issue #4078 — Sub-agent's request for permission is not shown in the primary agent's view (closed 2025-11-21T06:53:50Z)
   - Issue: https://github.com/sst/opencode/issues/4078
   - Fix: Commit adbb6037aca2 https://github.com/sst/opencode/commit/adbb6037aca2f2c7edd839ea7a121da5bc514873
   - Code excerpts:     - packages/opencode/src/cli/cmd/tui/routes/session/index.tsx: +    if (!currentSession) return

10. Issue #4051 — Formatters not running after changes (closed 2025-11-07T20:10:48Z)
   - Issue: https://github.com/sst/opencode/issues/4051
   - Fix: Commit b3c6d0b08a57 https://github.com/sst/opencode/commit/b3c6d0b08a571796e4a9ecce798408b15a525df1

11. Issue #4042 — Tool calls abort, fail, syntax error (closed 2025-11-12T23:47:40Z)
   - Issue: https://github.com/sst/opencode/issues/4042
   - Fix: PR #4234 https://github.com/sst/opencode/pull/4234
   - Code excerpts:     - packages/opencode/src/storage/storage.ts: +      const result = await Bun.file(target).json() +      return result as T +      using _ = await Lock.write(target) +      using _ = await Lock.write(target)

12. Issue #4022 — Unexpected Errors v1.0.39 (closed 2025-11-13T20:28:03Z)
   - Issue: https://github.com/sst/opencode/issues/4022
   - Fix: Commit 779a27693a9d https://github.com/sst/opencode/commit/779a27693a9d37ae212c27af353414ff4de07ea4

13. Issue #4021 — [BUG]: Integrity check failed for tarball: opencode-darwin-arm64 (closed 2025-11-09T18:19:33Z)
   - Issue: https://github.com/sst/opencode/issues/4021
   - Fix: Commit 09bb8190640d https://github.com/sst/opencode/commit/09bb8190640dabd12908b77e2f6a0390fb7fafd6
   - Code excerpts:     - packages/opencode/script/build.ts: +  await $`npm pack ${opentui}@${pkg.dependencies["@opentui/core"]}`.cwd( +    path.join(dir, "../../node_modules"), +  ) +  const parserWorker = fs.realpathSync( +    path.resolve(dir, "./node_module

14. Issue #4017 — opentui: theme console log error when using zellij (closed 2025-11-08T22:27:08Z)
   - Issue: https://github.com/sst/opencode/issues/4017
   - Fix: PR #4083 https://github.com/sst/opencode/pull/4083
   - Code excerpts:     - packages/opencode/src/cli/cmd/tui/context/theme.tsx: +  const palette = colors.palette.filter((x) => x !== null).map((x) => RGBA.fromHex(x))

15. Issue #3993 — CLI run --model fails for namespaced models with : or multi-segment paths (truncates modelID → ProviderModelNotFoundError) (closed 2025-11-06T18:10:16Z)
   - Issue: https://github.com/sst/opencode/issues/3993
   - Fix: Commit de1278414f4f https://github.com/sst/opencode/commit/de1278414f4f11056649670f2e928631b267a74d
   - Code excerpts:     - packages/opencode/src/cli/cmd/run.ts: +import { Provider } from "../../provider/provider" +        const modelParam = args.model ? Provider.parseModel(args.model) : undefined

16. Issue #3901 — Undo command doesn't allow editing reverted message like keyboard shortcut (closed 2025-11-04T16:59:48Z)
   - Issue: https://github.com/sst/opencode/issues/3901
   - Fix: Commit 927566586850 https://github.com/sst/opencode/commit/927566586850717aa3f722170f04652723049f07
   - Code excerpts:     - packages/opencode/src/cli/cmd/tui/component/prompt/autocomplete.tsx: +          onSelect: () => { +            hide() +            command.trigger("session.undo") +          },

17. Issue #3892 — Slash commands through ACP doesn't work (closed 2025-11-05T06:56:17Z)
   - Issue: https://github.com/sst/opencode/issues/3892
   - Fix: Commit 1e0596bc46fc https://github.com/sst/opencode/commit/1e0596bc46fcd130257174e6691c74484391f905
   - Code excerpts:     - bun.lock: +        "@agentclientprotocol/sdk": "0.5.1", +    "@agentclientprotocol/sdk": ["@agentclientprotocol/sdk@0.5.1", "", { "dependencies": { "zod": "^3.0.0" } }, "sha512-9bq2TgjhLBSUSC5jE04MEe+Hqw8YePzKg

18. Issue #3777 — bun dev with different project dir fails (closed 2025-11-04T16:38:12Z)
   - Issue: https://github.com/sst/opencode/issues/3777
   - Fix: PR #3778 https://github.com/sst/opencode/pull/3778
   - Code excerpts:     - packages/opencode/script/build.ts: +  await $`npm pack ${opentui}@${pkg.dependencies["@opentui/core"]}`.cwd( +    path.join(dir, "../../node_modules"), +  ) +  const parserWorker = fs.realpathSync( +    path.resolve(dir, "./node_module

