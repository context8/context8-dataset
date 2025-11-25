# react merged PRs referencing issues via "Fix #"
- entries: 196

1. Issue #35040 — Bug:  Getting `Cannot access refs during render` error from event handler. (closed 2025-11-14T17:00:35Z)
   - Issue detail: So on react official documentations, I found, it recommend to avoid direct read or write during render on ref. Here is the docs link (under pitfall)- https://react.dev/reference/react/useRef And here I also found that ref is safe to use on event handler or effect. `You can read or write refs from event handlers or effects instead.` So, we can read `ref.current` from a onSubmit handler as it is...
   - Issue: https://github.com/facebook/react/issues/35040
   - Fix PR #35062 — [compiler] Allow ref access in callbacks passed to event handler props
   - PR: https://github.com/facebook/react/pull/35062
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/HIR/Environment.ts: + +  /** +   * Enables inference of event handler types for JSX props on built-in DOM elements. +   * When enabled, functions passed to event handler props (props starting with "on") +   * on primitiv
     - compiler/packages/babel-plugin-react-compiler/src/HIR/Globals.ts: +  BuiltInEffectEventId, +          shapeId: BuiltInEffectEventId,

2. Issue #34745 — Bug: eslint-plugin-react-hooks@6.1.1 does not export config types correctly (closed 2025-10-06T04:53:22Z)
   - Issue detail: <!-- Please provide a clear and concise description of what the bug is. Include screenshots if needed. Please test using the latest version of the relevant React packages to make sure your issue has not already been fixed. --> - rel: #34705 React version: 19.2.0 ## Steps To Reproduce 1. Install eslint-plugin-react-hooks@6.1.1 2. Import `reactHooks.configs['recommended-latest']` in...
   - Issue: https://github.com/facebook/react/issues/34745
   - Fix PR #34746 — [eprh] Fix config type not being exported correctly
   - PR: https://github.com/facebook/react/pull/34746
   - Code excerpts:
     - fixtures/eslint-v9/eslint.config.ts: +    extends: [reactHooks.configs['recommended-latest']],
     - fixtures/eslint-v9/package.json: +    "lint": "tsc --noEmit && eslint index.js --report-unused-disable-directives" +  }, +  "devDependencies": { +    "typescript": "^5.4.3"

3. Issue #10 — Can't require() react-tools module (closed 2013-05-30T12:14:18Z)
   - Issue detail: I'm trying to programatically invoke the JSX transformer (using the version of `react-tools` in the npm registry) by running something like ``` require('react-tools').transform(someCode); ``` Which then throws this error: ``` Error: Cannot find module './build/React' ``` If I comment out the lines in `main.js` that require/use `./build/React` the `react-tools` module loads fine and the...
   - Issue: https://github.com/facebook/react/issues/10
   - Fix PR #11 — Fix react-tools module
   - PR: https://github.com/facebook/react/pull/11
   - Code excerpts:
     - main.js: +var React = require('./build/react');
     - package.json: +    "build/react.js",

4. Issue #34751 — Bug: RSC `renderToReadableStream/createFromReadableStream` gets stuck for certain objects on development (closed 2025-10-27T21:06:30Z)
   - Issue detail: <!-- Please provide a clear and concise description of what the bug is. Include screenshots if needed. Please test using the latest version of the relevant React packages to make sure your issue has not already been fixed. --> React version: 19.2 (This didn't reproduce on 19.1.1. Based on old reproduction https://github.com/hi-ogawa/react-router-...
   - Issue: https://github.com/facebook/react/issues/34751
   - Fix PR #34988 — [Flight] Don't hang after resolving cyclic references
   - PR: https://github.com/facebook/react/pull/34988
   - Code excerpts:
     - packages/react-client/src/ReactFlightClient.js: +            // The status might have changed after fulfilling the reference. +            switch ((chunk: SomeChunk<T>).status) { +              case INITIALIZED: +                const initializedCh
     - packages/react-server-dom-webpack/src/__tests__/ReactFlightDOMEdge-test.js: + +  it('should properly resolve with deduped objects', async () => { +    const obj = {foo: 'hi'}; + +    function Test(props) { +      return props.obj.foo; +    } + +    const root = { +      obj: 

5. Issue #34108 — [Compiler Bug]: Compiler introduces unnecessary breaks that skips its own memoization (closed 2025-09-04T00:44:43Z)
   - Issue detail: ### What kind of issue is this? - [x] React Compiler core (the JS output is incorrect, or your app works incorrectly after optimization) - [ ] babel-plugin-react-compiler (build issue installing or using the Babel plugin) - [ ] eslint-plugin-react-compiler (build issue installing or using the eslint plugin) - [ ] react-compiler-healthcheck (build issue installing or using the healthcheck...
   - Issue: https://github.com/facebook/react/issues/34108
   - Fix PR #34335 — [compiler] Fix for scopes with unreachable fallthroughs
   - PR: https://github.com/facebook/react/pull/34335
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/AlignReactiveScopesToBlockScopesHIR.ts: +    } else if (terminal.kind === 'goto') { +      /** +       * If we encounter a goto that is not to the natural fallthrough of the current +       * block (not the topmost fallthrough on the stack)
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/align-scopes-reactive-scope-overlaps-if.expect.md: +  if ($[1] !== cond) { +    bb0: { +      if (cond) { +        items = []; +      } else { +        break bb0; +      } +      items.push(2); +    }

6. Issue #31407 — [Compiler Bug]: `'Unused 'use no memo' directive'` lint warning even though the directive is used (closed 2025-10-02T23:19:03Z)
   - Issue detail: ### What kind of issue is this? - [ ] React Compiler core (the JS output is incorrect, or your app works incorrectly after optimization) - [ ] babel-plugin-react-compiler (build issue installing or using the Babel plugin) - [X] eslint-plugin-react-compiler (build issue installing or using the eslint plugin) - [ ] react-compiler-healthcheck (build issue installing or using the healthcheck...
   - Issue: https://github.com/facebook/react/issues/31407
   - Fix PR #34703 — [eprh] Remove NoUnusedOptOutDirectives
   - PR: https://github.com/facebook/react/pull/34703
   - Code excerpts:
     - compiler/packages/eslint-plugin-react-compiler/src/rules/ReactCompilerRule.ts: +export const allRules: RulesConfig = LintRules.reduce((acc, rule) => { +  acc[rule.name] = {rule: makeRule(rule), severity: rule.severity}; +  return acc; +}, {} as RulesConfig); +).reduce((acc, rule

7. Issue #34662 — Bug: ViewTransition can stall transitions for ~60s (closed 2025-10-02T01:58:14Z)
   - Issue detail: Repro here: https://codesandbox.io/p/sandbox/repro-transition-stall-54mwcx
   - Issue: https://github.com/facebook/react/issues/34662
   - Fix PR #34676 — [Fiber] Clean up ViewTransition when it fails to start
   - PR: https://github.com/facebook/react/pull/34676
   - Code excerpts:
     - packages/react-dom-bindings/src/client/ReactFiberConfigDOM.js: +      // $FlowFixMe[prop-missing] +      if (ownerDocument.__reactViewTransition === transition) { +        // $FlowFixMe[prop-missing] +        ownerDocument.__reactViewTransition = null; +      } +

8. Issue #33612 — Bug: renderToPipeableStream is missing in Bun exports (closed 2025-10-27T22:06:46Z)
   - Issue detail: <!-- Please provide a clear and concise description of what the bug is. Include screenshots if needed. Please test using the latest version of the relevant React packages to make sure your issue has not already been fixed. --> React version: 19.10.0 ## Steps To Reproduce 1. Run under Bun and Node and see the export differense without a reason ```ts import { createServer } from "node:http";...
   - Issue: https://github.com/facebook/react/issues/33612
   - Fix PR #34193 — [react-dom] Include all Node.js APIs in Bun entrypoint for `/server`
   - PR: https://github.com/facebook/react/pull/34193
   - Code excerpts:
     - packages/react-dom/npm/server.bun.js: +exports.renderToPipeableStream = b.renderToPipeableStream; +exports.resumeToPipeableStream = b.resumeToPipeableStream;
     - packages/react-dom/server.bun.js: + +export function renderToPipeableStream() { +  return require('./src/server/react-dom-server.bun').renderToPipeableStream.apply( +    this, +    arguments, +  ); +} + +export function resumeToPipeab

9. Issue #34098 — Bug: `Transition was aborted because of invalid state` when browser tab not active (closed 2025-09-10T13:07:12Z)
   - Issue detail: <!-- Please provide a clear and concise description of what the bug is. Include screenshots if needed. Please test using the latest version of the relevant React packages to make sure your issue has not already been fixed. --> React version: 19.1.1 ## Steps To Reproduce 1. Call `document.startViewTransition` when the browser tab is not active/visible 2. Go back/select the browser tab - a...
   - Issue: https://github.com/facebook/react/issues/34098
   - Fix PR #34450 — Ignore generic InvalidStateError in View Transitions
   - PR: https://github.com/facebook/react/pull/34450
   - Code excerpts:
     - packages/react-dom-bindings/src/client/ReactFiberConfigDOM.js: +            'Skipping view transition because viewport size changed.' || +          // Chrome uses a generic error message instead of specific reasons. It will log a +          // more specific reaso

10. Issue #30782 — [Compiler Bug]: eslint-plugin-react-compiler errors when updating initialization of ref.current (closed 2025-07-29T17:53:14Z)
   - Issue detail: ### What kind of issue is this? - [ ] React Compiler core (the JS output is incorrect, or your app works incorrectly after optimization) - [ ] babel-plugin-react-compiler (build issue installing or using the Babel plugin) - [X] eslint-plugin-react-compiler (build issue installing or using the eslint plugin) - [ ] react-compiler-healthcheck (build issue installing or using the healthcheck...
   - Issue: https://github.com/facebook/react/issues/30782
   - Fix PR #34024 — [compiler] ref guards apply up to fallthrough of the test
   - PR: https://github.com/facebook/react/pull/34024
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateNoRefAccessInRender.ts: +import {retainWhere} from '../Utils/utils'; +    const safeBlocks: Array<{block: BlockId; ref: RefId}> = []; +      retainWhere(safeBlocks, entry => entry.block !== block.id); +            let safe: 
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/allow-ref-lazy-initialization-with-logical.expect.md: + +## Input + +```javascript +// @validateRefAccessDuringRender + +import {useRef} from 'react'; + +function Component(props) { +  const ref = useRef(null); +  if (ref.current == null) { +    // the l

11. Issue #33534 — Bug: Server functions error when returning a client reference (closed 2025-08-02T22:11:55Z)
   - Issue detail: Returning a temporary client reference from a server function causes an error. My understanding of the issue is that `async` functions will automatically check return values for `.then()` methods in order to flatten nested promises. However, client references in server functions [guard access to virtually all...
   - Issue: https://github.com/facebook/react/issues/33534
   - Fix PR #34084 — [Flight] Allow Temporary References to be awaited
   - PR: https://github.com/facebook/react/pull/34084
   - Code excerpts:
     - packages/react-server-dom-webpack/src/__tests__/ReactFlightDOMReply-test.js: +  it('can return an opaque object through an async function', async () => { +    function fn() { +      return 'this is a client function'; +    } + +    const args = [fn]; + +    const temporaryRefe
     - packages/react-server/src/ReactFlightServerTemporaryReferences.js: +        // Allow returning a temporary reference from an async function +        // Unlike regular Client References, a Promise would never have been serialized as +        // an opaque Temporary Ref
12. Issue #26876 — Bug: Radio button onChange not called in current React Canary (closed 2023-09-21T04:57:11Z)
   - Issue detail: <!-- Please provide a clear and concise description of what the bug is. Include screenshots if needed. Please test using the latest version of the relevant React packages to make sure your issue has not already been fixed. --> React version: 18.3.0-canary-a1f97589f-20230526 ## Steps To Reproduce 1. Create radio buttons that toggle `disabled` in `onChange` 2. After selecting each radio button,...
   - Issue: https://github.com/facebook/react/issues/26876
   - Fix PR #27443 — Fix controlled radios, maybe for real this time
   - PR: https://github.com/facebook/react/pull/27443
   - Code excerpts:
     - packages/react-dom-bindings/src/client/ReactDOMInput.js: +  if (checked != null) { +    // Important to set this even if it's not a change in order to update input +    // value tracking with radio buttons +    // TODO: Should really update input value trac
     - packages/react-dom/src/__tests__/ReactDOMComponent-test.js: +      ReactDOM.render(<audio muted={true} />, container); +      Object.defineProperty(node, 'muted', { +      ReactDOM.render(<audio muted={true} data-unrelated="yes" />, container); +      ReactDOM

13. Issue #24985 — Bug: `renderToPipeableStream()` emit mysterious mojibake whitespace chars in the result (closed 2023-02-24T19:33:57Z)
   - Issue detail: <!-- Please provide a clear and concise description of what the bug is. Include screenshots if needed. Please test using the latest version of the relevant React packages to make sure your issue has not already been fixed. --> `renderToPipeableStream()` emit mojibake whitespace chars in its result. This would sometimes breaks the final generated html. React version: 18.2.0 ## Steps To Reproduce...
   - Issue: https://github.com/facebook/react/issues/24985
   - Fix PR #26228 — [Fizz Node] Fix null bytes written at text chunk boundaries
   - PR: https://github.com/facebook/react/pull/26228
   - Code excerpts:
     - packages/react-dom/src/__tests__/ReactDOMFizzServerNode-test.js: + +  it('should encode multibyte characters correctly without nulls (#24985)', () => { +    const {writable, output} = getTestWritable(); +    const {pipe} = ReactDOMFizzServer.renderToPipeableStream(
     - packages/react-server/src/ReactServerStreamConfigNode.js: +    writeToDestination( +      destination, +      (currentView: any).subarray(0, writtenBytes), +    ); +      (currentView: any),

14. Issue #31331 — [Compiler Bug]: `"use no memo"` Directive ignored by React Compiler Playground (closed 2024-11-18T20:38:24Z)
   - Issue detail: ### What kind of issue is this? - [X] React Compiler core (the JS output is incorrect, or your app works incorrectly after optimization) - [ ] babel-plugin-react-compiler (build issue installing or using the Babel plugin) - [x] eslint-plugin-react-compiler (build issue installing or using the eslint plugin) - [ ] react-compiler-healthcheck (build issue installing or using the healthcheck...
   - Issue: https://github.com/facebook/react/issues/31331
   - Fix PR #31561 — [playground] Fixes #31331
   - PR: https://github.com/facebook/react/pull/31561
   - Code excerpts:
     - compiler/apps/playground/README.md: +## Testing +```sh +# Install playwright browser binaries +$ npx playwright install --with-deps +# Run tests +$ yarn test +```

15. Issue #31687 — Bug: [eslint-plugin-react-hooks] incorrectly reports an error when hook is called outside of a loop. (closed 2024-12-10T21:46:34Z)
   - Issue detail: The following code triggers an ESLint error with the rule `eslintreact-hooks/rules-of-hooks` stating: > "React Hook 'useState' may be executed more than once. Possibly because it is called in a loop. React Hooks must be called in the exact same order in every component render." However, the hook `useState` is not inside the loop, and there is no reason for the error to be thrown. ### React...
   - Issue: https://github.com/facebook/react/issues/31687
   - Fix PR #31720 — react-hooks/rules-of-hooks: Improve support for `do/while` loops
   - PR: https://github.com/facebook/react/pull/31720
   - Code excerpts:
     - packages/eslint-plugin-react-hooks/__tests__/ESLintRulesOfHooks-test.js: +    { +      code: normalizeIndent` +        // Valid because the hook is outside of the loop +        const Component = () => { +          const [state, setState] = useState(0); +          for (let 
     - packages/eslint-plugin-react-hooks/src/RulesOfHooks.js: +function isInsideDoWhileLoop(node) { +  while (node) { +    if (node.type === 'DoWhileStatement') { +      return true; +    } +    node = node.parent; +  } +  return false; +} + +              pathA

16. Issue #32354 — Bug: Poor error message when useEffect is called with no parameters (closed 2025-02-11T22:01:05Z)
   - Issue detail: <!-- Please provide a clear and concise description of what the bug is. Include screenshots if needed. Please test using the latest version of the relevant React packages to make sure your issue has not already been fixed. --> React version: 19.0.0 ## Steps To Reproduce 1. Call `useEffect()` - note the lack of arguments Link to code example: * https://codesandbox.io/p/sandbox/pqx384 *...
   - Issue: https://github.com/facebook/react/issues/32354
   - Fix PR #32355 — Added dev-only warning for null/undefined create in use*Effect
   - PR: https://github.com/facebook/react/pull/32355
   - Code excerpts:
     - packages/react/src/ReactHooks.js: +  if (__DEV__) { +    if (create == null) { +      console.warn( +        'React Hook useEffect requires an effect callback. Did you forget to pass a callback to the hook?', +      ); +    } +  } + +

17. Issue #28713 — Bug: `react-hooks/rules-of-hooks` does not support `do/while` loops (closed 2024-10-22T20:07:11Z)
   - Issue detail: <!-- Please provide a clear and concise description of what the bug is. Include screenshots if needed. Please test using the latest version of the relevant React packages to make sure your issue has not already been fixed. --> React version: 18.2.0 ## Steps To Reproduce 1. Use a hook inside a `do/while` loop. 2. You'll see that it's not considered a violation of the rule. <!-- Your bug will get...
   - Issue: https://github.com/facebook/react/issues/28713
   - Fix PR #28714 — `react-hooks/rules-of-hooks`: Add support for `do/while` loops
   - PR: https://github.com/facebook/react/pull/28714
   - Code excerpts:
     - packages/eslint-plugin-react-hooks/__tests__/ESLintRulesOfHooks-test.js: +    { +      code: normalizeIndent` +        // Invalid because it's dangerous and might not warn otherwise. +        // This *must* be invalid. +        function ComponentWithHookInsideLoop() { +   
     - packages/eslint-plugin-react-hooks/src/RulesOfHooks.js: +              pathArray.indexOf(segment.id) - 1,

18. Issue #31717 — [eslint-plugin-react-hooks] v5.1.0 was released without any changes in github (closed 2025-03-06T18:58:40Z)
   - Issue detail: The newer version is released https://www.npmjs.com/package/eslint-plugin-react-hooks/v/5.1.0 However, there aren't any changes in the package dir here as of the time of posting the issue. https://github.com/facebook/react/tree/372ec00c0384cd2089651154ea7c67693ee3f2a5/packages/eslint-plugin-react-hooks This is concerning because it could indicate that someone published on behalf of the react team.
   - Issue: https://github.com/facebook/react/issues/31717
   - Fix PR #32536 — docs(eslint-plugin-react-hooks): add changelog for 5.1.0 & 5.2.0
   - PR: https://github.com/facebook/react/pull/32536
   - Code excerpts:
     - packages/eslint-plugin-react-hooks/CHANGELOG.md: +## 5.2.0 + +- Support flat config ([@michaelfaith](https://github.com/michaelfaith) in [#30774](https://github.com/facebook/react/pull/30774)) +- Convert the plugin to TypeScript and provide package 

19. Issue #26095 — Bug: useSyncExternalStore will cause hydration missmatch in `StrictMode` if `serverSnapshot` is different from `snapshot` (closed 2023-05-12T21:18:05Z)
   - Issue detail: ## React version React version: 18.3.0-next-b0671f9ea-20230130 ## Problem In `StrictMode`, when using hydrateRoot to render a component that using `useSyncExternalStore` it seems that useSES will do hydration twice. But in second hydration process, useSES does not use the result of `getServerSnapshot` as initial state, which will cause hydration error. This problem will only happen in...
   - Issue: https://github.com/facebook/react/issues/26095
   - Fix PR #26791 — Fix uSES hydration in strict mode
   - PR: https://github.com/facebook/react/pull/26791
   - Code excerpts:
     - packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js: +let ReactDOM; +    ReactDOM = require('react-dom'); +  it('can hydrate uSES in StrictMode with different client and server snapshot (sync)', async () => { +    function subscribe() { +      return ()
     - packages/react-reconciler/src/ReactFiberHooks.js: +  let nextSnapshot; +  const isHydrating = getIsHydrating(); +  if (isHydrating) { +    // Needed for strict mode double render +    if (getServerSnapshot === undefined) { +      throw new Error( +  

20. Issue #31745 — [Compiler Bug]: Handle TSInstantiationExpression expressions (closed 2025-02-03T16:41:06Z)
   - Issue detail: ### What kind of issue is this? - [ ] React Compiler core (the JS output is incorrect, or your app works incorrectly after optimization) - [ ] babel-plugin-react-compiler (build issue installing or using the Babel plugin) - [ ] eslint-plugin-react-compiler (build issue installing or using the eslint plugin) - [ ] react-compiler-healthcheck (build issue installing or using the healthcheck...
   - Issue: https://github.com/facebook/react/issues/31745
   - Fix PR #32302 — [compiler] Handle TSInstantiationExpression in lowerExpression
   - PR: https://github.com/facebook/react/pull/32302
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts: +    case 'TSInstantiationExpression':
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/ts-instantiation-expression.expect.md: + +## Input + +```javascript +import {identity, invoke} from 'shared-runtime'; + +function Test() { +  const str = invoke(identity<string>, 'test'); +  return str; +} + +export const FIXTURE_ENTRYPOIN

21. Issue #30864 — Bug: Focus restore after elements are reordered does not work in child windows (closed 2024-09-13T20:29:41Z)
   - Issue detail: This affects various Microsoft products that use child windows, and is an accessibility bug for users because focus is lost when they interact with an app and the active element is moved in DOM by React. React version: 18.3.1 ## Steps To Reproduce 1. Clone the repro repo https://github.com/ling1726/react-child-window-focus-repro 2. Run `npm install` 3. Run `npm run dev` 4. Open the demo app in...
   - Issue: https://github.com/facebook/react/issues/30864
   - Fix PR #30951 — fix: restore selection should consider the window of the container
   - PR: https://github.com/facebook/react/pull/30951
   - Code excerpts:
     - packages/react-dom-bindings/src/client/ReactFiberConfigDOM.js: +  selectionInformation = getSelectionInformation(containerInfo); +  restoreSelection(selectionInformation, containerInfo);
     - packages/react-dom-bindings/src/client/ReactInputSelection.js: +function getActiveElementDeep(containerInfo) { +  let win = containerInfo?.ownerDocument?.defaultView ?? window; +  let element = getActiveElement(win.document); +export function getSelectionInformat

22. Issue #29724 — [DevTools Bug]: CVE-2024-29415 (`ip` dependency) (closed 2024-06-05T10:17:37Z)
   - Issue detail: ### Website or app https://github.com/facebook/react ### Repro steps See this vulnerability https://github.com/advisories/GHSA-2p57-rm9w-gvfp Can the version of `ip` be updated to at least v2.0.1 for react-devtools? ### How often does this bug happen? Every time ### DevTools package (automated) _No response_ ### DevTools version (automated) _No response_ ### Error message (automated) _No...
   - Issue: https://github.com/facebook/react/issues/29724
   - Fix PR #29725 — Fix #29724: `ip` dependency update for CVE-2024-29415
   - PR: https://github.com/facebook/react/pull/29725
   - Code excerpts:
     - packages/react-devtools/package.json: +    "ip": "^2.0.1",

23. Issue #29069 — Compiler: Unexpected token error when using double quotes Inside single-quoted JSX prop (closed 2024-05-15T21:40:34Z)
   - Issue detail: <!-- Please provide a clear and concise description of what the bug is. Include screenshots if needed. Please test using the latest version of the relevant React packages to make sure your issue has not already been fixed. --> React version: 19 RC ## Steps To Reproduce Use double quote mark in single-quoted JSX string prop like so: ```jsx export function Component() { return (<Message...
   - Issue: https://github.com/facebook/react/issues/29069
   - Fix PR #29079 — compiler: fix jsx text attributes with double quotes
   - PR: https://github.com/facebook/react/pull/29079
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/CodegenReactiveFunction.ts: +          if (value.value.indexOf('"') !== -1) { +            value = createJsxExpressionContainer(value.loc, value); +          }
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/quoted-strings-in-jsx-attribute-escaped.expect.md: + +## Input + +```javascript +export function Component() { +  return <Child text='Some \"text\"' />; +} + +function Child(props) { +  return props.text; +} + +export const FIXTURE_ENTRYPOINT = { +  f

24. Issue #29131 — [React 19] react compiler warns about mutating ref in specific case (closed 2024-05-20T02:13:03Z)
   - Issue detail: ## Summary im not sure what is the specific case here. i know that i dont get an error if i do any of the following: - stop returning the `execute` func in the hook - remove the useEffect - remove the listener ![image](https://github.com/facebook/react/assets/18744505/daf7ae6f-d58e-483f-bfa1-5974e815d2c3)...
   - Issue: https://github.com/facebook/react/issues/29131
   - Fix PR #29154 — compiler: fix accidental propagation of function effects from StartMemoize/FinishMemoize
   - PR: https://github.com/facebook/react/pull/29154
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/Inference/InferReferenceEffects.ts: +              [] +              []
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/allow-global-mutation-in-effect-indirect-usecallback.expect.md: +// @validatePreserveExistingMemoizationGuarantees +import { c as _c } from "react/compiler-runtime"; // @validatePreserveExistingMemoizationGuarantees

25. Issue #24665 — [DevTools] find best renderer when inspecting (closed 2022-06-08T20:01:07Z)
   - Issue detail: ## Summary <!-- Explain the **motivation** for making this change. What existing problem does the pull request solve? --> resolves #24539 When inspecting with DevTools, originally we use the first renderer where we can found a fiber with inspected element. However, if two or more renderers are nested (see the example in the issue #24539), this might cause a mismatch. In this PR, we now always...
   - Issue: https://github.com/facebook/react/pull/24665
   - Fix PR #30494 — [DevTools] Implement "best renderer" by taking the inner most matched node
   - PR: https://github.com/facebook/react/pull/30494
   - Code excerpts:
     - packages/react-devtools-shared/src/__tests__/legacy/storeLegacy-v15-test.js: +        const deepestedNodeID = global.agent.getIDForHostInstance(ref);
     - packages/react-devtools-shared/src/__tests__/store-test.js: +      const deepestedNodeID = agent.getIDForHostInstance(ref.current);

26. Issue #29068 — [React 19]: `eslint-plugin-react-compiler` defines no `main` in its package.json (closed 2024-05-15T21:02:21Z)
   - Issue detail: ## Summary <!-- Please provide a CodeSandbox (https://codesandbox.io/s/new), a link to a repository on GitHub, or provide a minimal code example that reproduces the problem. You may provide a screenshot of the application if you think it is relevant to your bug report. Here are some tips for providing a minimal example: https://stackoverflow.com/help/mcve. --> `require('eslint-plugin-react-...
   - Issue: https://github.com/facebook/react/issues/29068
   - Fix PR #29072 — Add a `main` field to `eslint-plugin-react-compiler`, fixes #29068.
   - PR: https://github.com/facebook/react/pull/29072
   - Code excerpts:
     - compiler/packages/eslint-plugin-react-compiler/package.json: +  "main": "dist/index.js",

27. Issue #29106 — [React 19] React compiler is warning on mutating values in refs that are used in JSX. (closed 2024-05-29T14:46:32Z)
   - Issue detail: ## Summary When mutating a ref value in an event handler (e.g. when dealing with uncontrolled inputs), the React Compiler ESLint rule is giving the following error: ESLint: Updating a value used previously in JSX is not allowed. Consider moving the mutation before the JSX(react-compiler/react-compiler) Linked CodeSandbox: https://codesandbox.io/p/sandbox/kind-mirzakhani-qzw4t3 Linked Compiler...
   - Issue: https://github.com/facebook/react/issues/29106
   - Fix PR #29591 — compiler: Allow global mutation in jsx props
   - PR: https://github.com/facebook/react/pull/29591
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/Inference/InferReferenceEffects.ts: +        if (instrValue.tag.kind === "Identifier") { +          state.referenceAndRecordEffects( +            instrValue.tag, +            Effect.Freeze, +            ValueReason.JsxCaptured, +       
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/allow-modify-global-in-callback-jsx.expect.md: + +## Input + +```javascript +import { useMemo } from "react"; + +const someGlobal = { value: 0 }; + +function Component({ value }) { +  const onClick = () => { +    someGlobal.value = value; +  }; + 

28. Issue #26910 — Bug: React fails to log invariant 306 message when lazy() resolves to a `Fragment` (closed 2024-07-23T17:00:52Z)
   - Issue detail: <!-- Please provide a clear and concise description of what the bug is. Include screenshots if needed. Please test using the latest version of the relevant React packages to make sure your issue has not already been fixed. --> React version: 18.2.0 ## Steps To Reproduce 1. Try to render this component: `const LazyFragment = lazy(() => Promise.resolve({ default: Fragment }));` <!-- Your bug will...
   - Issue: https://github.com/facebook/react/issues/26910
   - Fix PR #30372 — Log Fragment name when trying to render a lazy fragment
   - PR: https://github.com/facebook/react/pull/30372
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberBeginWork.js: +  const loggedComponent = getComponentNameFromType(Component) || Component; + +    `Element type is invalid. Received a promise that resolves to: ${loggedComponent}. ` +
     - packages/react-reconciler/src/__tests__/ReactLazy-test.internal.js: +  it('throws with a useful error when wrapping fragment with lazy()', async () => { +    const BadLazy = lazy(() => fakeImport(React.Fragment)); + +    const root = ReactTestRenderer.create( +      <

29. Issue #25625 — Update before hydration completed error does not clarify which suspense boundary or which update (closed 2022-11-16T03:10:55Z)
   - Issue detail: Error in question: > Uncaught Error: This Suspense boundary received an update before it finished hydrating. This caused the boundary to switch to client rendering. The usual way to fix this is to wrap the original update in startTransition. The current error gives no indication which part of the code causes the error, making it very hard to debug. Two suggestions / questions: **Indicate which...
   - Issue: https://github.com/facebook/react/issues/25625
   - Fix PR #25692 — Remove recoverable error when a sync update flows into a dehydrated boundary
   - PR: https://github.com/facebook/react/pull/25692
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberBeginWork.new.js: +      // If we have scheduled higher pri work above, this will just abort the render +      // since we now have higher priority work. We'll try to infinitely suspend until +      // we yield. TODO: 

30. Issue #29107 — [React 19] `eslint-plugin-react-compiler` throws SyntaxErrors when it encounters `.json` or `.graphql` files (closed 2024-05-31T23:04:49Z)
   - Issue detail: ## Summary If your linting command encompasses `.json` or `.graphql` files (e.g. `eslint . package.json --ext .js,.jsx,.ts,.tsx,.graphql`), and you have react-compiler/react-compiler enabled in your rules object: ``` rules: { 'react-compiler/react-compiler': 'error', ``` Then HermesParser will throw an exception and stop linting: ``` SyntaxError: Error while loading rule 'react-compiler/react-...
   - Issue: https://github.com/facebook/react/issues/29107
   - Fix PR #29631 — [compiler:eslint] Don't crash if hermes parser fails to parse
   - PR: https://github.com/facebook/react/pull/29631
   - Code excerpts:
     - compiler/packages/eslint-plugin-react-compiler/src/rules/ReactCompilerRule.ts: +      try { +        babelAST = HermesParser.parse(sourceCode, { +          babel: true, +          enableExperimentalComponentSyntax: true, +          sourceFilename: filename, +          sourceType

31. Issue #29161 — [Compiler Bug]: Compiler doesn't bail out when reading or writing `ref.current` during a render (closed 2024-05-29T16:27:48Z)
   - Issue detail: ### What kind of issue is this? - [X] React Compiler core (the JS output is incorrect, or your app works incorrectly after optimization) - [ ] babel-plugin-react-compiler (build issue installing or using the Babel plugin) - [ ] eslint-plugin-react-compiler (build issue installing or using the eslint plugin) - [ ] react-compiler-healthcheck (build issue installing or using the healthcheck...
   - Issue: https://github.com/facebook/react/issues/29161
   - Fix PR #29170 — compiler: ValidateNoRefInRender detects writes of refs
   - PR: https://github.com/facebook/react/pull/29170
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateNoRefAccesInRender.ts: +  SourceLocation, +              validateNoRefAccess( +                errors, +                refAccessingFunctions, +                operand, +                operand.loc +              ); +      
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/error.invalid-aliased-ref-in-callback-invoked-during-render-.expect.md: +     |                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^ InvalidReact: Ref values (the `current` property) may not be accessed during render. (https://react.dev/reference/react/useRef) (9:9

32. Issue #29135 — React compiler healthcheck (and ESLint plugin) ignores all files if a babel.config.js file is present (closed 2024-05-29T02:46:42Z)
   - Issue detail: ## Summary Create the following two files in a new directory: ``` // index.jsx const App = () => <div />; // babel.config.js export default {}; ``` Then run `npx react-compiler-healthcheck --src index.jsx`. It reports `Successfully compiled 0 out of 0 components.` Then remove the `babel.config.js` file (or comment out the line inside it) and run `npx react-compiler-healthcheck --src index.jsx`...
   - Issue: https://github.com/facebook/react/issues/29135
   - Fix PR #29211 — [compiler:babel] Don't read config files when not running as part of
   - PR: https://github.com/facebook/react/pull/29211
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/Babel/RunReactCompilerBabelPlugin.ts: +    configFile: false, +    babelrc: false,
     - compiler/packages/eslint-plugin-react-compiler/src/rules/ReactCompilerRule.ts: +          configFile: false, +          babelrc: false,

33. Issue #29854 — [React 19] useSyncExternalStore shim might break (closed 2024-06-12T18:13:18Z)
   - Issue detail: ## Summary I just wanted to bring this to your attention - the `uSES` shim was previously packaged in a way that accessed `__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED` and the new 1.4 RC versions directly access `__CLIENT_INTERNALS_DO_NOT_USE_OR_WARN_USERS_THEY_CANNOT_UPGRADE`. So either way, there will be versions of the `uSES` shim and React that will break when compiling them with...
   - Issue: https://github.com/facebook/react/issues/29854
   - Fix PR #29868 — Avoid acccessing React internals from `use-sync-external-store/shim`
   - PR: https://github.com/facebook/react/pull/29868
   - Code excerpts:
     - packages/use-sync-external-store/src/__tests__/useSyncExternalStoreShared-test.js: +let assertConsoleErrorDev; +    assertConsoleErrorDev = InternalTestUtils.assertConsoleErrorDev; +      await act(() => { +        ReactDOM.flushSync(async () => +          root.render(React.createEl
     - packages/use-sync-external-store/src/useSyncExternalStore.js: +  // Avoid transforming the `console.error` call as it would cause the built artifact +  // to access React internals, which exist under different paths depending on the +  // React version. +  conso

34. Issue #29200 — [Flight] Add failing test for dedupe resolution on blocked models (closed 2024-05-21T18:12:21Z)
   - Issue detail: Triggered by https://github.com/vercel/next.js/pull/66033 ~I was suspecting that the bug was introduced with #28996, but I could not make the test succeed on a commit before that PR, so maybe this assumption (or the reproduction) is wrong.~ EDIT: With a revert of #28996, the test does succeed.
   - Issue: https://github.com/facebook/react/pull/29200
   - Fix PR #29201 — [Flight / Flight Reply] Don't clear pending listeners when entering blocked state
   - PR: https://github.com/facebook/react/pull/29201
   - Code excerpts:
     - packages/react-server-dom-webpack/src/__tests__/ReactFlightDOMBrowser-test.js: +  it('should resolve deduped objects within the same model root when it is blocked', async () => { +    let resolveClientComponentChunk; + +    const ClientOuter = clientExports(function ClientOuter(

35. Issue #29598 — compiler feature request: report error on reassigning a const (closed 2024-05-28T20:09:26Z)
   - Issue detail: ### What kind of issue is this? - [ ] React Compiler core (the JS output is incorrect, or your app works incorrectly after optimization) - [ ] babel-plugin-react-compiler (build issue installing or using the Babel plugin) - [ ] eslint-plugin-react-compiler (build issue installing or using the eslint plugin) - [ ] react-compiler-healthcheck (build issue installing or using the healthcheck...
   - Issue: https://github.com/facebook/react/issues/29598
   - Fix PR #29619 — compiler: error on reassigning to const
   - PR: https://github.com/facebook/react/pull/29619
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts: +  } else if ( +    binding.bindingKind === "const" && +    kind === InstructionKind.Reassign +  ) { +    builder.errors.push({ +      reason: `Cannot reassign a \`const\` variable`, +      severity: 
     - compiler/packages/babel-plugin-react-compiler/src/HIR/HIR.ts: +import { BindingKind } from "@babel/traverse"; +  | { kind: "Identifier"; identifier: Identifier; bindingKind: BindingKind }

36. Issue #28968 — Update react GitHub page CNAME record (closed 2024-05-03T14:05:53Z)
   - Issue detail: React GitHub page (https://facebook.github.io/react) (`gh-pages` branch) currently pointing to [reactjs.org](https://reactjs.org) and then it redirects to https://react.dev/. So many redirects, can we update the content of `CNAME` file with `react.dev`, if it ok to do, then I am very happy to do the same and I'll contribution in real open source project.
   - Issue: https://github.com/facebook/react/issues/28968
   - Fix PR #28983 — Update CNAME in gh-pages
   - PR: https://github.com/facebook/react/pull/28983
   - Code excerpts:
     - CNAME: +react.dev

37. Issue #13688 — Global `window.event` is overwritten in React 16.5+ in development mode.  (closed 2018-09-25T15:24:23Z)
   - Issue detail: **Do you want to request a *feature* or report a *bug*?** Report a bug. **What is the current behavior?** Global `window.event` is overwritten in React 16.5+ in development mode. Here're minimal repro steps: - React **16.5.2 in dev mode**: https://jsfiddle.net/sergei_startsev/ecz103vL/2/ If you click the button, you see `DOMContentLoaded` event type. **What is the expected behavior?** The...
   - Issue: https://github.com/facebook/react/issues/13688
   - Fix PR #13697 — Restore global window.event after event dispatching (#13688)
   - PR: https://github.com/facebook/react/pull/13697
   - Code excerpts:
     - packages/shared/invokeGuardedCallbackImpl.js: +      // Keeps track of the descriptor of window.event to restore it after event +      // dispatching: https://github.com/facebook/react/issues/13688 +      const windowEventDescriptor = Object.getO

38. Issue #4721 — Shallow rendering won't render primitive nodes in 0.14 (closed 2015-08-31T20:30:56Z)
   - Issue detail: This might be intentional, but it's technically a breaking change, so I figured I'd report it. The following script: ``` js var React = require('react'); var TestUtils; if (React.version.substring(4) == '0.13') { TestUtils = require('react/addons').addons.TestUtils; } else { TestUtils = require('react-addons-test-utils'); } var renderer = TestUtils.createRenderer(); renderer.render(...
   - Issue: https://github.com/facebook/react/issues/4721
   - Fix PR #4735 — Better error for invalid element when shallow rendering
   - PR: https://github.com/facebook/react/pull/4735
   - Code excerpts:
     - src/test/ReactTestUtils.js: +  invariant( +    ReactElement.isValidElement(element), +    'ReactShallowRenderer render(): Invalid component element.%s', +    typeof element === 'function' ? +      ' Instead of passing a componen
     - src/test/__tests__/ReactTestUtils-test.js: +  it('should throw for invalid elements', function() { +    var SomeComponent = React.createClass({ +      render: function() { +        return <div />; +      }, +    }); + +    var shallowRenderer 

39. Issue #4233 — Cryptic error message for findDOMNode of unmounted component (closed 2015-08-28T19:52:18Z)
   - Issue detail: As per https://github.com/facebook/react/issues/2410#issuecomment-115659185: findDOMNode(this) throws for unmounted components, but the error message is too cryptic: `Uncaught Error: Invariant Violation: Component (with keys: getDOMNode,_handleChange,props,context,state,refs,_reactInternalInstance) contains render method but is not mounted in the DOM` Some expert React users honestly thought...
   - Issue: https://github.com/facebook/react/issues/4233
   - Fix PR #4727 — Make findDOMNode error clearer
   - PR: https://github.com/facebook/react/pull/4727
   - Code excerpts:
     - src/renderers/dom/client/__tests__/findDOMNode-test.js: +    var Foo = React.createClass({ +      render: function() { +        return <div />; +      }, +    }); + +    var container = document.createElement('div'); +    var inst = ReactDOM.render(<Foo />
     - src/renderers/dom/client/findDOMNode.js: +    'findDOMNode was called on an unmounted component.'

40. Issue #28595 — Bug: [Flight] Async server components in `ai/rsc` not rendered correctly (closed 2024-04-01T16:37:28Z)
   - Issue detail: When returning an async server component from an `ai/rsc` tool's `render` function, a reference to it is not serialized as a lazy node, even though it might not have been emitted as a row yet. Currently the React Flight Client is not resilient to this. This leads to the reference not being resolved correctly, and then `null` is rendered instead of the element. The bug was introduced with...
   - Issue: https://github.com/facebook/react/issues/28595
   - Fix PR #28669 — [Flight] Update stale blocked values in `createModelResolver`
   - PR: https://github.com/facebook/react/pull/28669
   - Code excerpts:
     - packages/react-client/src/ReactFlightClient.js: + +    // If this is the root object for a model reference, where `blocked.value` +    // is a stale `null`, the resolved value can be used directly. +    if (key === '' && blocked.value === null) { +
     - packages/react-server-dom-webpack/src/__tests__/ReactFlightDOM-test.js: +  it('should handle streaming async server components', async () => { +    const reportedErrors = []; + +    const Row = async ({current, next}) => { +      const chunk = await next; + +      if (chu

41. Issue #27657 — Bug: Select when passed a value as Prop errors with a suggestion to pass readOnly  (closed 2023-12-01T15:55:57Z)
   - Issue detail: Seems weird when we try to use a `select` component, and pass a value as a prop, it prompts with the error to either set `onChange` or `readOnly`. the `readOnly` at the last seems misleading since the `select` component does not have a `readOnly` prop, unlike inputs which do have a `readOnly` attribute. **SELECT PROPS** https://react.dev/reference/react-dom/components/select seems an easy fix...
   - Issue: https://github.com/facebook/react/issues/27657
   - Fix PR #27740 — fix: select console error to not suggest to set readonly to true
   - PR: https://github.com/facebook/react/pull/27740
   - Code excerpts:
     - packages/react-dom-bindings/src/shared/ReactControlledValuePropTypes.js: +      if (tagName === 'select') { +        console.error( +          'You provided a `value` prop to a form field without an ' + +            '`onChange` handler. This will render a read-only field. 
     - packages/react-dom/src/__tests__/ReactDOMSelect-test.js: + +    it('should not warn about missing onChange if value is not set', () => { +      expect(() => { +        ReactTestUtils.renderIntoDocument( +          <select> +            <option value="monkey

42. Issue #28203 — Bug: Removal of custom element property sets it to `null` rather than `undefined` (closed 2024-04-02T15:48:28Z)
   - Issue detail: React version: experimental ## Steps To Reproduce 1. Set up a React project with `react@experimental` & `react-dom@experimental` which includes custom element property support. 2. Render a custom element with a property value provided as prop, then on a re-render remove that prop. e.g. ```jsx function App() { const [condition, setCondition] = useState(false); return ( <> <button onClick={() =>...
   - Issue: https://github.com/facebook/react/issues/28203
   - Fix PR #28716 — Differentiate null and undefined in Custom Elements - removing sets to undefined
   - PR: https://github.com/facebook/react/pull/28716
   - Code excerpts:
     - packages/react-dom-bindings/src/client/ReactDOMComponent.js: +          if (propValue === undefined) { +            undefined, +            lastProp !== undefined && +              undefined, +            (nextProp !== undefined || lastProp !== undefined)
     - packages/react-dom/src/__tests__/DOMPropertyOperations-test.js: +      expect(customelement.oncustomevent).toBe(undefined); +      expect(customElement.foo).toBe(undefined); + +    it('switching between null and undefined should update a property', async () => { +

43. Issue #22481 — Reactdevtools  -----> Modal deleting filter fix (closed 2021-10-01T17:50:07Z)
   - Issue detail: whats the problem? As you can see in below when we try to delete the last filter index , it closes the whole modal but rather it should just delete the last filter this PR fixes this issue ![127568480-5210f281-2f37-4388-baf3-ac81008cd8eb](https://user-images.githubusercontent.com/72331432/135650644-75132201-57aa-41a7-8ff2-4f613c47a498.gif) Fixed- ![127568697-12c28e3e-bf43-47dd-...
   - Issue: https://github.com/facebook/react/pull/22481
   - Fix PR #22484 — Reopen #22481 Fixed modal closing issue
   - PR: https://github.com/facebook/react/pull/22484
   - Code excerpts:
     - packages/react-devtools-shared/src/devtools/views/hooks.js: +        ownerDocument.addEventListener('click', handleDocumentClick, true); +        ownerDocument.removeEventListener('click', handleDocumentClick, true);

44. Issue #27572 — Bug: 'Warning: validateDOMNesting: <hr> cannot appear as a child of <select>' – but this is now valid HTML (closed 2023-10-31T21:43:17Z)
   - Issue detail: The latest version of Chrome and Safari support `hr` elements as children of `select` elements, and the HTML spec has been updated – but React warns about this as it used to be invalid HTML. - https://developer.chrome.com/blog/hr-in-select - https://webkit.org/blog/14445/webkit-features-in-safari-17-0/#:~:text=Horizontal%20rules%20inside%20select%20elements - https://html.spec.whatwg.org/#the-...
   - Issue: https://github.com/facebook/react/issues/27572
   - Fix PR #27632 — validateDOMNesting: Allow hr as child of select
   - PR: https://github.com/facebook/react/pull/27632
   - Code excerpts:
     - packages/react-dom-bindings/src/client/validateDOMNesting.js: +      return ( +        tag === 'hr' || +        tag === 'option' || +        tag === 'optgroup' || +        tag === '#text' +      );

45. Issue #20186 — Distribute source maps for easier debugging in Chrome's Performance tab (closed 2023-11-07T18:59:28Z)
   - Issue detail: ~~I want to propose the addition of a new file in the `react-dom` npm package called `react-dom.production.js` — a non-minified version of `react-dom` production build.~~ Edit: After some discussion(see below) it seems that distributing source maps makes more sense. Source maps will help you see the real function names and explore them. (The points below apply for source maps as well.) ## Why?...
   - Issue: https://github.com/facebook/react/issues/20186
   - Fix PR #26446 — Generate sourcemaps for production build artifacts
   - PR: https://github.com/facebook/react/pull/26446
   - Code excerpts:
     - scripts/rollup/build.js: +const path = require('path'); +    sourcemap: false, +function getBundleTypeFlags(bundleType) { +  const isUMDBundle = +    bundleType === UMD_DEV || +    bundleType === UMD_PROD || +    bundleType =
     - scripts/rollup/plugins/closure-plugin.js: +module.exports = function closure(flags = {}, {needsSourcemaps}) { +    async renderChunk(code, chunk, options) { + +      // Use a path like `node_modules/react/cjs/react.production.min.js.map` for 

46. Issue #26756 — [DevTools Bug]: React pages not being detected as using React in Incognito mode (closed 2023-05-03T16:27:41Z)
   - Issue detail: ### Website or app https://opensource.fb.com ### Repro steps It seems that with the latest update of Chrome and React DevTools, it cannot detect pages as using React on incognito. Screenshot attached below: <img width="518" alt="image" src="https://user-images.githubusercontent.com/34370238/235575519-8eeaa3c5-80fa-4cc4-a33d-3d2f0541f0d9.png"> * _Chrome version: 112.0.5615.137 (arm64)_ * _React...
   - Issue: https://github.com/facebook/react/issues/26756
   - Fix PR #26765 — fix[dynamic-scripts-injection]: unregister content scripts before registration
   - PR: https://github.com/facebook/react/pull/26765
   - Code excerpts:
     - packages/react-devtools-extensions/src/background.js: +async function dynamicallyInjectContentScripts() { +  const contentScriptsToInject = [ +    { +      id: 'hook', +      matches: ['<all_urls>'], +      js: ['build/installHook.js'], +      runAt: 'do

47. Issue #26200 — Bug:  React dev tools inspect element of hover does not work on shadow elements (closed 2023-06-07T15:38:40Z)
   - Issue detail: Using react while making a shadow DOM and then using react devtools inspect element feature does not work as expected video and codesandbox below **sandboxLink** https://stackblitz.com/edit/react-zqp67t?file=src/App.js **while attaching shadowroot** https://user-images.githubusercontent.com/72331432/219961254-65c9e84c-9774-441f-9eec-e9ef58f1382d.mp4 **without attaching root** https://user-...
   - Issue: https://github.com/facebook/react/issues/26200
   - Fix PR #26888 — Fix:- Fixed dev tools inspect mode on Shadow dom
   - PR: https://github.com/facebook/react/pull/26888
   - Code excerpts:
     - packages/react-devtools-shared/src/backend/views/Highlighter/index.js: +      window.addEventListener('pointermove', onPointerMove, true); +      window.removeEventListener('pointermove', onPointerMove, true); +    selectFiberForNode(getEventTarget(event)); +  let lastHo

48. Issue #26821 — [DevTools Bug]: Strict mode badge points to the old docs (closed 2023-05-17T12:34:36Z)
   - Issue detail: ### Website or app https://fb.me/devtools-strict-mode ### Repro steps The Strict mode warning badge points to https://fb.me/devtools-strict-mode which points to the strict mode section in [the old docs](https://legacy.reactjs.org/docs/strict-mode.html) instead of [the new docs](https://react.dev/reference/react/StrictMode). Badge: <img width="273" alt="Screenshot 2023-05-16 at 20 20 59"...
   - Issue: https://github.com/facebook/react/issues/26821
   - Fix PR #26825 — Fix strict mode badge URL
   - PR: https://github.com/facebook/react/pull/26825
   - Code excerpts:
     - packages/react-devtools-shared/src/devtools/views/Components/InspectedElement.js: +        href="https://react.dev/reference/react/StrictMode"

49. Issue #27177 — Bug: [18.3.0-canary] renderToString hoists some tags to top(working in 18.2) (closed 2023-08-22T17:54:34Z)
   - Issue detail: <!-- Please provide a clear and concise description of what the bug is. Include screenshots if needed. Please test using the latest version of the relevant React packages to make sure your issue has not already been fixed. --> React version: 18.3.0-canary-493f72b0a-20230727 ## Steps To Reproduce 1. run following code. ```js import * as ReactDOMServer from "react-dom/server"; const element = (...
   - Issue: https://github.com/facebook/react/issues/27177
   - Fix PR #27269 — [Float][Fizz][Legacy] hoisted elements no longer emit before `<html>` in legacy apis such as `renderToString()`
   - PR: https://github.com/facebook/react/pull/27269
   - Code excerpts:
     - packages/react-dom-bindings/src/server/ReactFizzConfigDOM.js: +export const ROOT_HTML_MODE = 0; // Used for the root most element tag. +const HTML_MODE = 2; +export const doctypeChunk: PrecomputedChunk = +  stringToPrecomputedChunk('<!DOCTYPE html>'); + +import 
     - packages/react-dom-bindings/src/server/ReactFizzConfigDOMLegacy.js: +import { +  stringToChunk, +  stringToPrecomputedChunk, +} from 'react-server/src/ReactServerStreamConfig'; + +// this chunk is empty on purpose because we do not want to emit the DOCTYPE in legacy m

50. Issue #18945 — DevTools: Improve browser extension iframe support (closed 2024-04-17T18:15:59Z)
   - Issue detail: <!-- Please provide a clear and concise description of what the bug is. Include screenshots if needed. Please test using the latest version of the relevant React packages to make sure your issue has not already been fixed. --> When react is inside an iframe, chrome extension for react devtools fails to detect react. This is because the extension sets `__REACT_DEVTOOLS_GLOBAL_HOOK__` only on the...
   - Issue: https://github.com/facebook/react/issues/18945
   - Fix PR #19854 — DevTools: Improve browser extension iframe support
   - PR: https://github.com/facebook/react/pull/19854
   - Code excerpts:
     - fixtures/devtools/iframe/iframe-in-component.html: +<!DOCTYPE html> +<html> +  <head> +    <script crossorigin src="https://unpkg.com/react@16/umd/react.development.js"></script> +    <script crossorigin src="https://unpkg.com/react-dom@16/umd/react-d
     - fixtures/devtools/iframe/iframe-other-origin.html: +<!DOCTYPE html> +<html> +  <head></head> +  <body> +    <iframe src="http://127.0.0.1:3000/main.html"></iframe> +  </body> +</html>

51. Issue #26226 — Bug: Nested useTransition makes isPending of outer one always false (closed 2023-03-16T01:10:54Z)
   - Issue detail: Nested `startTransition` call "takes over" and makes parent `startTransition` unable to track `isPending`. Seb says it's a bug. Repro: https://codesandbox.io/s/pensive-breeze-rg70wn?file=/IndexPage.js:192-288 1. Click the button 2. `isPending` in `IndexPage.js` is `true` However, `isPending` in `App.js` is `false`. Expected: `isPending` in `App.js` is also `true`.
   - Issue: https://github.com/facebook/react/issues/26226
   - Fix PR #26243 — Setting transition pending flag shouldn't be part of a surrounding transition
   - PR: https://github.com/facebook/react/pull/26243
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberHooks.js: +  ReactCurrentBatchConfig.transition = null; +  setPending(true); +  const currentTransition = (ReactCurrentBatchConfig.transition = +    ({}: BatchConfigTransition));
     - packages/react-reconciler/src/__tests__/ReactTransition-test.js: + +  it('tracks two pending flags for nested startTransition (#26226)', async () => { +    let update; +    function App() { +      const [isPendingA, startTransitionA] = useTransition(); +      const

52. Issue #25989 — Feat(renderToPipeableStream): Allow passing crossorigin attribute on bootstrapScripts (closed 2023-06-13T16:12:11Z)
   - Issue detail: When using `window.onerror` in the bootstrap script that is hosted in a CDN the error message will show `"Script error."` instead of a proper error message. This is because of the [cross-origin](https://blog.sentry.io/2016/05/17/what-is-script-error/) script. To fix this issue a `crossorigin="anonymous"` attribute needs to be added in the script tag. Currently, `bootstrapScripts` supports...
   - Issue: https://github.com/facebook/react/issues/25989
   - Fix PR #26844 — Add support for 'crossorigin' attribute on bootstrapScripts and bootstrapModules
   - PR: https://github.com/facebook/react/pull/26844
   - Code excerpts:
     - packages/react-dom-bindings/src/server/ReactFizzConfigDOM.js: +const scriptCrossOrigin = stringToPrecomputedChunk('" crossorigin="'); +  crossOrigin?: string, +      const crossOrigin = +        typeof scriptConfig === 'string' || scriptConfig.crossOrigin == nul
     - packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js: +  it('accepts a crossOrigin property for bootstrapScripts and bootstrapModules', async () => { +    await act(() => { +      const {pipe} = renderToPipeableStream( +        <html> +          <head />

53. Issue #25964 — Bug: Suspense | client component should have a queue (closed 2023-02-24T20:06:29Z)
   - Issue detail: React version: 18.2.0 Next version: 13.1.1 ## Steps To Reproduce 1. Suspend using a (fake) promise in a client component in app dir (next) 2. Try to useState after the use() call ````ts 'use client'; import { use, useState } from 'react'; const testPromise = new Promise((resolve) => { setTimeout(() => { resolve('use test promise'); }); }); export default function Page() { use(testPromise);...
   - Issue: https://github.com/facebook/react/issues/25964
   - Fix PR #26232 — Switch to mount dispatcher after use() when needed
   - PR: https://github.com/facebook/react/pull/26232
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberHooks.js: +    if (didScheduleRenderPhaseUpdateDuringThisPass) { +      // It's possible that a use() value depended on a state that was updated in +      // this rerender, so we need to watch for different the
     - packages/react-reconciler/src/__tests__/ReactHooks-test.internal.js: +        'Update hook called on initial render. This is likely a bug in React. Please file an issue.',

54. Issue #PR35159 — [Flight] Reduce risk of maximum call stack exceeded when emitting async sequence (closed 2025-11-17T17:54:13Z)
   - Issue detail: Refactors async sequence emission to reduce stack depth (single return with breaks) and keeps manual depth guard to avoid call stack overflow risk.
   - Issue: PR-only
   - Fix PR #35159 — [Flight] Reduce risk of maximum call stack exceeded when emitting async sequence
   - PR: https://github.com/facebook/react/pull/35159
   - Code excerpts:
     - packages/react-server/src/ReactFlightServer.js: let previousIONode: void | null | PromiseNode | IONode = null; // We can't use multiple return statements in the following switch; refactor to reduce stack depth.

55. Issue #PR35143 — [Flight] Fix pending chunks count for streams & async iterables in DEV (closed 2025-11-14T22:52:12Z)
   - Issue detail: In DEV retain a strong reference to the response while pending chunks/results remain for ReadableStreams/AsyncIterables to avoid GC while work is outstanding.
   - Issue: PR-only
   - Fix PR #35143 — [Flight] Fix pending chunks count for streams & async iterables in DEV
   - PR: https://github.com/facebook/react/pull/35143
   - Code excerpts:
     - packages/react-client/src/ReactFlightClient.js: if (__DEV__) { if (response._pendingChunks++ === 0) { response._weakResponse.response = response; } }

56. Issue #PR35117 — [react-dom] Batch updates from resize until next frame (closed 2025-11-13T12:30:22Z)
   - Issue detail: Treat resize like scroll: batch state updates during a frame and flush before next paint instead of flushing on discrete events.
   - Issue: PR-only
   - Fix PR #35117 — [react-dom] Batch updates from resize until next frame
   - PR: https://github.com/facebook/react/pull/35117
   - Code excerpts:
     - packages/react-dom-bindings/src/events/ReactDOMEventListener.js: case 'resize': // batch continuous resize events before painting.

57. Issue #PR34995 — [compiler] Fix false negatives for deriving state in effects; add data flow tree (closed 2025-11-10T20:16:27Z)
   - Issue detail: Revamps derivation tracking to avoid missing derived-state-in-effects violations; error output now includes data flow tree for debugging.
   - Issue: PR-only
   - Fix PR #34995 — [compiler] Fix false negatives and add data flow tree to compiler error for no-deriving-state-in-effects
   - PR: https://github.com/facebook/react/pull/34995
   - Code excerpts:
     - compiler/.../ValidateNoDerivedComputationsInEffects_exp.ts: isStateSource flag, finalIsSource, track sources to avoid missed derivations.
     - compiler/.../error.derived-state-conditionally-in-effect.expect.md: Using an effect triggers an additional render... setState call is setting a derived value...

58. Issue #PR34972 — [compiler] Log validation errors instead of throwing (closed 2025-11-10T20:16:14Z)
   - Issue detail: no-derived-computations validation now logs errors via pipeline env instead of throwing, preventing hard crashes while still reporting issues.
   - Issue: PR-only
   - Fix PR #34972 — [compiler] Update ValidateNoDerivedComputationsInEffects_exp to log errors instead of throwing
   - PR: https://github.com/facebook/react/pull/34972
   - Code excerpts:
     - compiler/.../Entrypoint/Pipeline.ts: env.logErrors(validateNoDerivedComputationsInEffects_exp(hir));
     - compiler/.../ValidateNoDerivedComputationsInEffects_exp.ts: import {Result} from '../Utils/Result'; return errors.asResult();

59. Issue #PR34973 — [compiler] Track setState usage by alias/id (closed 2025-11-10T20:16:27Z)
   - Issue detail: setState usage tracking made robust by following aliasing/IDs instead of identifier names, improving correctness of setState analysis.
   - Issue: PR-only
   - Fix PR #34973 — [compiler] Switch to track setStates by aliasing and id instead of identifier names
   - PR: https://github.com/facebook/react/pull/34973
   - Code excerpts:
     - compiler/.../Validation/ValidateNoDerivedComputationsInEffects_exp.ts: setStateLoads/Usages maps now track aliased identifiers and source locations.

60. Issue #PR34472 — [compiler] Disallow unnecessary non-reactive deps in exhaustive deps check (closed 2025-11-21T03:30:35Z)
   - Issue detail: Exhaustive deps validator now rejects extraneous non-reactive deps for consistency, tightening memo/callback dependency checking.
   - Issue: PR-only
   - Fix PR #34472 — [compiler] ValidateExhaustiveDeps disallows unnecessary non-reactive deps
   - PR: https://github.com/facebook/react/pull/34472
   - Code excerpts:
     - compiler/.../CompilerError.ts: handle MemoDependencies category.
     - compiler/.../ValidateExhaustiveDependencies.ts: collapse optional/non-optional paths when checking memo deps.
61. Issue #PR34959 — Update bug report template for eslint plugin label (closed 2025-11-05T21:57:26Z)
   - Issue detail: Update bug report template for eslint plugin label Summary When creating #34957, I noticed a reference to eslint-plugin-react-compiler instead of eslint-plugin-react-hooks. Since the former is merged into the latter (#32416, #34228), I have decided to update the issue template to avoid confusion.
   - Issue: PR-only
   - Fix PR #34959 — Update bug report template for eslint plugin label
   - PR: https://github.com/facebook/react/pull/34959
   - Code excerpts:
     - .github/ISSUE_TEMPLATE/compiler_bug_report.yml: +      - label: eslint-plugin-react-hooks (build issue installing or using the eslint plugin)

62. Issue #PR35042 — [Fiber] SuspenseList with "hidden" tail row should "catch" suspense (closed 2025-11-05T03:11:33Z)
   - Issue detail: [Fiber] SuspenseList with "hidden" tail row should "catch" suspense Normally if you suspend in a SuspenseList row above a Suspense boundary in that row, it'll suspend the parent. Which can itself delay the commit or resuspend a parent boundary. That's because SuspenseList mostly just coordinates the state of the inner boundaries and isn't a boundary itself. However, for tail "hidden" and...
   - Issue: PR-only
   - Fix PR #35042 — [Fiber] SuspenseList with "hidden" tail row should "catch" suspense
   - PR: https://github.com/facebook/react/pull/35042
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberBeginWork.js: +  if (workInProgress.flags & DidCapture) { +    // This is the second pass after having suspended in a row. Proceed directly +    // to the complete phase. +    pushSuspenseListContext(workInProgress
     - packages/react-reconciler/src/ReactFiberCompleteWork.js: +  pushSuspenseListCatch, +function isOnlyNewMounts(tail: Fiber): boolean { +  let fiber: null | Fiber = tail; +  while (fiber !== null) { +    if (fiber.alternate !== null) { +      return false; +  

63. Issue #PR35041 — [eslint] Fix useEffectEvent checks in component syntax (closed 2025-11-04T19:59:29Z)
   - Issue detail: [eslint] Fix useEffectEvent checks in component syntax We were not recording uEE calls in component/hook syntax. Easy fix. Added tests matching function component syntax for component syntax + added one for hooks
   - Issue: PR-only
   - Fix PR #35041 — [eslint] Fix useEffectEvent checks in component syntax
   - PR: https://github.com/facebook/react/pull/35041
   - Code excerpts:
     - packages/eslint-plugin-react-hooks/__tests__/ESLintRulesOfHooks-test.js: +          const onClick = useEffectEvent(() => { +            showNotification(theme); +          }); +          useMyEffect(() => { +            onClick(); +          }); +          useServerEffect(
     - packages/eslint-plugin-react-hooks/src/rules/RulesOfHooks.ts: + +      // @ts-expect-error parser-hermes produces these node types +      ComponentDeclaration(node) { +        // component MyComponent() { const onClick = useEffectEvent(...) } +        recordAllU

64. Issue #PR34961 — [Tracks] Annotate devtools.performanceIssue for Cascading Updates in DEV (closed 2025-11-04T17:07:32Z)
   - Issue detail: [Tracks] Annotate devtools.performanceIssue for Cascading Updates in DEV Summary Updates ReactFiberPerformanceTrack.js to report a Performance Issue (detail.devtools.performanceIssue, see reactwg/react#400, facebook/react-native#54265) when emitting a Cascading Update trace event when __DEV__ is set. This is gated behind a new enablePerformanceIssueReporting flag, enabled for RN only. How did...
   - Issue: PR-only
   - Fix PR #34961 — [Tracks] Annotate devtools.performanceIssue for Cascading Updates in DEV
   - PR: https://github.com/facebook/react/pull/34961
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberPerformanceTrack.js: +  enablePerformanceIssueReporting, +const reusableCascadingUpdateIssue = { +  name: 'React: Cascading Update', +  severity: 'warning', +  description: +    'A cascading update is an update that is tr
     - packages/shared/ReactFeatureFlags.js: +// Enables annotating of React performance track events with `performanceIssue` +// metadata, to more prominently highlight performance issues to users +// (initially, an experimental feature in Reac

65. Issue #PR35039 — [Flight] Fix `hasReadable` flag in Node.js clients' debug channel (closed 2025-11-04T15:30:08Z)
   - Issue detail: [Flight] Fix `hasReadable` flag in Node.js clients' debug channel For Edge Flight servers, that use Web Streams, we're defining the debugChannel option as: debugChannel?: {readable?: ReadableStream, writable?: WritableStream, ...} Whereas for Node.js Flight servers, that use Node.js Streams, we're defining it as: debugChannel?: Readable | Writable | Duplex | WebSocket For the Edge Flight...
   - Issue: PR-only
   - Fix PR #35039 — [Flight] Fix `hasReadable` flag in Node.js clients' debug channel
   - PR: https://github.com/facebook/react/pull/35039
   - Code excerpts:
     - packages/react-server-dom-esm/src/client/ReactFlightDOMClientNode.js: +      ? {hasReadable: true, callback: null}
     - packages/react-server-dom-parcel/src/client/ReactFlightDOMClientNode.js: +      ? {hasReadable: true, callback: null}

66. Issue #PR35036 — [Flight] Fix debug info filtering to include later resolved I/O (closed 2025-11-03T21:59:41Z)
   - Issue detail: [Flight] Fix debug info filtering to include later resolved I/O In #35019, we excluded debug I/O info from being considered for enhancing the owner stack if it resolved after the defined endTime option that can be passed to the Flight client. However, we should include any I/O that was awaited before that end time, even if it resolved later.
   - Issue: PR-only
   - Fix PR #35036 — [Flight] Fix debug info filtering to include later resolved I/O
   - PR: https://github.com/facebook/react/pull/35036
   - Code excerpts:
     - packages/react-client/src/ReactFlightClient.js: +  // Remove any debug info entries after the defined end time. For async info +  // that means we're including anything that was awaited before the end time, +  // but it doesn't need to be resolved 
     - packages/react-server-dom-webpack/src/__tests__/ReactFlightDOMNode-test.js: +      let resolveDynamicData1; +      let resolveDynamicData2; + +      async function getDynamicData1() { +          resolveDynamicData1 = resolve; +      async function getDynamicData2() { +       

67. Issue #PR28491 — Add `React.useActionState` (closed 2024-03-22T17:03:44Z)
   - Issue detail: Add `React.useActionState` Overview Depends on #28514 This PR adds a new React hook called useActionState to replace and improve the ReactDOM useFormState hook. Motivation This hook intends to fix some of the confusion and limitations of the useFormState hook. The useFormState hook is only exported from the ReactDOM package and implies that it is used only for the state of <form> actions,...
   - Issue: PR-only
   - Fix PR #28491 — Add `React.useActionState`
   - PR: https://github.com/facebook/react/pull/28491
   - Code excerpts:
     - packages/react-debug-tools/src/ReactDebugHooks.js: +      if (typeof Dispatcher.useActionState === 'function') { +        // This type check is for Flow only. +        Dispatcher.useActionState((s: mixed, p: mixed) => s, null); +      } +function useA
     - packages/react-dom/src/__tests__/ReactDOMFizzForm-test.js: +let useActionState; +    if (__VARIANT__) { +      // Remove after API is deleted. +      useActionState = require('react-dom').useFormState; +    } else { +      useActionState = require('react').us

68. Issue #PR35019 — [Fizz] Push halted await to the owner stack for late-arriving I/O info (closed 2025-11-01T15:03:09Z)
   - Issue detail: [Fizz] Push halted await to the owner stack for late-arriving I/O info To quote from #33634: If an aborted task is not rendering, then this is an async abort. Conceptually it's as if the abort happened inside the async gap. The abort reason's stack frame won't have that on the stack so instead we use the owner stack and debug task of any halted async debug info. This PR extends that logic to...
   - Issue: PR-only
   - Fix PR #35019 — [Fizz] Push halted await to the owner stack for late-arriving I/O info
   - PR: https://github.com/facebook/react/pull/35019
   - Code excerpts:
     - packages/react-client/src/ReactFlightClient.js: +  _debugEndTime?: number, // DEV-only +function filterDebugInfo( +  response: Response, +  value: {_debugInfo: ReactDebugInfo, ...}, +) { +  if (response._debugEndTime === null) { +    // No end time
     - packages/react-server-dom-esm/src/client/ReactFlightDOMClientBrowser.js: +  endTime?: number, +    __DEV__ && options && options.endTime != null ? options.endTime : undefined,

69. Issue #PR34929 — [DevTools] Reset forced states when changing component filters (closed 2025-10-31T11:57:11Z)
   - Issue detail: [DevTools] Reset forced states when changing component filters When we change component filters, we unmount the whole tree and mount it again. That means that any Suspense rect measurement will be gone. On mount, we're not measuring Suspense nodes since there's nothing to measure. Users can't even get back the original state since we no longer know which Fibers we forced a fallback for. Now...
   - Issue: PR-only
   - Fix PR #34929 — [DevTools] Reset forced states when changing component filters
   - PR: https://github.com/facebook/react/pull/34929
   - Code excerpts:
     - packages/react-devtools-shared/src/__tests__/setupTests.js: +  const maybeError = args[1]; +  if ( +    maybeError !== null && +    typeof maybeError === 'object' && +    maybeError.message === 'Simulated error coming from DevTools' +  ) { +    // Error from f
     - packages/react-devtools-shared/src/__tests__/storeComponentFilters-test.js: +  let agent; +    agent = global.agent; + +  // @reactVersion >= 16.6 +  it('resets forced error and fallback states when filters are changed', async () => { +    store.componentFilters = []; +    cl

70. Issue #PR35005 — [Flight] Cache the value if we visit the same I/O or Promise multiple times along different paths (closed 2025-10-29T14:55:43Z)
   - Issue detail: [Flight] Cache the value if we visit the same I/O or Promise multiple times along different paths We avoid visiting the same async node twice but if we see it again we returned "null" indicating that there's no I/O there. This means that if you have two different Promises both resolving from the same I/O node then we only show one of them. However, in general we treat that as two different I/O...
   - Issue: PR-only
   - Fix PR #35005 — [Flight] Cache the value if we visit the same I/O or Promise multiple times along different paths
   - PR: https://github.com/facebook/react/pull/35005
    - Code excerpts:
      - packages/react-server/src/ReactFlightServer.js: +  visited: Map< +    AsyncSequence | ReactDebugInfo, +    void | null | PromiseNode | IONode, +  >, +    return visited.get(node); +  } +  // Set it as visited early in case we see ourselves before r

71. Issue #35040 — Bug: Getting `Cannot access refs during render` error from event handler. (closed 2025-11-14T17:00:35Z)
   - Issue detail: So on react official documentations, I found, it recommend to avoid direct read or write during render on ref. Here is the docs link (under pitfall)- https://react.dev/reference/react/useRef And here I also found that ref is safe to use on event handler or effect. `You can read or write refs from event handlers or effects instead.` So, we can read `ref.current` from a onSubmit handler as it is...
   - Issue: https://github.com/facebook/react/issues/35040
   - Fix PR #35062 — [compiler] Allow ref access in callbacks passed to event handler props
   - PR: https://github.com/facebook/react/pull/35062
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/HIR/Environment.ts: + +  /** +   * Enables inference of event handler types for JSX props on built-in DOM elements. +   * When enabled, functions passed to event handler props (props starting with "on") +   * on primitiv
     - compiler/packages/babel-plugin-react-compiler/src/HIR/Globals.ts: +  BuiltInEffectEventId, +          shapeId: BuiltInEffectEventId,
     - compiler/packages/babel-plugin-react-compiler/src/HIR/ObjectShape.ts: +const BuiltInEventHandlerId = 'BuiltInEventHandlerId';
     - compiler/packages/babel-plugin-react-compiler/src/TypeInference/InferTypes.ts: +      if (env.config.enableInferEventHandlers) { +        if ( +          value.kind === 'JsxExpression' && +          value.tag.kind === 'BuiltinTag' && +          !value.tag.name.includes('-') +        ) { +          /* +           * Infer event handler types for built-in DOM elements. +           * Props starting with "on" (e.g., onClick, onSubmit) on primitive tags +           * are inferred as event handlers. This allows functions with ref access +           * to be passed to these props, since DOM event handlers are guaranteed +           * by React to only execute in response to events, never during render. +           * +           * We exclude tags with hyphens to avoid web components (custom elements), +           * which are required by the HTML spec to contain a hyphen. Web components +           * may call event handler props during their lifecycle methods (e.g., +           * connectedCallback), which would be unsafe for ref access. +           */ +          for (const prop of value.props) { +            if ( +              prop.kind === 'JsxAttribute' && +              prop.name.startsWith('on') && +              prop.name.length > 2 && +              prop.name[2] === prop.name[2].toUpperCase() +            ) { +              yield equation(prop.place.identifier.type, { +                kind: 'Function', +                shapeId: BuiltInEventHandlerId, +                return: makeType(), +                isConstructor: false, +              }); +            } +          } +        } +      }
     - compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateNoRefAccessInRender.ts: +function isEventHandlerType(identifier: Identifier): boolean { +  const type = identifier.type; +  return type.kind === 'Function' && type.shapeId === BuiltInEventHandlerId; +} +              const isEventHandlerLValue = isEventHandlerType( +                instr.lvalue.identifier, +              ); +              for (const operand of eachInstructionValueOperand(instr.value)) { +                /** +                 * By default we check that function call operands are not refs, +                 * but there are some exceptions. +                 */ +                if ( +                  isRefLValue || +                  isEventHandlerLValue || +                  (hookKind != null && +                    hookKind !== 'useState' && +                    hookKind !== 'useReducer') +                ) { +                  /** +                   * Allow passing refs or ref-accessing functions when: +                   * 1. lvalue is a ref (mergeRefs pattern: `mergeRefs(ref1, ref2)`) +                   * 2. lvalue is an event handler (DOM events execute outside render) +                   * 3. calling hooks (independently validated for ref safety) +                   */ +                  validateNoDirectRefValueAccess(errors, operand, env); +                } else if (interpolatedAsJsx.has(instr.lvalue.identifier.id)) {

72. Issue #30368 — Bug: useFormStatus pending state is reset when component state is updated. (closed 2025-11-19T17:22:08Z)
   - Issue detail: If you have a component that relies on the `pending` return value of `useFormStatus`, the `pending` state will incorrectly reset to `false` if the component is updated due to a `useState` update. This does not happen if the `useState` hook is placed in a child component. React version: 19.0.0-rc-512b09b2-20240718 ## Steps To Reproduce [codesandbox.io/p/sandbox/react-useformstatus-pending-reset-on-unrelated-state-update-m59zw8](https://codesandbox.io/p/sandbox/react-useformstatus-pending-reset-on-unrelated-state-update-m59zw8) 1. Create a react app that uses form actions (this uses NextJS starter code) 2. Have the form action delay for a set period of time before resolving 3. Create a child component that uses `useFormStatus().pending`. Have the component also use a `useState` hook that updates on an interval using `useEffect`. 4. Place this child component as a child of the `<form />` element 5. Verify that `useFormStatus().pending` is reset to false as soon as a call to `setState` happns Example component ``` export default function SubmissionState() { const formStatus = useFormStatus(); const [counter, setCounter] = useState(0); useEffect(() => { const id = setTimeout(() => { if (!formStatus.pending) { setCounter(0); return; } setCounter(counter + 1); }, 1000); return () => clearTimeout(id); }, [counter, formStatus.pending]); return ( <div> {formStatus.pending ? `Pending for ${counter} seconds` : \"Not pending\"} </div> ); } ``` this example works as expected, `useFormStatus().pending` state matches the server actions state ``` function SubmissionStateBody({ pending }: { pending: boolean }) { const [counter, setCounter] = useState(0); useEffect(() => { if (!pending) { setCounter(0); return; } const id = setTimeout(() => { setCounter(counter + 1); }, 1000); return () => clearTimeout(id); }, [counter, pending]); return ( <div>{pending ? `Pending for ${counter} seconds` : \"Not pending\"}</div> ); } export default function SubmissionStateCorrect() { const formStatus = useFormStatus(); return <SubmissionStateBody pending={formStatus.pending} />; } ``` Link to code example: [Github repro using nextjs starter template](https://github.com/jatwood/repro-use-form-issue) ## The current behavior The UI shows the submission as pending for the length of the server action. ## The expected behavior The UI shows the submission as not-pending as soon as the counter is updated.
   - Issue: https://github.com/facebook/react/issues/30368
   - Fix PR #34075 — Fix form status reset when component state is updated
   - PR: https://github.com/facebook/react/pull/34075
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberHostContext.js: +function pushHostContext(fiber: Fiber): void { +  const stateHook: Hook | null = fiber.memoizedState; +  if (stateHook !== null) { +    // Propagate the current state to all the descendents. +    // We use Context as an implementation detail for this. +    // +    // NOTE: This assumes that there cannot be nested transition providers, +    // because the only renderer that implements this feature is React DOM, +    // and forms cannot be nested. If we did support nested providers, then +    // we would need to push a context value even for host fibers that +    // haven't been upgraded yet. +    const transitionStatus: TransitionStatus = stateHook.memoizedState; +    if (isPrimaryRenderer) { +      HostTransitionContext._currentValue = transitionStatus; +    } else { +      HostTransitionContext._currentValue2 = transitionStatus; +    } +    // Only provide context if this fiber has been upgraded by a host +    // transition. We use the same optimization for regular host context below. +    push(hostTransitionProviderCursor, fiber, fiber); +  } +}
     - packages/react-dom/src/__tests__/ReactDOMForm-test.js: +  it('form actions should retain status when nested state changes', async () => { +    const formRef = React.createRef(); +    let rerenderUnrelatedStatus; +    function UnrelatedStatus() { +      const {pending} = useFormStatus(); +      const [counter, setCounter] = useState(0); +      rerenderUnrelatedStatus = () => setCounter(n => n + 1); +      Scheduler.log(`[unrelated form] pending: ${pending}, state: ${counter}`); +    } +    let rerenderTargetStatus; +    function TargetStatus() { +      const {pending} = useFormStatus(); +      const [counter, setCounter] = useState(0); +      Scheduler.log(`[target form] pending: ${pending}, state: ${counter}`); +      rerenderTargetStatus = () => setCounter(n => n + 1); +    } +    function App() { +      async function action() { +        return new Promise(resolve => { +          // never resolves +        }); +      } +      return ( +        <> +          <form action={action} ref={formRef}> +            <input type="submit" /> +            <TargetStatus /> +          </form> +          <form> +            <UnrelatedStatus /> +          </form> +        </> +      ); +    } +    const root = ReactDOMClient.createRoot(container); +    await act(() => root.render(<App />)); +    assertLog([ +      '[target form] pending: false, state: 0', +      '[unrelated form] pending: false, state: 0', +    ]); +    await submit(formRef.current); +    assertLog(['[target form] pending: true, state: 0']); +    await act(() => rerenderTargetStatus()); +    assertLog(['[target form] pending: true, state: 1']); +    await act(() => rerenderUnrelatedStatus()); +    assertLog(['[unrelated form] pending: false, state: 1']); +  });

74. Issue #34328 — Update CodeSandbox CI to Node 20 to match .nvmrc (closed 2025-08-28T22:33:13Z)
   - Issue detail: ### Website or app  https://github.com/facebook/react  ### Repro steps  1. Check the repository’s `.nvmrc` file — it specifies Node 20. 2. Check `.codesandbox/ci.json` — it currently specifies Node 18. 3. This mismatch may cause builds in CodeSandbox CI to use an older Node version than intended.  ### How often does this bug happen?  Every time  ### DevTools package (automated)  _No response_  ### DevTools version (automated)  _No response_  ### Error message (automated)  _No response_  ### Erro
   - Issue: https://github.com/facebook/react/issues/34328
   - Fix PR #34329 — Update Code Sandbox CI to Node 20 to Match .nvmrc
   - PR: https://github.com/facebook/react/pull/34329
   - Code excerpts:
     - .codesandbox/ci.json:   "node": "20",

75. Issue #34679 — Bug: eslint-plugin-react-hooks v.6.1.0 recommended config uses array instead of object (closed 2025-10-02T22:52:53Z)
   - Issue detail: Not sure if this is technically a bug, or just a convention choice.  It's not possible to use the recommended config directly in a flat eslint config array in version 6.1.0  The `recommended-latest` config (now deprecated) will work, but the new `recommended` config will not.  The plugin is defined as:  ``` Object.assign(plugin.configs, {     'recommended-legacy': {         plugins: ['react-hooks'],         rules: ruleConfigs,     },     'flat/recommended': [         {             plugins: {
   - Issue: https://github.com/facebook/react/issues/34679
   - Fix PR #34700 — [eprh] Fix `recommended` config for flat config compatibility
   - PR: https://github.com/facebook/react/pull/34700
   - Code excerpts:
     - fixtures/eslint-v6/.eslintrc.json:   "extends": ["plugin:react-hooks/recommended-latest-legacy"],
     - fixtures/eslint-v6/index.js: 
/**
 * Compiler Rules
 */
// Invalid: component factory
function InvalidComponentFactory() {
  const DynamicComponent = () => <div>Hello</div>;
  // eslint-disable-next-line react-hooks/static-compon

76. Issue #34311 — [Compiler Bug]: errors when the `this` type is declared in a function (closed 2025-08-27T21:58:45Z)
   - Issue detail: ### What kind of issue is this?  - [ ] React Compiler core (the JS output is incorrect, or your app works incorrectly after optimization) - [x] babel-plugin-react-compiler (build issue installing or using the Babel plugin) - [ ] eslint-plugin-react-compiler (build issue installing or using the eslint plugin) - [ ] react-compiler-healthcheck (build issue installing or using the healthcheck script)  ### Link to repro  https://playground.react.dev/#N4Igzg9grgTgxgUxALhAHQHYIB4AcIwAuABAGZQZyECWEGxUYC
   - Issue: https://github.com/facebook/react/issues/34311
   - Fix PR #34322 — [compiler] Emit better error for unsupported syntax `this`
   - PR: https://github.com/facebook/react/pull/34322
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/HIR/HIRBuilder.ts:     if (node.name === 'this') {
      CompilerError.throwDiagnostic({
        severity: ErrorSeverity.UnsupportedJS,
        category: ErrorCategory.UnsupportedSyntax,
        reason: '`this` is not s
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/ecma/error.reserved-words.expect.md: Error: `this` is not supported syntax

React Compiler does not support compiling functions that use `this`

error.reserved-words.ts:8:28
   6 |
   7 |   if (ref.current === null) {
>  8 |     ref.curr

77. Issue #33978 — [Compiler Bug]: Component defined inside function cause incorrect optimization (closed 2025-08-27T17:59:27Z)
   - Issue detail: ### What kind of issue is this?  - [x] React Compiler core (the JS output is incorrect, or your app works incorrectly after optimization) - [ ] babel-plugin-react-compiler (build issue installing or using the Babel plugin) - [ ] eslint-plugin-react-compiler (build issue installing or using the eslint plugin) - [ ] react-compiler-healthcheck (build issue installing or using the healthcheck script)  ### Link to repro  https://playground.react.dev/#N4Igzg9grgTgxgUxALhASwLYAcIwC4AEASggIZyEBmMEGBA5DG
   - Issue: https://github.com/facebook/react/issues/33978
   - Fix PR #34305 — [compiler] Validate against component/hook factories
   - PR: https://github.com/facebook/react/pull/34305
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/CompilerError.ts:   // Checking for higher order functions acting as factories for components/hooks
  Factories = 'Factories',

    case ErrorCategory.Factories: {
      return {
        category,
        name: 'compon
     - compiler/packages/babel-plugin-react-compiler/src/Entrypoint/Program.ts:     // In 'all' mode, compile only top level functions
    if (
      pass.opts.compilationMode === 'all' &&
      fn.scope.getProgramParent() !== fn.scope.parent
    ) {
      return;
    }


    if 

78. Issue #32316 — [Flight] Resolve deduped references when chunks are blocked on each other (closed 2025-06-29T14:56:17Z)
   - Issue detail: This PR includes a reduced test case of https://github.com/vercel/next.js/pull/75726:
 
 ```jsx
 function Server() {
   const shared = {id: 42};
   const map = new Map([[42, shared]]);
 
   return <ClientComponent shared={shared} map={map} />;
 }
 ```
 
 This is serialized into the following RSC payload which the Flight Client was not able to resolve, because two chunks are blocked on each other:
 
 ```
 1:I["0",[],"*"]
 2:[[42,"$0:props:shared"]]
 0:["$","$L1",null,{"shared":{"id":42},"map":"$Q
   - Issue: https://github.com/facebook/react/pull/32316
   - Fix PR #33664 — [Flight] Resolve Deep Cycles
   - PR: https://github.com/facebook/react/pull/33664
   - Code excerpts:
     - packages/react-client/src/ReactFlightClient.js:   value: null | Array<InitializationReference | (T => mixed)>,
  reason: null | Array<InitializationReference | (mixed => mixed)>,
  value: null | Array<InitializationReference | (T => mixed)>,
  reas
     - packages/react-server-dom-webpack/src/__tests__/ReactFlightDOMBrowser-test.js: 
  it('should resolve deduped references in maps used in client component props', async () => {
    const ClientComponent = clientExports(function ClientComponent({
      shared,
      map,
    }) {
 

79. Issue #33577 — [Compiler Bug]: Compiler tries to assign to variables that does not exist (closed 2025-06-25T18:10:10Z)
   - Issue detail: ### What kind of issue is this?  - [x] React Compiler core (the JS output is incorrect, or your app works incorrectly after optimization) - [ ] babel-plugin-react-compiler (build issue installing or using the Babel plugin) - [ ] eslint-plugin-react-compiler (build issue installing or using the eslint plugin) - [ ] react-compiler-healthcheck (build issue installing or using the healthcheck script)  ### Link to repro  https://playground.react.dev/#N4Igzg9grgTgxgUxALhASwLYAcIwC4AEwBUYCASgmGgF4IDyAR
   - Issue: https://github.com/facebook/react/issues/33577
   - Fix PR #33624 — [compiler] Fix bug with reassigning function param in destructuring
   - PR: https://github.com/facebook/react/pull/33624
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/CodegenReactiveFunction.ts:     const place = param.kind === 'Identifier' ? param : param.place;
    cx.temp.set(place.identifier.declarationId, null);
    cx.declare(place.identifier);
     - compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/ExtractScopeDeclarationsFromDestructuring.ts:   for (const param of fn.params) {
    const place = param.kind === 'Identifier' ? param : param.place;
    state.declared.add(place.identifier.declarationId);
  }

80. Issue #32915 — [Compiler Bug]: Unicode characters handled incorrectly (closed 2025-08-19T16:36:05Z)
   - Issue detail: ### What kind of issue is this?  - [x] React Compiler core (the JS output is incorrect, or your app works incorrectly after optimization) - [ ] babel-plugin-react-compiler (build issue installing or using the Babel plugin) - [ ] eslint-plugin-react-compiler (build issue installing or using the eslint plugin) - [ ] react-compiler-healthcheck (build issue installing or using the healthcheck script)  ### Link to repro  https://playground.react.dev/#N4Igzg9grgTgxgUxALhAgHgBwjALgAgBMEAzAQygBsCSoA7OXA
   - Issue: https://github.com/facebook/react/issues/32915
   - Fix PR #33096 — [compiler] Fix for string attribute values with emoji
   - PR: https://github.com/facebook/react/pull/33096
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/CodegenReactiveFunction.ts:  *
 * u010000 to u10FFFF: Astral plane characters
 * https://mathiasbynens.be/notes/javascript-unicode
  /[\u{0000}-\u{001F}\u{007F}\u{0080}-\u{FFFF}\u{010000}-\u{10FFFF}]|"|\\/u;
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/jsx-string-attribute-expression-container.expect.md:       <Text value={'welcome 👋'} />
        <Text value={"welcome \uD83D\uDC4B"} />
</span><span>A	E</span><span>나은</span><span>Lauren</span><span>சத்யா</span><span>Sathya</span><span>welcome 👋</span><

81. Issue #21856 — [DevTools] Show which hooks (names) changed in the Profiler (closed 2025-04-15T10:10:01Z)
   - Issue detail: Hooks are the preferred way for writing stateful React components, but there are a few things about them that still lag behind the class component API: profiling (since DevTools just shows “hooks changed” rather than which ones changed).
 
 Building on top of the initial named hooks release _and_ the experimental `enableProfilerChangedHookIndices` feature flag, the Profiler should show the “names” of hooks that changed between renders. (Because this would be expensive to eagerly calculate, we wo
   - Issue: https://github.com/facebook/react/issues/21856
   - Fix PR #31398 — [DevTools] feat: show changed hooks names in the Profiler tab
   - PR: https://github.com/facebook/react/pull/31398
   - Code excerpts:
     - packages/react-devtools-shared/src/devtools/views/Components/Components.js:                   <InspectedElement />
     - packages/react-devtools-shared/src/devtools/views/DevTools.js: import {InspectedElementContextController} from './Components/InspectedElementContext';
                            <InspectedElementContextController>
                              <ThemeProvider>
  

82. Issue #32494 — Bug [`eslint-plugin-react-hooks`]: `Config (unnamed): Key "plugins": This appears to be in eslintrc format (array of strings) rather than flat config format (object).` (closed 2025-03-02T12:38:18Z)
   - Issue detail: <!--   Please provide a clear and concise description of what the bug is. Include   screenshots if needed. Please test using the latest version of the relevant   React packages to make sure your issue has not already been fixed. -->  React version: 19.0.0 eslint-plugin-react-hooks: 5.2.0  ## Steps To Reproduce  1. Follow installation instruction for flat config: https://github.com/facebook/react/tree/HEAD/packages/eslint-plugin-react-hooks#installation  <!--   Your bug will get fixed much faster
   - Issue: https://github.com/facebook/react/issues/32494
   - Fix PR #32498 — docs(eslint-plugin-react-hooks): clarify config details for prior versions
   - PR: https://github.com/facebook/react/pull/32498
   - Code excerpts:
     - packages/eslint-plugin-react-hooks/README.md: #### 5.2.0

For users of 5.2.0 (the first version with flat config support), add the `recommended-latest` config.
  reactHooks.configs['recommended-latest'],
#### >= 5.2.0

If you are still using ESLi

83. Issue #28313 — eslint-plugin-react-hooks & "Flat Config" (ESLint 9) (closed 2025-01-16T23:39:12Z)
   - Issue detail: 👋 Coming over from https://github.com/eslint/eslint/issues/18093: ESLint is migrating to a [new "flat config" format](https://eslint.org/docs/latest/use/configure/configuration-files-new) that will be the default in ESLint v9.
 
 It doesn't look like `eslint-plugin-react-hooks` has documented support yet. But, based on searching around (e.g. https://github.com/vercel/next.js/discussions/49337), ESLint v9 is _basically_ supported if you wire it up manually in your config:
 
 ```js
 // eslint.conf
   - Issue: https://github.com/facebook/react/issues/28313
   - Fix PR #30774 — feat(eslint-plugin-react-hooks): support flat config
   - PR: https://github.com/facebook/react/pull/30774
   - Code excerpts:
     - packages/eslint-plugin-react-hooks/README.md: ### Legacy Config (.eslintrc)

If you are still using ESLint below 9.0.0, please continue to use `recommended-legacy`. To avoid breaking changes, we still support `recommended` as well, but note that 
     - packages/eslint-plugin-react-hooks/src/index.js: const {name, version} = require('../package.json');
// All rules

// Config rules
const configRules = {
  'react-hooks/rules-of-hooks': 'error',
  'react-hooks/exhaustive-deps': 'warn',
};

// Legacy 

84. Issue #30119 — [eslint-plugin-react-hooks] Missing type declarations (closed 2025-02-16T19:10:55Z)
   - Issue detail: <ins>Versions:</ins> all
 
 <ins>Severity:</ins> low
 
 ## What
 
 When imported in a TypeScript environment, `eslint-plugin-react-hooks` throws a "missing type declarations" error.
 
 ![image](https://github.com/facebook/react/assets/28303477/fbb4a4fb-2db6-4d1a-aeba-0e73add1e507)
 
 ## Why
 
 This is because `eslint-plugin-react-hooks` does not have any type declarations bundled in the package. These would usually be in an `index.d.ts` file.
 
 Also, `eslint-plugin-react-hooks` does not have a
   - Issue: https://github.com/facebook/react/issues/30119
   - Fix PR #32240 — feat(eslint-plugin-react-hooks): convert to typescript and package type declarations
   - PR: https://github.com/facebook/react/pull/32240
   - Code excerpts:
     - packages/eslint-plugin-react-hooks/babel.config.js: /**
 * This file is purely being used for local jest runs, and doesn't participate in the build process.
 */
'use strict';

module.exports = {
  extends: '../../babel.config-ts.js',
};
     - packages/eslint-plugin-react-hooks/index.js: module.exports = require('./src/index.ts');

85. Issue #31422 — [DevTools Bug]: Copy to clipboard doesn't work (closed 2025-01-15T18:41:23Z)
   - Issue detail: ### Website or app  https://www.arbounie.nl/  ### Repro steps  1. Open the devtools to the Components tab
 2. Select a component. I used the first Context.Provider, but I suspect it doesn't matter.
 3. In the `props` panel, click the top-right "copy to clipboard" icon.
 4. Observe what gets put into the clipboard.  ### How often does this bug happen?  Every time  ### DevTools package (automated)  _No response_  ### DevTools version (automated)  _No response_  ### Error message (automated)  _No r
   - Issue: https://github.com/facebook/react/issues/31422
   - Fix PR #32077 — Fix copy functionality in Firefox
   - PR: https://github.com/facebook/react/pull/32077
   - Code excerpts:
     - packages/react-devtools-extensions/chrome/manifest.json:     "tabs",
    "clipboardWrite"
     - packages/react-devtools-extensions/edge/manifest.json:     "tabs",
    "clipboardWrite"

86. Issue #31977 — [DevTools Bug]: React DevTools Profiler freezes after recording multiple events (closed 2025-01-14T20:23:43Z)
   - Issue detail: ### Website or app  localhost  ### Repro steps  I'm experiencing an issue with React DevTools while debugging a project locally. Here are the steps to reproduce the issue:
 
 1. Open React DevTools and navigate to the Profiler tab.
 2. Start a recording by clicking on "Start Profiling," then stop it by clicking on "Stop Profiling."
 3. View the recording results without any issues.
 4. Attempt to start a new recording by clicking on "Start Profiling" again.
 5. After a few moments, the Profiler
   - Issue: https://github.com/facebook/react/issues/31977
   - Fix PR #32066 — [DevTools] Prevent crash when starting consecutive profiling sessions
   - PR: https://github.com/facebook/react/pull/32066
   - Code excerpts:
     - packages/react-devtools-shared/src/devtools/ProfilerStore.js:     this.clear();


87. Issue #31679 — [DevTools Bug]: Profiler stuck and crash (closed 2025-01-14T20:23:44Z)
   - Issue detail: ### Website or app
 
 Any dev or profiling build of React v16.5+, ie. https://zi8n3.csb.app/
 
 ### Repro steps
 
 Part 1 (Stuck):
 1. open profiler in react dev tools
 2. click record button
 3. do any action on the web page (click button or input, etc)
 4. click stop record button
 5. click record button again
 
 Then you can see the profiler is stuck.
 
 Part 2 (Crash):
 6. continue from the above steps
 7. close Chrome console
 8. open the Chrome console again
 
 Will see the components and
   - Issue: https://github.com/facebook/react/issues/31679
   - Fix PR #32066 — [DevTools] Prevent crash when starting consecutive profiling sessions
   - PR: https://github.com/facebook/react/pull/32066
   - Code excerpts:
     - packages/react-devtools-shared/src/devtools/ProfilerStore.js:     this.clear();


88. Issue #32014 — [Compiler Bug]: Playground doesn't display compiler violations (closed 2025-01-09T17:21:08Z)
   - Issue detail: ### What kind of issue is this?  - [ ] React Compiler core (the JS output is incorrect, or your app works incorrectly after optimization) - [ ] babel-plugin-react-compiler (build issue installing or using the Babel plugin) - [ ] eslint-plugin-react-compiler (build issue installing or using the eslint plugin) - [ ] react-compiler-healthcheck (build issue installing or using the healthcheck script)  ### Link to repro  https://playground.react.dev/#N4Igzg9grgTgxgUxALhASwLYAcIwC4AEwBUYCASggGYEC+BVME
   - Issue: https://github.com/facebook/react/issues/32014
   - Fix PR #32035 — [playground] Partially revert #32009
   - PR: https://github.com/facebook/react/pull/32035
   - Code excerpts:
     - compiler/apps/playground/components/Editor/EditorImpl.tsx:     panicThreshold: 'all_errors',

89. Issue #31864 — [Compiler Bug]: Linter complains about ref `current` access during render when returning array with Typescript's `as const` (closed 2024-12-20T16:56:49Z)
   - Issue detail: ### What kind of issue is this?  - [ ] React Compiler core (the JS output is incorrect, or your app works incorrectly after optimization) - [ ] babel-plugin-react-compiler (build issue installing or using the Babel plugin) - [X] eslint-plugin-react-compiler (build issue installing or using the eslint plugin) - [ ] react-compiler-healthcheck (build issue installing or using the healthcheck script)  ### Link to repro  https://playground.react.dev/#N4Igzg9grgTgxgUxALhASwLYAcIwC4AEwBUYCAwgIYA21ARpXA
   - Issue: https://github.com/facebook/react/issues/31864
   - Fix PR #31871 — [compiler] Allow type cast expressions with refs
   - PR: https://github.com/facebook/react/pull/31871
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/Validation/ValidateNoRefAccesInRender.ts:           case 'TypeCastExpression': {
            env.set(
              instr.lvalue.identifier.id,
              env.get(instr.value.value.identifier.id) ??
                refTypeOfType(instr.lval
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/allow-ref-type-cast-in-render.expect.md: 
## Input

```javascript
import {useRef} from 'react';

function useArrayOfRef() {
  const ref = useRef(null);
  const callback = value => {
    ref.current = value;
  };
  return [callback] as const;

90. Issue #31603 — [compiler] Prune all unused array destructure items during DCE (closed 2024-11-22T21:00:00Z)
   - Issue detail: Stack from [ghstack](https://github.com/ezyang/ghstack) (oldest at bottom): * #31604 * __->__ #31603  We didn't originally support holes within array patterns, so DCE was only able to prune unused items from the end of an array pattern. Now that we support holes we can replace any unused item with a hole, and then just prune the items to the last identifier/spread entry.  Note: this was motivated by finding useState where either the state or setState go unused — both are strong indications that
   - Issue: https://github.com/facebook/react/pull/31603
   - Fix PR #31619 — [compiler] Prune all unused array destructure items during DCE
   - PR: https://github.com/facebook/react/pull/31619
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/Optimization/DeadCodeElimination.ts:          * For arrays, we can prune items prior to the end by replacing
         * them with a hole. Items at the end can simply be dropped.
        let lastEntryIndex = 0;
        const items = instr
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/concise-arrow-expr.expect.md:   const [, setX] = useState(0);

91. Issue #26113 — [Fizz] Add failing test for failed hydration when using uSES in StrictMode (closed 2023-05-12T21:18:05Z)
   - Issue detail: ## Summary
 
 Failing test for https://github.com/facebook/react/issues/26095
 
 ## How did you test this change?
 
 - `yarn test ReactDOMFizzServer-test`
   - Issue: https://github.com/facebook/react/pull/26113
   - Fix PR #26791 — Fix uSES hydration in strict mode
   - PR: https://github.com/facebook/react/pull/26791
   - Code excerpts:
     - packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js: let ReactDOM;
    ReactDOM = require('react-dom');
  it('can hydrate uSES in StrictMode with different client and server snapshot (sync)', async () => {
    function subscribe() {
      return () => {
     - packages/react-reconciler/src/ReactFiberHooks.js:   let nextSnapshot;
  const isHydrating = getIsHydrating();
  if (isHydrating) {
    // Needed for strict mode double render
    if (getServerSnapshot === undefined) {
      throw new Error(
        '

92. Issue #25650 — Fork updateSyncExternalStore impl in update and rerender (closed 2023-05-12T21:18:06Z)
   - Issue detail: ## Summary
 
 Follow-up to https://github.com/facebook/react/pull/25578.
 
 Applied the same pattern as used in  `useDeferredValue` implementations.
 
 ## How did you test this change?
 
 - [x] `yarn test`
 - [x] CI
   - Issue: https://github.com/facebook/react/pull/25650
   - Fix PR #26791 — Fix uSES hydration in strict mode
   - PR: https://github.com/facebook/react/pull/26791
   - Code excerpts:
     - packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js: let ReactDOM;
    ReactDOM = require('react-dom');
  it('can hydrate uSES in StrictMode with different client and server snapshot (sync)', async () => {
    function subscribe() {
      return () => {
     - packages/react-reconciler/src/ReactFiberHooks.js:   let nextSnapshot;
  const isHydrating = getIsHydrating();
  if (isHydrating) {
    // Needed for strict mode double render
    if (getServerSnapshot === undefined) {
      throw new Error(
        '

93. Issue #29720 — fix<compiler>: only call readTestFilter if the filter option is enabled (closed 2024-06-03T23:09:58Z)
   - Issue detail: <!--
   Thanks for submitting a pull request!
   We appreciate you spending the time to work on these changes. Please provide enough information so that others can review your pull request. The three fields below are mandatory.
 
   Before submitting a pull request, please make sure the following is done:
 
   1. Fork [the repository](https://github.com/facebook/react) and create your branch from `main`.
   2. Run `yarn` in the repository root.
   3. If you've fixed a bug or added code that shou
   - Issue: https://github.com/facebook/react/pull/29720
   - Fix PR #29775 — fix<compiler>: reread the testfilter file if filter enabled during the watch process
   - PR: https://github.com/facebook/react/pull/29775
   - Code excerpts:
     - compiler/packages/snap/src/runner-watch.ts:   process.stdin.on("keypress", async (str, key) => {
      state.filter = state.mode.filter ? await readTestFilter() : null;

94. Issue #28923 — [React 19] useTransition()'s pending state does not go back to false (revision 94eed63c49-20240425) (closed 2024-05-31T21:52:48Z)
   - Issue detail: ## Summary
 
 I am excited to start using React v19 as it has so many features and QoL improvements I've been waiting for!
 
 There is a bug (new bug comparing to v18.2.0) that I found while reproducing https://github.com/facebook/react/issues/26814. When using `useTransition()` with `use()`, `pending` flag of transition correctly becomes `true` in the beginning, but doesn't go back to `false` after transition is complete, which means any pending state artifacts in the UI remain visible.
 
 Repo
   - Issue: https://github.com/facebook/react/issues/28923
   - Fix PR #29670 — Fix: `useTransition` after `use` gets stuck in pending state
   - PR: https://github.com/facebook/react/pull/29670
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberHooks.js: 
  // When something suspends with `use`, we replay the component with the
  // "re-render" dispatcher instead of the "mount" or "update" dispatcher.
  //
  // But if there are additional hooks that o
     - packages/react-reconciler/src/__tests__/ReactUse-test.js: let useTransition;
    useTransition = React.useTransition;

  it(
    'regression: does not get stuck in pending state after `use` suspends ' +
      '(when `use` comes before all hooks)',
    async 

95. Issue #29617 — Compiler String Concat Constant Propagation (closed 2024-05-28T23:15:47Z)
   - Issue detail: Consider the following constant propagation:
 
 Input:
 ```ts
 function foo() {
   const a = "a" + "b";
   const c = "c";
   return a + c;
 }
 ```
 Output:
 ```ts
 function foo() {
   return "abc";
 }
 ```
 
 Is this in scope for the react compiler? If so, is it open for contributions?
   - Issue: https://github.com/facebook/react/issues/29617
   - Fix PR #29621 — feat(compiler): Implement constant string concat propagation
   - PR: https://github.com/facebook/react/pull/29621
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/Optimization/ConstantPropagation.ts:             } else if (typeof lhs === "string" && typeof rhs === "string") {
              result = { kind: "Primitive", value: lhs + rhs, loc: value.loc };
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/constant-propagation-string-concat.expect.md: 
## Input

```javascript
function foo() {
  const a = "a" + "b";
  const c = "c";
  return a + c;
}

export const FIXTURE_ENTRYPOINT = {
  fn: foo,
  params: [],
  isComponent: false,
};

```

## Code

96. Issue #29649 — [compiler] Add more arithmetic binary expressions to constant propagation (closed 2024-05-29T17:35:20Z)
   - Issue detail: There are already most arithmetic operators in constant propagation: `+`, `-`, `*`, `/`.
 We could add more, namely: `|`, `&`, `^`, `<<`, `>>`, `>>>` and `%`:
 
 Input:
 ```js
 function f() {
   return [
     123.45 | 0,
     123.45 & 0,
     123.45 ^ 0,
     123 << 0,
     123 >> 0,
     123 >>> 0,
     123.45 | 1,
     123.45 & 1,
     123.45 ^ 1,
     123 << 1,
     123 >> 1,
     123 >>> 1,
     3 ** 2,
     3 ** 2.5,
     3.5 ** 2,
     2 ** 3 ** 0.5,
     4 % 2,
     4 % 2.5,
     4 % 3,
   - Issue: https://github.com/facebook/react/issues/29649
   - Fix PR #29650 — feat(compiler): Implement constant folding for more binary expressions
   - PR: https://github.com/facebook/react/pull/29650
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/Optimization/ConstantPropagation.ts:           case "|": {
            if (typeof lhs === "number" && typeof rhs === "number") {
              result = { kind: "Primitive", value: lhs | rhs, loc: value.loc };
            }
            br
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/assignment-variations.expect.md:   return 1;

97. Issue #29622 — Compiler Logical Negation Constant Propagation (closed 2024-05-29T16:17:44Z)
   - Issue detail: Consider the following constant propagation:
 
 Input:
 ```js
 function foo() {
   const b = true;
   if (!b) {
     console.log("bar");
   } else {
     console.log("baz");
   }
 
   return {
     b0: !true,
     n0: !0,
     n1: !1,
     n2: !2,
     s0: !"",
     s1: !"a",
     s2: !"ab",
     n: !null,
   };
 }
 ```
 
 Output:
 ```js
 function foo() {
   console.log("baz");
   return {
     b0: false,
     n0: true,
     n1: false,
     n2: false,
     s0: true,
     s1: false,
     s2: fals
   - Issue: https://github.com/facebook/react/issues/29622
   - Fix PR #29623 — feat(compiler): Compiler Logical Negation Constant Propagation
   - PR: https://github.com/facebook/react/pull/29623
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/Optimization/ConstantPropagation.ts:     case "UnaryExpression": {
      switch (value.operator) {
        case "!": {
          const operand = read(constants, value.value);
          if (operand !== null && operand.kind === "Primitive"
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/constant-propagation-unary.expect.md: 
## Input

```javascript
import { Stringify } from "shared-runtime";

function foo() {
  let _b;
  const b = true;
  if (!b) {
    _b = "bar";
  } else {
    _b = "baz";
  }

  return (
    <Stringify

98. Issue #29130 — `react-compiler-healthcheck` prints "StrictMode usage not found." in Next.js project with `reactStrictMode: true` in `next.config.js` (closed 2024-05-20T15:55:36Z)
   - Issue detail: ## Summary
 
 Can't provide a sandbox with Next.js I guess, but the case is rather simple. In Next.js, you don't manually add StrictMode, so the checks implemented in `compiler/packages/react-compiler-healthcheck/src/checks/strictMode.ts` won't apply. On top of these, we should add `reactStrictMode: true` detection in `next.config.js`, if the latter file is found.
   - Issue: https://github.com/facebook/react/issues/29130
   - Fix PR #29167 — feat(compiler-healthcheck): Support strict mode check for nextjs apps
   - PR: https://github.com/facebook/react/pull/29167
   - Code excerpts:
     - compiler/packages/react-compiler-healthcheck/src/checks/strictMode.ts: const NextConfigFileRE = /^next\.config\.(js|mjs)$/;
const NextStrictModeRE = /reactStrictMode:\s*true/;
    if (StrictModeUsage) {
    if (NextConfigFileRE.exec(path) !== null) {
      StrictModeUsag
     - compiler/packages/react-compiler-healthcheck/src/index.ts:       default: "**/+(*.{js,mjs,jsx,ts,tsx}|package.json)",

99. Issue #29132 — [React 19] react-compiler warns when mutating globals inside useCallback (closed 2024-05-20T02:13:04Z)
   - Issue detail: ## Summary
 
 ![image](https://github.com/facebook/react/assets/18744505/3e60a741-81e6-45b3-a2b4-64b4c8e8fc01)
 
 https://playground.react.dev/#N4Igzg9grgTgxgUxALhAHQHYIB4AcIwAuABACYIBmAhlADYkVQZyECWEGxAsgJ4CCuXAAoAlMWCZMxYnA5gSMBGFYAvBMQC8xKGAQBhKrVoAjKnADWQqdOKjNAPnHWbxAO6sMpCK4B0FCBCaxADkpjDBzsQAvgA0kQDaALrWItbWioSwnAA8pKwAbvYAEghGgQDqBLSk2QD0eYUA3JhRmCBRQA
   - Issue: https://github.com/facebook/react/issues/29132
   - Fix PR #29154 — compiler: fix accidental propagation of function effects from StartMemoize/FinishMemoize
   - PR: https://github.com/facebook/react/pull/29154
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/Inference/InferReferenceEffects.ts:               []
              []
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/allow-global-mutation-in-effect-indirect-usecallback.expect.md: // @validatePreserveExistingMemoizationGuarantees
import { c as _c } from "react/compiler-runtime"; // @validatePreserveExistingMemoizationGuarantees

100. Issue #29100 — [React 19] React Compiler doesn't preserve HTML Entities (closed 2024-05-17T21:36:32Z)
   - Issue detail: ## Summary
 
 When using React Compiler, this component:
 ```tsx
 export default function MyApp() {
   return <div>Parent &gt; Children</div>;
 }
 ```
 
 becomes
 
 ```tsx
 function MyApp() {
   const $ = _c(1);
 
   let t0;
 
   if ($[0] === Symbol.for("react.memo_cache_sentinel")) {
     t0 = <div>Parent > Children</div>;
     $[0] = t0;
   } else {
     t0 = $[0];
   }
 
   return t0;
 }
 ```
 
 which leads to this error: `ERROR: The character ">" is not valid inside a JSX element`
 
 Repro:
   - Issue: https://github.com/facebook/react/issues/29100
   - Fix PR #29143 — compiler: workaround babel issue with html entity escaping
   - PR: https://github.com/facebook/react/pull/29143
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/CodegenReactiveFunction.ts: const JSX_TEXT_CHILD_REQUIRES_EXPR_CONTAINER_PATTERN = /[<>&]/;
      if (JSX_TEXT_CHILD_REQUIRES_EXPR_CONTAINER_PATTERN.test(value.value)) {
        return createJsxExpressionContainer(
          pla
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/jsx-html-entity.expect.md: 
## Input

```javascript
function Component() {
  return <div>&gt;&lt;span &amp;</div>;
}

export const FIXTURE_ENTRYPOINT = {
  fn: Component,
  params: [{}],
};

```

## Code

```javascript
import {

101. Issue #29120 — Bug: React Compiler should not encode in JSX prop value (closed 2024-05-17T17:59:08Z)
   - Issue detail: <!--
   Please provide a clear and concise description of what the bug is. Include
   screenshots if needed. Please test using the latest version of the relevant
   React packages to make sure your issue has not already been fixed.
 -->
 
 React version: 19.0.0-beta-26f2496093-20240514
 
 ## Steps To Reproduce
 
 Link to code example:
 
 **Input Code**
 
 ```jsx
 'use client';
 
 function Comp() {
   return (
     <div aria-label="我能吞下玻璃而不伤身体">
       我能吞下玻璃而不伤身体
     </div>
   )
 }
 ```
 
 **Re
   - Issue: https://github.com/facebook/react/issues/29120
   - Fix PR #29141 — compiler: Workaround Babel bug with unicode in jsx string attrs
   - PR: https://github.com/facebook/react/pull/29141
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/CodegenReactiveFunction.ts: import { createHmac } from "crypto";
/**
 * Due to a bug in earlier Babel versions, JSX string attributes with double quotes or with unicode characters
 * may be escaped unnecessarily. To avoid trigge
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/jsx-string-attribute-non-ascii.expect.md: 
## Input

```javascript
function Component() {
  return (
    <Post
      author="potetotes"
      text="in addition to understanding JavaScript semantics and the rules of React, the compiler team al

102. Issue #29124 — fix(compiler): avoid escape non-English character (closed 2024-05-17T17:59:09Z)
   - Issue detail: <!--
   Thanks for submitting a pull request!
   We appreciate you spending the time to work on these changes. Please provide enough information so that others can review your pull request. The three fields below are mandatory.
 
   Before submitting a pull request, please make sure the following is done:
 
   1. Fork [the repository](https://github.com/facebook/react) and create your branch from `main`.
   2. Run `yarn` in the repository root.
   3. If you've fixed a bug or added code that shou
   - Issue: https://github.com/facebook/react/pull/29124
   - Fix PR #29141 — compiler: Workaround Babel bug with unicode in jsx string attrs
   - PR: https://github.com/facebook/react/pull/29141
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/ReactiveScopes/CodegenReactiveFunction.ts: import { createHmac } from "crypto";
/**
 * Due to a bug in earlier Babel versions, JSX string attributes with double quotes or with unicode characters
 * may be escaped unnecessarily. To avoid trigge
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/jsx-string-attribute-non-ascii.expect.md: 
## Input

```javascript
function Component() {
  return (
    <Post
      author="potetotes"
      text="in addition to understanding JavaScript semantics and the rules of React, the compiler team al

103. Issue #29113 — [React 19] React compiler strips `await` from `for await` loops (closed 2024-05-17T18:03:26Z)
   - Issue detail: ## Summary
 
 React compiler is compiling
 
 ```
 async function MyApp({ something }) {
   for await (const deferredState of foo) {
     // do stuff
   }
 }
 ```
 
 into
 
 ```
 async function MyApp(t0) {
   for (const deferredState of foo) {
   }
 }
 ```
 
 i.e the `for await` became a regular `for`. 
 
 https://playground.react.dev/#N4Igzg9grgTgxgUxALhAQzATwHZwAQBmUuALgJYTZ4CymAggA4MAUwekAtgiQBZnYBzPAF8AlHmAAdKoQgw8aAO5oyJPMziUwagCYICCGDAQ6AyiTQkEeCAVkRxUmXjwB6V3h0R2JKAQLSLsLSwdggwkA
   - Issue: https://github.com/facebook/react/issues/29113
   - Fix PR #29118 — [compiler] Todo for for-await loops
   - PR: https://github.com/facebook/react/pull/29118
   - Code excerpts:
     - compiler/packages/babel-plugin-react-compiler/src/HIR/BuildHIR.ts:       if (stmt.node.await) {
        builder.errors.push({
          reason: `(BuildHIR::lowerStatement) Handle for-await loops`,
          severity: ErrorSeverity.Todo,
          loc: stmt.node.loc ?
     - compiler/packages/babel-plugin-react-compiler/src/__tests__/fixtures/compiler/error.todo-for-await-loops.expect.md: 
## Input

```javascript
async function Component({ items }) {
  const x = [];
  for await (const item of items) {
    x.push(item);
  }
  return x;
}

```


## Error

```
  1 | async function Compone

104. Issue #16462 — DevTools: Fully disable 0.14 support (closed 2019-09-26T15:41:47Z)
   - Issue detail: It’s confusing that 0.14 or earlier is in half-working state where it displays a tree (but incorrectly). We should detect it and fully disable if it doesn’t work. Or fix it.
 
 If we go the route of disabling support:
 1. DevTools should show a warning message that clearly indicates the version of React isn't supported. (This is probably a good idea for v13 and older anyway.)
 2. DevTools should not throw any errors.
 
 ---
 Originally reported by @gaearon via https://github.com/bvaughn/react-de
   - Issue: https://github.com/facebook/react/issues/16462
   - Fix PR #16897 — DevTools shows unsupported renderer version dialog
   - PR: https://github.com/facebook/react/pull/16897
   - Code excerpts:
     - packages/react-devtools-extensions/src/main.js:               warnIfUnsupportedVersionDetected: true,
     - packages/react-devtools-shared/src/backend/agent.js:   onUnsupportedRenderer(rendererID: number) {
    this._bridge.send('unsupportedRendererVersion', rendererID);
  }


105. Issue #4730 — Shallow rendering uses `.type` and throws deprecations (closed 2015-08-31T20:30:56Z)
   - Issue detail: When calling `renderer.render()` I get:  ``` Warning: Foo.type is deprecated. Use Foo directly to access the class ```  It seems to be here, and a few other places:   https://github.com/facebook/react/blob/master/src/test/ReactTestUtils.js#L418  I wonder if https://github.com/facebook/react/pull/4009 broke this entirely...
   - Issue: https://github.com/facebook/react/issues/4730
   - Fix PR #4735 — Better error for invalid element when shallow rendering
   - PR: https://github.com/facebook/react/pull/4735
   - Code excerpts:
     - src/test/ReactTestUtils.js:   invariant(
    ReactElement.isValidElement(element),
    'ReactShallowRenderer render(): Invalid component element.%s',
    typeof element === 'function' ?
      ' Instead of passing a component cla
     - src/test/__tests__/ReactTestUtils-test.js:   it('should throw for invalid elements', function() {
    var SomeComponent = React.createClass({
      render: function() {
        return <div />;
      },
    });

    var shallowRenderer = ReactT

106. Issue #26065 — Bug: onTransitionStart (closed 2024-04-08T21:23:05Z)
   - Issue detail: <!--
   Please provide a clear and concise description of what the bug is. Include
   screenshots if needed. Please test using the latest version of the relevant
   React packages to make sure your issue has not already been fixed.
 -->
 
 React version: any
 
 ## Steps To Reproduce
 
 Add onTransitionStart and onTransitionEnd handlers to element with styles that contain transition declaration
 
 <!--
   Your bug will get fixed much faster if we can run your code and it doesn't
   have dependenc
   - Issue: https://github.com/facebook/react/issues/26065
   - Fix PR #27345 — Add support for transition{run,start,cancel} events
   - PR: https://github.com/facebook/react/pull/27345
   - Code excerpts:
     - packages/react-dom-bindings/src/events/DOMEventNames.js:   // 'transitionrun' |
  // 'transitionstart' |
  // 'transitioncancel' |

export const TRANSITION_RUN: DOMEventName =
  getVendorPrefixedEventName('transitionrun');
export const TRANSITION_START: DOM
     - packages/react-dom-bindings/src/events/DOMEventProperties.js:   TRANSITION_RUN,
  TRANSITION_START,
  TRANSITION_CANCEL,

  registerSimpleEvent(TRANSITION_RUN, 'onTransitionRun');
  registerSimpleEvent(TRANSITION_START, 'onTransitionStart');
  registerSimpleEven

107. Issue #28602 — Class components should consume the ref prop (closed 2024-04-02T22:25:28Z)
   - Issue detail: Class components should consume the ref prop   With the `enableRefAsProp` flag enabled, refs are normal props and no longer filtered in the JSX runtime. Still, some APIs exist that conceptionally "consume" the ref since they bind the ref to a value. This includes `forwardRef` that already implemented filtering the `ref` prop out to the props passed to the inner component. We also need to do the same for class components. A `ref` passed a class component is bound to that class instance, if we kee
   - Issue: https://github.com/facebook/react/pull/28602
   - Fix PR #28719 — Fix: Class components should "consume" ref prop
   - PR: https://github.com/facebook/react/pull/28719
   - Code excerpts:
     - packages/react-dom/src/__tests__/ReactCompositeComponent-test.js:     expect(instance1.props).toEqual({prop: 'testKey'});
    expect(instance2.props).toEqual({prop: 'testKey'});
    expect(instance3.props).toEqual({prop: null});
     - packages/react-reconciler/src/ReactFiberBeginWork.js:   resolveClassComponentProps,
      const resolvedProps = resolveClassComponentProps(Component, props, false);
      const resolvedProps = resolveDefaultProps(Component, props);
      const resolvedPr

108. Issue #24539 — [DevTools Bug]: When inspecting with DevTools, it fails to select correct react component when there are multiple react-dom instances in the application (closed 2022-06-08T20:01:07Z)
   - Issue detail: ### Website or app
 
 https://codesandbox.io/s/jtiw8m
 
 ### Repro steps
 
 When using devtools in the linked codesandbox, I am not able to select react components that are rendered by the micro-fe using the inspect tool.
 
 Steps to reproduce:
 1. Go to https://jtiw8m.csb.app/ 
 2. Open React DevTools and click on Inspect icon with the "Select an element on the page to inspect it"  tooltip
 3. Inspect the component with the pink background and text "micro-fe example heading"
 4. Devtools select
   - Issue: https://github.com/facebook/react/issues/24539
   - Fix PR #24665 — [DevTools] find best renderer when inspecting
   - PR: https://github.com/facebook/react/pull/24665
   - Code excerpts:
     - packages/react-devtools-shared/src/backend/agent.js:   getBestMatchingRendererInterface(node: Object): RendererInterface | null {
    let bestMatch = null;
      const fiber = renderer.getFiberForNative(node);
      if (fiber !== null) {
        // chec
     - packages/react-devtools-shared/src/backend/legacy/renderer.js:   let getFiberForNative = (node: NativeType) => {
    // Not implemented.
    return null;
  };
    getFiberForNative = (node: NativeType) => {
      return renderer.ComponentTree.getClosestInstanceFr

109. Issue #20750 — Bug: react-hooks/exhaustive-deps false positive when function is casted with TypeScript (closed 2024-02-01T20:08:23Z)
   - Issue detail: React version: 17.0.1
 
 ### Steps To Reproduce
 Setup eslint with @typescript-eslint/parser as parser
 Cast a function passed to `useEffect`
 
 ```
 import {useCallback, useEffect} from 'react';
 
 type F = (...args: unknown[]) => void;
 
 function MyComp() {
 	const foo = useCallback(() => {}, []);
 
 	// OK
 	useEffect(() => {
 		foo();
 	}, [foo]);
 
 	// WARNS?
 	useEffect((() => {
 		foo();
 	}) as F, [foo]);
 
 	return 'Hello, world'
 }
 ```
 
 Link to code example: https://github.com/0x2
   - Issue: https://github.com/facebook/react/issues/20750
   - Fix PR #28202 — fix(eslint-plugin-react-hooks): accepting `as` expression as a callback
   - PR: https://github.com/facebook/react/pull/28202
   - Code excerpts:
     - packages/eslint-plugin-react-hooks/__tests__/ESLintRuleExhaustiveDeps-test.js:     {
      code: normalizeIndent`
        function App(props) {
          React.useEffect((() => {
            console.log(props.test);
          }) as any, [props.test]);
        }
      `,
    },
     - packages/eslint-plugin-react-hooks/src/ExhaustiveDeps.js:         case 'TSAsExpression':
          visitFunctionWithDependencies(
            callback.expression,
            declaredDependenciesNode,
            reactiveHook,
            reactiveHookName,
 

110. Issue #25844 — Bug: react-hooks/exhaustive-deps does not accept readonly arrays as deps (closed 2024-02-01T19:30:19Z)
   - Issue detail: <!--
   Please provide a clear and concise description of what the bug is. Include
   screenshots if needed. Please test using the latest version of the relevant
   React packages to make sure your issue has not already been fixed.
 -->
 
 React version:
 ```
 react: 16.8.6
 eslint-plugin-react-hooks: 4.2.0
 ```
 
 ## Steps To Reproduce
 
 1. Properly [configure](https://reactjs.org/docs/hooks-rules.html#eslint-plugin) the `react-hooks/exhaustive-deps` ESLint rule
 2. In your code, pass the `dep
   - Issue: https://github.com/facebook/react/issues/25844
   - Fix PR #28189 — fix(eslint-plugin-react-hooks): accepting `as` expressions as deps array
   - PR: https://github.com/facebook/react/pull/28189
   - Code excerpts:
     - packages/eslint-plugin-react-hooks/__tests__/ESLintRuleExhaustiveDeps-test.js:     {
      code: normalizeIndent`
        function App(props) {
          React.useEffect(() => {
            console.log(props.test);
          }, [props.test] as const);
        }
      `,
    },
 
     - packages/eslint-plugin-react-hooks/src/ExhaustiveDeps.js:       const isArrayExpression =
        declaredDependenciesNode.type === 'ArrayExpression';
      const isTSAsArrayExpression =
        declaredDependenciesNode.type === 'TSAsExpression' &&
        d

111. Issue #20162 — Bug: react-hooks/exhaustive-deps false positive when deps is defined with typescript const typing (closed 2024-02-01T19:30:19Z)
   - Issue detail: React version: 17.0.1
 
 ## Steps To Reproduce
 
 1. Setup eslint with `@typescript-eslint/parser` as parser
 2. Add `as const` to the deps array
 
 ```
 function MyComp() {
 	const [state, setState] = useState()
 	useEffect(() => {
 		console.log(state)
 	}, [state] as const)
 	return 'Hello, world'
 }
 ```
 
 Link to code example: https://github.com/tranvansang/exhaustive-deps-bug-1
 
 
 ## The current behavior
 
 The following errors were reported
 
 ```
   5:5  warning  React Hook useEffect
   - Issue: https://github.com/facebook/react/issues/20162
   - Fix PR #28189 — fix(eslint-plugin-react-hooks): accepting `as` expressions as deps array
   - PR: https://github.com/facebook/react/pull/28189
   - Code excerpts:
     - packages/eslint-plugin-react-hooks/__tests__/ESLintRuleExhaustiveDeps-test.js:     {
      code: normalizeIndent`
        function App(props) {
          React.useEffect(() => {
            console.log(props.test);
          }, [props.test] as const);
        }
      `,
    },
 
     - packages/eslint-plugin-react-hooks/src/ExhaustiveDeps.js:       const isArrayExpression =
        declaredDependenciesNode.type === 'ArrayExpression';
      const isTSAsArrayExpression =
        declaredDependenciesNode.type === 'TSAsExpression' &&
        d

112. Issue #22970 — [DevTools Bug] Could not find ID for Fiber "App" (closed 2022-01-21T16:05:49Z)
   - Issue detail: ### Website or app  not public  ### Repro steps  I have two code bases in a yarn workspaces linked monorepo. One is using react-three-fiber (the lib), and the other one is really thin wrapper around it with some simple UI, just couple of buttons. Both are using multiple (3) zustand stores.  ### How often does this bug happen?  Every time  ### DevTools package (automated)  react-devtools-extensions  ### DevTools version (automated)  4.21.0-2f8f60ca8  ### Error message (automated)  Could not find
   - Issue: https://github.com/facebook/react/issues/22970
   - Fix PR #23162 — DevTools should not crawl unmounted subtrees when profiling starts
   - PR: https://github.com/facebook/react/pull/23162
   - Code excerpts:
     - packages/react-devtools-shared/src/__tests__/profilerStore-test.js: 
  it('should not throw while initializing context values for Fibers within a not-yet-mounted subtree', () => {
    const promise = new Promise(resolve => {});
    const SuspendingView = () => {
     
     - packages/react-devtools-shared/src/backend/renderer.js:     const id = getFiberIDUnsafe(fiber);

    // Not all Fibers in the subtree have mounted yet.
    // For example, Offscreen (hidden) or Suspense (suspended) subtrees won't yet be tracked.
    // We 

113. Issue #21718 — [DevTools Bug]: Settings panel layout broken (closed 2021-06-24T15:19:57Z)
   - Issue detail: ### Website or app  https://www.enexis.nl/  ### Repro steps  Website is actually irrelevant, but required.
 
 1. Open the devtools
 2. Press the settings button.
 3. Observe the layout being broken (causing horizontal scrollbar).
 
 Screenshot
 ![image](https://user-images.githubusercontent.com/152227/122902511-cb7feb00-d34e-11eb-9656-29f5c9c62194.png)
   ### How often does this bug happen?  Every time  ### DevTools package (automated)  _No response_  ### DevTools version (automated)  _No respon
   - Issue: https://github.com/facebook/react/issues/21718
   - Fix PR #21747 — DevTools: Fix Settings dialog scroll/size bug in Firefox
   - PR: https://github.com/facebook/react/pull/21747
   - Code excerpts:
     - packages/react-devtools-shared/src/devtools/views/Settings/SettingsModal.css:   width: 410px;
     - packages/react-devtools-shared/src/devtools/views/TabBar.css:   /* Hide radio buttons for Firefox too */
  position:  relative;


  /* Hide radio buttons for Firefox too */
  position:  absolute;

114. Issue #24883 — Bug: React 18 renderToPipeableStream missing support for nonce for bootstrapScripts and bootstrapModules (closed 2023-05-01T16:19:04Z)
   - Issue detail: React version: 18.1.0-next-af730436c-20220405
 
 ## Steps To Reproduce
 1. Use server with CSP script-src set to strict-dynamic and with nonce.
 2. Use renderToPipeableStream and add nonce to its options. Pass js client assets through bootstrapScripts.
 3. Launch development server and try to load app.
 
 ## The current behavior
 The renderToPipeableStream nonce is only applied to inline scripts (bootstrapScriptContent) in createResponseState().
 
 ## The expected behavior
 A strict-dynamic scri
   - Issue: https://github.com/facebook/react/issues/24883
   - Fix PR #26738 — Add nonce support to bootstrap scripts and external runtime
   - PR: https://github.com/facebook/react/pull/26738
   - Code excerpts:
     - packages/react-dom-bindings/src/server/ReactFizzConfigDOM.js:   // state for outputting CSP nonce
  nonce: string | void,

const scriptNonce = stringToPrecomputedChunk('" nonce="');

      if (nonce) {
        bootstrapChunks.push(
          scriptNonce,
       
     - packages/react-dom-bindings/src/server/ReactFizzConfigDOMLegacy.js:   nonce: string | void,
    nonce: responseState.nonce,

115. Issue #25667 — [DevTools Bug]: react-devtools depends on vulnerable version of electron (closed 2023-03-08T03:31:56Z)
   - Issue detail: ### Website or app  https://github.com/facebook/react/blob/main/packages/react-devtools/package.json  ### Repro steps  ### Issue
 electron package versions <18.3.7 suffer from a security vulnerability: "Exfiltration of hashed SMB credentials on Windows via file:// redirect".
 See https://github.com/advisories/GHSA-p2jh-44qj-pf2v
 
 ### Solution
 Upgrade electron dependency in react-devtools to >18.3.7  ### How often does this bug happen?  Every time  ### DevTools package (automated)  _No respons
   - Issue: https://github.com/facebook/react/issues/25667
   - Fix PR #26337 — [DevTools] upgrade electron to latest version & security improvements
   - PR: https://github.com/facebook/react/pull/26337
   - Code excerpts:
     - packages/react-devtools/app.html:       // window.api is defined in preload.js
      const {electron, readEnv, ip, getDevTools} = window.api;
      const {options, useHttps, host, protocol, port} = readEnv();
      const localIp = ip.
     - packages/react-devtools/app.js:       contextIsolation: true, // protect against prototype pollution
      enableRemoteModule: false, // turn off remote
      sandbox: false, // allow preload script to access file system
      prelo

116. Issue #26051 — [DevTools Bug]: Can not work on devtools, instructions lead to error (closed 2023-01-27T20:35:08Z)
   - Issue detail: ### Website or app  https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en  ### Repro steps  Because react requires java, not on macos (but assumes brew installed!):
 ```
 brew update && brew install java
 sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
 export PATH="/usr/local/opt/openjdk/bin:$PATH"' >> ~/.zshrc
 export PATH="/usr/local/opt/openjdk/bin:$PATH" >> ~/.zshrc
 export PATH="/usr/loca
   - Issue: https://github.com/facebook/react/issues/26051
   - Fix PR #26067 — [DevTools] fix local build for extension
   - PR: https://github.com/facebook/react/pull/26067
   - Code excerpts:
     - packages/react-devtools-extensions/webpack.backend.js:   devtool: __DEV__ ? 'cheap-module-source-map' : false,
     - packages/react-devtools-extensions/webpack.config.js:   devtool: __DEV__ ? 'cheap-module-source-map' : false,

117. Issue #24522 — [DevTools] Manifest version 2 is deprecated (closed 2022-10-22T02:52:19Z)
   - Issue detail: ### Website or app  https://developer.chrome.com/blog/mv2-transition/  ### Repro steps  Use latest React DevTools with Electron (Chromium) (18.2.0 / Chromium 100)
 
 ```
   (node:80082) ExtensionLoadWarning: Warnings loading extension at ./node_modules/electron-devtools-vendor/extensions/react-developer-tools:
     Manifest version 2 is deprecated, and support will be removed in 2023. See https://developer.chrome.com/blog/mv2-transition/ for more details.
 ```  ### How often does this bug happen
   - Issue: https://github.com/facebook/react/issues/24522
   - Fix PR #25145 — [DevTools] upgrade to Manifest V3
   - PR: https://github.com/facebook/react/pull/25145
   - Code excerpts:
     - packages/react-devtools-extensions/chrome/manifest.json:   "manifest_version": 3,
  "minimum_chrome_version": "88",
  "action": {
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'self'"
  },
    {
      "resources": [
  
     - packages/react-devtools-extensions/edge/manifest.json:   "manifest_version": 3,
  "minimum_chrome_version": "88",
  "action": {
  "content_security_policy": {
    "extension_pages": "script-src 'self'; object-src 'self'"
  },
    {
      "resources": [
  

118. Issue #24032 — renderToReadableStream Passes Reusable Chunks (closed 2022-03-07T18:34:11Z)
   - Issue detail: https://github.com/cloudflare/miniflare/issues/203
 
 We switched to using "bytes" streams but, by spec, chunks get transferred in that format. Totally reasonable. However, we pass reusable chunks which then get detached. I'm not sure why the polyfill or fixtures didn't catch this.
 
 We really should be using the byob model instead and copy into a larger chunk for perf anyway so this just makes that more urgent.
   - Issue: https://github.com/facebook/react/issues/24032
   - Fix PR #24034 — [Fizz] write chunks to a buffer with no re-use
   - PR: https://github.com/facebook/react/pull/24034
   - Code excerpts:
     - packages/react-dom/src/__tests__/ReactDOMFizzServerBrowser-test.js: 
  // @gate experimental
  it('should stream large contents that might overlow individual buffers', async () => {
    const str492 = `(492) This string is intentionally 492 bytes long because we want 
     - packages/react-server/src/ReactServerStreamConfigBrowser.js: const VIEW_SIZE = 512;
let currentView = null;
let writtenBytes = 0;

export function beginWriting(destination: Destination) {
  currentView = new Uint8Array(VIEW_SIZE);
  writtenBytes = 0;
}
  if (ch

119. Issue #25565 — Bug: useSyncExternalStore does not update internal value if a setState is also called, outside useEffect, causing store sets not re-render (closed 2022-11-08T10:25:44Z)
   - Issue detail: In a custom hook, I forgot to wrap my `setState` call in a `useEffect`, which did not pose any problems prior to React 18 but now this does not work anymore. The component does not re-render if the store is changed back to its initial value. I guess this might be expected, but there was no warning whatsoever, so it was hard to find out.
 
 So this is more like a question:
 - Is that behavior a bug?
 - If it is not, would it be useful to have a warning for another developer making the same mistak
   - Issue: https://github.com/facebook/react/issues/25565
   - Fix PR #25578 — Fix useSyncExternalStore dropped update when state is dispatched in render phase
   - PR: https://github.com/facebook/react/pull/25578
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberHooks.new.js:   const prevSnapshot = (currentHook || hook).memoizedState;
     - packages/react-reconciler/src/ReactFiberHooks.old.js:   const prevSnapshot = (currentHook || hook).memoizedState;

120. Issue #16497 — DevTools: Show component file path (closed 2019-12-10T17:24:35Z)
   - Issue detail: **Do you want to request a *feature* or report a *bug*?**
 
 Feature.
 
 **What is the current behavior?**
 
 The new DevTools doesn't show the component file path as did the v3 version.
 
 **What is the expected behavior?**
 
 It would be great to show the component file path, it's a really important feature when working in a large codebase.
 
 **Which versions of React, and which browser / OS are affected by this issue? Did this work in previous versions of React?**
 
 React DevTools v4 is aff
   - Issue: https://github.com/facebook/react/issues/16497
   - Fix PR #17567 — Show component location for selected element in bottom/right of props panel
   - PR: https://github.com/facebook/react/pull/17567
   - Code excerpts:
     - packages/react-devtools-shared/src/devtools/views/Components/SelectedElement.css: .Source {
  padding: 0.25rem;
  border-top: 1px solid var(--color-border);
}

.SourceHeaderRow {
  display: flex;
  align-items: center;
}

.SourceHeader {
  flex: 1 1;
  font-family: var(--font-famil
     - packages/react-devtools-shared/src/devtools/views/Components/SelectedElement.js: import {copy} from 'clipboard-js';
    source,

      {source !== null && (
        <Source fileName={source.fileName} lineNumber={source.lineNumber} />
      )}
    </div>
  );
}

// This function is

121. Issue #25187 — [DevTools Bug]: DevTools shouldn't skip over keyed Fragments in the tree (closed 2022-09-07T17:21:31Z)
   - Issue detail: ### Website or app  https://github.com/reactjs/reactjs.org/pull/4981  ### Repro steps  1. Wrap something into `<Fragment key="stuff">`
 2. It doesn't show up in DevTools
 
 We filter out fragments because they tend to be useless. But this one is important! Keys are crucial and we should show anything with a key in the tree.  ### How often does this bug happen?  Every time  ### DevTools package (automated)  _No response_  ### DevTools version (automated)  _No response_  ### Error message (automat
   - Issue: https://github.com/facebook/react/issues/25187
   - Fix PR #25197 — [DevTools][Bugfix] Don't hide fragment if it has a key
   - PR: https://github.com/facebook/react/pull/25197
   - Code excerpts:
     - packages/react-devtools-shared/src/backend/renderer.js:       case Fragment:
        return 'Fragment';
    const {_debugSource, tag, type, key} = fiber;
      case Fragment:
        return key === null;

122. Issue #24170 — [React DevTools] Component Stacks for Timeline Profiler (closed 2022-06-28T21:15:24Z)
   - Issue detail: In the Timeline Profiler, we currently denote each state update with a dot. If you hover on the state update, you get some information about it, such as which component caused the update, the lane the update was rendered at, and the time that the update happened. This is useful for unique components. However, for components (ex. library components) that are used in multiple places, just having the component name is less helpful. 
 
 It would be most useful to get a stack of component owners (lik
   - Issue: https://github.com/facebook/react/issues/24170
   - Fix PR #24805 — [DevTools] front-end for profiling event stack
   - PR: https://github.com/facebook/react/pull/24805
   - Code excerpts:
     - packages/react-devtools-extensions/src/main.js:         const viewSourceLineFunction = (url, line) => {
          chrome.devtools.panels.openResource(url, line);
        };

              viewSourceLineFunction,
     - packages/react-devtools-shared/src/__tests__/utils-test.js: import {stackToComponentSources} from 'react-devtools-shared/src/devtools/utils';

    it('should parse a component stack trace', () => {
      expect(
        stackToComponentSources(`
    at Foobar 

123. Issue #24623 — [DevTools Bug] When inspecting, hook values after `useDeferredValue` are offset (closed 2022-06-17T18:43:10Z)
   - Issue detail: ### Website or app
 
 https://github.com/Alduino/React-useDeferredValue-DevTools-Reprod
 
 ### Repro steps
 
 1. Start the app in either dev or production mode.
 2. Open the React dev tools
 3. Click on the "App" component
 4. The first Memo has the value `3.14` (the value that the second Memo should have) instead of `1.41`
 
 If you want it to throw an error instead of just looking at the values, you can set `window.throwIfIncorrect = true` before DevTools inspects the component.
 
 I tried in
   - Issue: https://github.com/facebook/react/issues/24623
   - Fix PR #24742 — [DevTools] fix useDeferredValue to match reconciler change
   - PR: https://github.com/facebook/react/pull/24742
   - Code excerpts:
     - packages/react-debug-tools/src/ReactDebugHooks.js:   const hook = nextHook();
    value: hook !== null ? hook.memoizedState : value,
     - packages/react-debug-tools/src/__tests__/ReactHooksInspectionIntegration-test.js:       React.useMemo(() => 'not used', []);
      {
        id: 2,
        isStateEditable: false,
        name: 'Memo',
        value: 'not used',
        subHooks: [],
      },
  it('should support u

124. Issue #24603 — [DevTools Bug]: "Reload and profile" aways disabled on Timeline tab (closed 2022-06-10T14:38:33Z)
   - Issue detail: ### Website or app  beta.reactjs.org (local development)  ### Repro steps  1. https://github.com/reactjs/reactjs.org/tree/main/beta
 2. `yarn dev`
 
 "Reload and profile" is enabled for Flamegraph:
 
 <img width="724" alt="Screenshot 2022-05-23 at 21 28 07" src="https://user-images.githubusercontent.com/810438/169900687-7c62d7c5-34ad-43c0-b1fa-ca45c8e16dba.png">
 
 But disabled for Timeline:
 
 <img width="671" alt="Screenshot 2022-05-23 at 21 28 12" src="https://user-images.githubusercontent.co
   - Issue: https://github.com/facebook/react/issues/24603
   - Fix PR #24702 — [DevTools] enable "reload & profile" button for timeline view
   - PR: https://github.com/facebook/react/pull/24702
   - Code excerpts:
     - packages/react-devtools-shared/src/devtools/views/Profiler/Profiler.js:             <ReloadAndProfileButton disabled={!supportsProfiling} />

125. Issue #21541 — Create GitHub actions to auto verify DevTools issues have repro steps (closed 2021-05-21T19:48:12Z)
   - Issue detail: Many of the issues created with the with the [`devtools_bug_report.yml`](https://github.com/facebook/react/blob/master/.github/ISSUE_TEMPLATE/devtools_bug_report.yml) template are missing repro information (e.g. a "localhost" or otherwise invalid URL, missing or no repro description). I usually have to review, label, comment, and close this by hand.
 
 It would be nice if we had an automated action that checked:
 * Was the issue made with the [`devtools_bug_report.yml`](https://github.com/facebo
   - Issue: https://github.com/facebook/react/issues/21541
   - Fix PR #21542 — Add GitHub action to check for bug repro
   - PR: https://github.com/facebook/react/pull/21542
   - Code excerpts:
     - .github/workflows/devtools_check_repro.yml: name: DevTools Check for bug repro
on:
  issues:
    types: [opened, edited]
  issue_comment:
    types: [created, edited]

jobs:
  check-repro:
    runs-on: ubuntu-latest
    steps:
      - uses: act

126. Issue #24543 — [DevTools Bug]: console.log crashes when I enable DevTools on Chrome (closed 2022-05-12T14:29:36Z)
   - Issue detail: ### Website or app
 
 https://github.com/coolwind0202/web/blob/23877f77e23837a007aada5be363d65290571c88/web/src/components/page/members/IndexPage/IndexPage.tsx#L27
 
 ### Repro steps
 
 For checking whenever my project will work correctly, when I run a command `next dev`, errors which are shown below occurred.
 
 ![image](https://user-images.githubusercontent.com/51913600/168043187-bf77a943-39c4-45d3-9a1d-2cdf97c904df.png)
 
 When I pass a first argument which is an **object** to `console.log()`
   - Issue: https://github.com/facebook/react/issues/24543
   - Fix PR #24546 — [devtools] fix a bug in console.log with non-string args
   - PR: https://github.com/facebook/react/pull/24546
   - Code excerpts:
     - packages/react-devtools-shared/src/backend/utils.js:     typeof inputArgs[0] !== 'string' ||
    inputArgs[0].match(/([^%]|^)(%c)/g) ||
     - packages/react-devtools-shared/src/hook.js:       typeof inputArgs[0] !== 'string' ||
      inputArgs[0].match(/([^%]|^)(%c)/g) ||

127. Issue #24441 — [DevTools Bug]: TreeContext error: Can't access property "id" in undefined (closed 2022-05-05T15:46:57Z)
   - Issue detail: ### Website or app  https://app.replay.io/  ### Repro steps  Unfortunately I don't know how to reproduce this bug. It was just logged to Sentry.
 
 It seems like there's a logic bug here though:
 https://github.com/facebook/react/blob/bd4784c8f8c6b17cf45c712db8ed8ed19a622b26/packages/react-devtools-shared/src/devtools/views/Components/TreeContext.js#L386-L416
 
 If `selectedElementIndex` is null or `elementIndicesWithErrorsOrWarnings` is empty, then `flatIndex` would be 0 still– and this stateme
   - Issue: https://github.com/facebook/react/issues/24441
   - Fix PR #24501 — Fixed possible undefined error in TreeContext reducer
   - PR: https://github.com/facebook/react/pull/24501
   - Code excerpts:
     - packages/react-devtools-shared/src/devtools/views/Components/TreeContext.js:         const elementIndicesWithErrorsOrWarnings = store.getElementsWithErrorsAndWarnings();
        if (elementIndicesWithErrorsOrWarnings.length === 0) {
        const elementIndicesWithErrorsOrWarn

128. Issue #24428 — [DevTools Bug]: forwardRef components not marked as "rendered" if context changed (closed 2022-05-04T20:25:28Z)
   - Issue detail: ### Website or app
 
 https://codesandbox.io/s/forwardref-context-change-did-not-render-lpdk4t?file=/src/index.js
 
 ### Repro steps
 
 1. Goto https://lpdk4t.csb.app/
 1. Start profiling
 3. Enter "a" into the input
 4. Stop profiling
 ![forwardRef-did-not-render](https://user-images.githubusercontent.com/12292047/164915101-f28f305a-2c51-4b89-8515-da073e5551c9.png)
 
 
 
 ### How often does this bug happen?
 
 Every time
 
 ### DevTools package (automated)
 
 _No response_
 
 ### DevTools versi
   - Issue: https://github.com/facebook/react/issues/24428
   - Fix PR #24494 — [React DevTools] Fix `didFiberRender`
   - PR: https://github.com/facebook/react/pull/24494
   - Code excerpts:
     - packages/react-devtools-shared/src/backend/renderer.js:       case ForwardRef:

129. Issue #24302 — Console dimming on second StrictMode render forces string cast (closed 2022-04-14T16:30:04Z)
   - Issue detail: <!--
   Please provide a clear and concise description of what the bug is. Include
   screenshots if needed. Please test using the latest version of the relevant
   React packages to make sure your issue has not already been fixed.
 -->
 
 React version: 18.0.0 (congrats on the release ☺️)
 
 ## Steps To Reproduce
 
 1. During rendering of a component, log something that doesn't naturally cast to a string (e.g., `console.log(new Set())`).
 2. Wrap the tree in `StrictMode`.
 3. Observe the consol
   - Issue: https://github.com/facebook/react/issues/24302
   - Fix PR #24373 — [DevTools] Avoid Stringifying Objects during Strict Mode Double Logging
   - PR: https://github.com/facebook/react/pull/24373
   - Code excerpts:
     - packages/react-devtools-shared/src/__tests__/console-test.js:     expect(mockLog.mock.calls[1]).toEqual([
      '%c%s',
      `color: ${process.env.DARK_MODE_DIMMED_LOG_COLOR}`,
      'log',
    ]);
    expect(mockWarn.mock.calls[1]).toHaveLength(3);
    expect(
     - packages/react-devtools-shared/src/__tests__/utils-test.js: import {
  format,
  formatWithStyles,
} from 'react-devtools-shared/src/backend/utils';

  describe('formatWithStyles', () => {
    it('should format empty arrays', () => {
      expect(formatWithSty

130. Issue #24384 — Bug: Incorrect Hydration Mismatch Detection during Suspense - "Hydration failed because the initial UI does not match what was rendered on the server." (closed 2022-05-03T19:31:17Z)
   - Issue detail: React version: 18.0.0
 
 ## Steps To Reproduce
 
 1. Add a Suspense Boundary
 2. Add a **component that will suspend** to load some data (faked).
 3. Render at least one **sibling component** _after_ the suspending component.
 3. Render server-side using renderToPipeableStream()
 4. Render client-side using hydrateRoot()
 
 __Reproductions in CodeSandbox:__
 
 - [Reproduction 1](https://yt3148.sse.codesandbox.io) with Next.js [Edit](https://codesandbox.io/s/github/xiel/SuspenseHydrationErrorNext
   - Issue: https://github.com/facebook/react/issues/24384
   - Fix PR #24404 — Suppress hydration warnings when a preceding sibling suspends
   - PR: https://github.com/facebook/react/pull/24404
   - Code excerpts:
     - packages/react-dom/src/__tests__/ReactDOMFizzServer-test.js: 
  // @gate experimental && enableClientRenderFallbackOnTextMismatch
  it('#24384: Suspending should halt hydration warnings while still allowing siblings to warm up', async () => {
    const makeApp 
     - packages/react-dom/src/__tests__/ReactDOMServerPartialHydration-test.internal.js:       const container = document.createElement('section');
        const secondToLastCall =
          mockError.mock.calls[mockError.mock.calls.length - 2];
        expect(secondToLastCall).toEqual([


131. Issue #24268 — Bug: [eslint-plugin-exhaustive-deps] can't find unstable value. (closed 2022-04-11T20:43:16Z)
   - Issue detail: <!--
   Please provide a clear and concise description of what the bug is. Include
   screenshots if needed. Please test using the latest version of the relevant
   React packages to make sure your issue has not already been fixed.
 -->
 
 React version: 18.0.0 (not important)
 
 ## Steps To Reproduce
 I'll show as a code.
 <img width="593" alt="스크린샷 2022-04-04 오전 12 01 05" src="https://user-images.githubusercontent.com/65149763/161434194-868b7fbb-9571-40d8-a4e3-2b261506d9ac.png">
 
 Li
   - Issue: https://github.com/facebook/react/issues/24268
   - Fix PR #24343 —  [eslint-plugin-exhaustive-deps] Fix exhaustive deps check for unstable vars
   - PR: https://github.com/facebook/react/pull/24343
   - Code excerpts:
     - packages/eslint-plugin-react-hooks/__tests__/ESLintRuleExhaustiveDeps-test.js:     {
      code: normalizeIndent`
        function Counter(unstableProp) {
          let [count, setCount] = useState(0);
          setCount = unstableProp
          useEffect(() => {
            let
     - packages/eslint-plugin-react-hooks/src/ExhaustiveDeps.js:                 let writeCount = 0;
                  if (references[i].isWrite()) {
                    writeCount++;
                  }
                  if (writeCount > 1) {
                    r

132. Issue #24279 — Bug: [eslint-plugin-exhaustive-deps] hook wrongly marked as conditional (at exact number of conditionals in FC) (closed 2022-04-07T23:22:47Z)
   - Issue detail: <!--
   Please provide a clear and concise description of what the bug is. Include
   screenshots if needed. Please test using the latest version of the relevant
   React packages to make sure your issue has not already been fixed.
 -->
 
 When using an exact number of conditionals before and after a react hook, the `React Hook "hook_name" is called conditionally. React Hooks must be called in the exact same order in every component render` rule is wrongly flagged as being violated. This is a re
   - Issue: https://github.com/facebook/react/issues/24279
   - Fix PR #24287 — Fix false positive lint error with large number of branches 
   - PR: https://github.com/facebook/react/pull/24287
   - Code excerpts:
     - packages/eslint-plugin-react-hooks/__tests__/ESLintRulesOfHooks-test.js:     `
      // Valid because the neither the conditions before or after the hook affect the hook call
      // Failed prior to implementing BigInt because pathsFromStartToEnd and allPathsFromStartToEn
     - packages/eslint-plugin-react-hooks/src/RulesOfHooks.js: /* global BigInt */
            return BigInt('0');
            paths = BigInt('0');
            paths = BigInt('1');
            paths = BigInt('0');
          if (segment.reachable && paths === BigI

133. Issue #24162 — [DevTools Bug] Cannot add node "1" because a node with that id is already in the Store. (closed 2022-03-28T18:25:31Z)
   - Issue detail: ### Website or app
 
 http://bestellen-a.cito.nl
 
 ### Repro steps
 
 Just opening the console and going to Components or Profiler shows this error.
 
 I noticed that in the console there are two warnings for contentScript.js (I am assuming this file is part of this extension):
 ﻿
 contentScript.js:113 [Violation] 'message' handler took 210ms
 contentScript.js:113 [Violation] 'message' handler took 891ms
 
 ### How often does this bug happen?
 
 Sometimes
 
 ### DevTools package (automated)
   - Issue: https://github.com/facebook/react/issues/24162
   - Fix PR #24186 — DevTools bugfix: Ignore duplicate welcome "message" events
   - PR: https://github.com/facebook/react/pull/24186
   - Code excerpts:
     - packages/react-devtools-extensions/src/backend.js: let welcomeHasInitialized = false;

  // In some circumstances, this method is called more than once for a single welcome message.
  // The exact circumstances of this are unclear, though it seems rel
     - packages/react-devtools-extensions/src/contentScript.js: function handleMessageFromPage(event) {
    event.source === window &&
    event.data &&
    event.data.source === 'react-devtools-bridge'
    port.postMessage(event.data.payload);

134. Issue #24233 — eslint-plugin-react-hooks CHANGELOG missing 4.4.0 release (closed 2022-03-31T14:43:08Z)
   - Issue detail: Currently the CHANGELOG shows 4.3.0 as the latest version of `eslint-plugin-react-hooks`, but at least on `main`, there is not a 4.4.0.
 
 
 React version: n/a
 
 ## Steps To Reproduce
 
 1. View Changelog
 2. Compare to version on https://www.npmjs.com/package/eslint-plugin-react-hooks
 
 
 Link to code example: n/a
 
 
 ## The current behavior
 
 No 4.4.0 explanation in CHANGELOG.md
 
 ## The expected behavior
 
 4.4.0 explanation in CHANGELOG.md
   - Issue: https://github.com/facebook/react/issues/24233
   - Fix PR #24234 — Add 4.4.0 release to eslint rules CHANGELOG
   - PR: https://github.com/facebook/react/pull/24234
   - Code excerpts:
     - packages/eslint-plugin-react-hooks/CHANGELOG.md: ## 4.4.0

* No changes, this was an automated release together with React 18.


135. Issue #11911 —  React DOM crashes when <option> contains three interpolated value if one is a conditional.  (closed 2018-08-01T15:16:35Z)
   - Issue detail: <!--
   Note: if the issue is about documentation or the website, please file it at:
   https://github.com/reactjs/reactjs.org/issues/new
 -->
 
 **Do you want to request a *feature* or report a *bug*?** 
 
 Bug 
 
 **What is the current behavior?**
 
 React DOM crashes when `<option>` contains three interpolated value if one is a conditional. 
 
 Reproduction: https://jsfiddle.net/0opjvycp/ 
 
 1. Change the value of the `<select>`
 2. React crashes with `NotFoundError: Node was not found`
   - Issue: https://github.com/facebook/react/issues/11911
   - Fix PR #13261 — Fix a crash when using dynamic children in <option> tag
   - PR: https://github.com/facebook/react/pull/13261
   - Code excerpts:
     - fixtures/dom/src/components/fixtures/selects/index.js: 
        <TestCase
          title="An option which contains conditional render fails"
          relatedIssues="11911">
          <TestCase.Steps>
            <li>Select any option</li>
          </Te
     - packages/react-dom/src/__tests__/ReactDOMOption-test.js:       '<div> cannot appear as a child of <option>.\n' + '    in option (at **)',

136. Issue #24116 — [DevTools] fix inspecting an element in a nested renderer bug (closed 2022-03-17T19:40:04Z)
   - Issue detail: Fixes [this issue](https://github.com/facebook/react/issues/23225), where inspecting components in nested renderers results in an error. The reason for this is because we have different `fiberToIDMap` instances for each renderer, and owners of a component could be in different renderers.
 
 This fix moves the `fiberToIDMap` and `idToArbitraryFiberMap` out of the `attach` method so there's only one instance of each for all renderers.
 
 ---
 
 Resolves #24116.
   - Issue: https://github.com/facebook/react/pull/24116
   - Fix PR #24116 — [DevTools] fix inspecting an element in a nested renderer bug
   - PR: https://github.com/facebook/react/pull/24116
   - Code excerpts:
     - packages/react-devtools-shared/src/__tests__/inspectedElement-test.js:   it('inspecting nested renderers should not throw', async () => {
    // Ignoring react art warnings
    spyOn(console, 'error');
    const ReactArt = require('react-art');
    const ArtSVGMode = req
     - packages/react-devtools-shared/src/backend/renderer.js: // Map of one or more Fibers in a pair to their unique id number.
// We track both Fibers to support Fast Refresh,
// which may forcefully replace one of the pair as part of hot reloading.
// In that 

137. Issue #23373 — [DevTools Bug] Cannot read properties of undefined (reading 'split') (closed 2022-03-10T18:36:47Z)
   - Issue detail: ### Website or app
 
 https://next-rsc-notes.vercel.app/
 
 ### Repro steps
 
 1. enter the site
 2. open react-devtools
 3. select We(maybe suspense's child component)
 4. and show following errors.
 
 ### How often does this bug happen?
 
 Every time
 
 ### DevTools package (automated)
 
 react-devtools-extensions
 
 ### DevTools version (automated)
 
 4.23.0-e28a0db22
 
 ### Error message (automated)
 
 Cannot read properties of undefined (reading 'split')
 
 ### Error call stack (automated)
   - Issue: https://github.com/facebook/react/issues/23373
   - Fix PR #24065 — Better handle undefined Error stacks in DevTools error boundary
   - PR: https://github.com/facebook/react/pull/24065
   - Code excerpts:
     - packages/react-devtools-shared/src/devtools/views/ErrorBoundary/ErrorBoundary.js:       typeof error.message === 'string'
        : null;
      typeof error.stack === 'string'

138. Issue #23283 — [DevTools Bug] Could not find node with id "18" in commit tree (closed 2022-03-10T18:35:52Z)
   - Issue detail: ### Website or app  https://github.com/ModelSaber/ModelSaber.Main  ### Repro steps  Just try and load the 2/5 and 3/5 report from a reload and start profiling instance.
 
 Change `REACT_APP_API_URL` to `https://apimodelsaber.rainemods.io` in order to launch the app without needing the full .NET 6 environment and the corresponding data in the postgres database.  ### How often does this bug happen?  Every time  ### DevTools package (automated)  react-devtools-extensions  ### DevTools version (auto
   - Issue: https://github.com/facebook/react/issues/23283
   - Fix PR #24031 — Fixed edge case bug in Profiler
   - PR: https://github.com/facebook/react/pull/24031
   - Code excerpts:
     - packages/react-devtools-shared/src/__tests__/__snapshots__/profilingCache-test.js.snap: exports[`ProfilingCache should collect data for each root (including ones added or mounted after profiling started): Data for root Parent 3`] = `
Object {
  "commitData": Array [
    Object {
      "c
     - packages/react-devtools-shared/src/__tests__/profilingCache-test.js:     expect(allProfilingDataForRoots).toHaveLength(3);

139. Issue #16437 — Devtools V4: Where is Highlight Updates? (closed 2019-10-03T17:46:01Z)
   - Issue detail: If I understood correctly, this is the correct repository for devtools v4, right?
 
 I just noticed that react devtool were updated. I'm missing the "Highlight Updates" function.
 How can I activate it?
 
 ![image](https://user-images.githubusercontent.com/12381373/63209674-4ab58f80-c0e4-11e9-8134-40789625c81e.png)
 
 ![image](https://user-images.githubusercontent.com/12381373/63209676-543ef780-c0e4-11e9-8128-a73c4b6bf8f7.png)
 
 Version: 4.0.2 (8/15/2019)
   - Issue: https://github.com/facebook/react/issues/16437
   - Fix PR #16989 — Added trace updates feature (DOM only)
   - PR: https://github.com/facebook/react/pull/16989
   - Code excerpts:
     - packages/react-devtools-core/src/backend.js:             bridge.shutdown();
     - packages/react-devtools-extensions/src/backend.js:   // Let the frontend know that the backend has attached listeners and is ready for messages.
  // This covers the case of of syncing saved values after reloading/navigating while DevTools remain open

140. Issue #23089 — React 18: Context providers are reset to initial value in SSR during rendering (closed 2022-01-24T17:52:51Z)
   - Issue detail: <!--
   Ask a question or share feedback about the React 18 release here.
 -->
 
 While testing SSR streaming in latest React 18 experimental and alpha versions, [we noticed](https://github.com/Shopify/hydrogen/issues/415) that context providers are reset to their initial values during rendering under certain conditions.
 It works well when handling 1 request at a time. However, when the server gets 2 or more requests at the same time, the context providers seem to get confused. The context is c
   - Issue: https://github.com/facebook/react/issues/23089
   - Fix PR #23171 — Fix context providers in SSR when handling multiple requests
   - PR: https://github.com/facebook/react/pull/23171
   - Code excerpts:
     - packages/react-dom/src/__tests__/ReactDOMFizzServerNode-test.js: 
  // @gate experimental
  it('should be able to get context value when promise resolves', async () => {
    class DelayClient {
      get() {
        if (this.resolved) return this.resolved;
        
     - packages/react-server/src/ReactFizzNewContext.js: 
    // On the way back, we push the new ones that weren't common.
    pushNode(next);

141. Issue #22947 — Missing entry point in package.json (closed 2022-01-07T20:59:47Z)
   - Issue detail: https://github.com/facebook/react/blob/3b3daf5573efe801fa3dc659020625b4023d3a9f/packages/react/package.json#L32
 
 This `build-info.json` is not published to npm.
 
 https://www.jsdelivr.com/package/npm/react?version=18.0.0-rc.0
   - Issue: https://github.com/facebook/react/issues/22947
   - Fix PR #22954 — Add package.json as one of entry point
   - PR: https://github.com/facebook/react/pull/22954
   - Code excerpts:
     - packages/react/package.json:     "./package.json": "./package.json",

142. Issue #22646 — Add e2e tests for inline package (closed 2022-01-04T15:28:03Z)
   - Issue detail: DevTools has good unit test coverage but no e2e test coverage. This is because the support for testing _extensions_ is pretty limited in e2e testing libraries. That being said, we could probably get 80% of the value of e2e testing leveraging our `react-devtools-inline` package.
 
 We should create a few example tests (e.g. load hook names, select a component and edit props/state, etc) to see how viable this is.
 
 For now, these tests should not block PRs from landing.
   - Issue: https://github.com/facebook/react/issues/22646
   - Fix PR #23019 — Circle CI: Run DevTools Playwright e2e tests
   - PR: https://github.com/facebook/react/pull/23019
   - Code excerpts:
     - .circleci/config.yml:   run_devtools_e2e_tests:
    docker: *docker
    environment: *environment
    steps:
      - checkout
      - attach_workspace:
          at: .
      - run: yarn workspaces info | head -n -1 > works
     - scripts/circleci/run_devtools_e2e_tests.js: #!/usr/bin/env node

'use strict';

const {spawn} = require('child_process');
const {join} = require('path');

const ROOT_PATH = join(__dirname, '..', '..');

const inlinePackagePath = join(ROOT_PATH,

143. Issue #22958 — [react-devtools-inline][4.22.0]: broken published package (closed 2021-12-15T04:45:46Z)
   - Issue detail: ## Steps To Reproduce
 
 1. install `react-devtools-inline` in a project that has `react` and `react-is`
 2. open node
 3. `require('react-devtools-inline')`
 4. See error:
 ```
 Uncaught:
 Error: Cannot find module '/Users/jstejada/code/jstejada-react/build/oss-experimental/react-is'
 Require stack:
 - /home/avi/projects/temp/inlinetest/node_modules/react-devtools-inline/dist/backend.js
 - <repl>
     at Function.Module._resolveFilename (node:internal/modules/cjs/loader:933:15)
     at Function
   - Issue: https://github.com/facebook/react/issues/22958
   - Fix PR #22961 — Revert changes to react-devtools-inline Webpack config from PR #22760
   - PR: https://github.com/facebook/react/pull/22961
   - Code excerpts:
     - packages/react-devtools-inline/webpack.config.js:     react: 'react',
    'react-dom': 'react-dom',
    'react-is': 'react-is',
    scheduler: 'scheduler',

144. Issue #22959 — react-devtools report Error: Cannot find module './app' (closed 2021-12-15T04:28:57Z)
   - Issue detail: react-devtools version: 4.22.0
 npm -g install react-devtools
 react-devtools
 
 ```
 internal/modules/cjs/loader.js:905
   throw err;
   ^
 
 Error: Cannot find module './app'
 Require stack:
 - /Users/foo/.nvm/versions/node/v14.18.1/lib/node_modules/react-devtools/bin.js
     at Function.Module._resolveFilename (internal/modules/cjs/loader.js:902:15)
     at Function.resolve (internal/modules/cjs/helpers.js:99:19)
     at Object.<anonymous> (/Users/foo/.nvm/versions/node/v14.18.1/lib/node_modu
   - Issue: https://github.com/facebook/react/issues/22959
   - Fix PR #22960 — Re-added deleted files array to react-devtools package.json
   - PR: https://github.com/facebook/react/pull/22960
   - Code excerpts:
     - packages/react-devtools/package.json:   "files": [
    "bin.js",
    "app.html",
    "app.js",
    "index.js",
    "icons"
  ],

145. Issue #22834 — [DevTools Bug]: CDN-based site not working (closed 2021-12-09T20:32:11Z)
   - Issue detail: ### Website or app
 
 https://lcdev.shaped.ca
 
 ### Repro steps
 
 Dev tools not working in FF or Chrome, says "This page doesn't appear to be using react".
 
 React is included via CDN as shown on react website https://reactjs.org/docs/cdn-links.html:
 ``
 	<script crossorigin="anonymous" src="https://unpkg.com/react@17/umd/react.development.js"></script>
 ``
 
 Web Console on said page says:
 ``
 Download the React DevTools for a better development experience: https://reactjs.org/link/react-d
   - Issue: https://github.com/facebook/react/issues/22834
   - Fix PR #22932 — DevTools should inject XHTML pages too (not just HTML)
   - PR: https://github.com/facebook/react/pull/22932
   - Code excerpts:
     - packages/react-devtools-extensions/src/injectGlobalHook.js: switch (document.contentType) {
  case 'text/html':
  case 'application/xhtml+xml': {
    injectCode(
      ';(' +
        installHook.toString() +
        '(window))' +
        saveNativeValues +
   

146. Issue #22747 — Bug: markInternalModuleRanges undefined (closed 2021-11-12T15:03:41Z)
   - Issue detail: Testing react 18 im getting this error 
 
 ![Screenshot from 2021-11-12 07-33-44](https://user-images.githubusercontent.com/86263126/141428205-3f3b3f67-e235-44ef-ae1a-5c42e4f7800a.png)
 
 
 React version: https://unpkg.com/react-dom@18.0.0-alpha-a44a7a2a3-20211111/umd/react-dom.development.js
 
 wants to add that in this version: https://unpkg.com/react-dom@18.0.0-alpha-05726d72c-20210927/umd/react-dom.development.js no happens, so probably a recent change affected this
 
 File Related: https://
   - Issue: https://github.com/facebook/react/issues/22747
   - Fix PR #22748 — Add runtime type checks around module boundary code
   - PR: https://github.com/facebook/react/pull/22748
   - Code excerpts:
     - packages/react-reconciler/src/SchedulingProfiler.js: import isArray from 'shared/isArray';
    // This check would not be required,
    // except that it's possible for things to override __REACT_DEVTOOLS_GLOBAL_HOOK__.
    if (isArray(ranges)) {
      

147. Issue #22413 — Bug: Components inside typescript namespaces cause ReferenceError (closed 2021-11-09T20:22:19Z)
   - Issue detail: Forwarded from https://github.com/vitejs/vite/issues/3900 by @not-rusty based on the recommendation of @sodatea, which stated that this should be considered as a bug in the `react-refresh` package.
 &nbsp;  
 
 ----
 
 ### Describe the bug
 Apparently components inside namespaces is not supported. I don't exactly know if the error comes from esbuild or something, but it would nice.
 
 The bug is that is not shown as a compilation error.
 
 ### Reproduction
 Simply start a `react-ts` project with
   - Issue: https://github.com/facebook/react/issues/22413
   - Fix PR #22621 — [React Refresh] support typescript namespace syntax
   - PR: https://github.com/facebook/react/pull/22621
   - Code excerpts:
     - package.json:     "@babel/plugin-syntax-typescript": "^7.14.5",
    "web-streams-polyfill": "^3.1.1",
     - packages/react-refresh/src/ReactFreshBabelPlugin.js:           let modulePrefix = '';
            case 'TSModuleBlock':
              insertAfterPath = path;
              programPath = insertAfterPath.parentPath.parentPath;
              break;

      

148. Issue #22051 — ESlint plugin is broken on 7.32.0 - Missing hasSuggestions (closed 2021-09-06T19:17:51Z)
   - Issue detail: ## Summary
 
 I kept hitting this error after upgrading to ESlint 7.32.0 whenever reaching a hook that had a suggestion.
 
 ```
 Oops! Something went wrong! :(
 
 ESLint: 7.32.0
 
 Error: Rules with suggestions must set the `meta.hasSuggestions` property to `true`.
 ```
 
 ## Test Plan
 
 I've updated the meta entry and used it in my own project. Lint completes successfully.
 I've also updated the Eslint version in this project.
   - Issue: https://github.com/facebook/react/pull/22051
   - Fix PR #22248 — feat(eslint-plugin-react-hooks): support ESLint 8.x
   - PR: https://github.com/facebook/react/pull/22248
   - Code excerpts:
     - .eslintrc.js:     {
      files: ['packages/eslint-plugin-react-hooks/src/*.js'],
      plugins: ['eslint-plugin'],
      rules: {
        'eslint-plugin/prefer-object-rule': ERROR,
        'eslint-plugin/require-m
     - package.json:     "eslint-plugin-eslint-plugin": "^3.5.3",

149. Issue #22246 — [eslint-plugin-react-hooks] Support ESLint 8.x (closed 2021-09-06T19:17:52Z)
   - Issue detail: ESLint has released the first beta versions of v8 🎉
 https://eslint.org/blog/2021/08/eslint-v8.0.0-beta.0-released
 https://eslint.org/blog/2021/08/eslint-v8.0.0-beta.1-released
 https://eslint.org/blog/2021/09/eslint-v8.0.0-beta.2-released
 https://eslint.org/blog/2021/09/eslint-v8.0.0-rc.0-released
 
 It would be awesome to have official ESLint 8 support. 👊
 I'm happy to help where I can of course 🙂
   - Issue: https://github.com/facebook/react/issues/22246
   - Fix PR #22248 — feat(eslint-plugin-react-hooks): support ESLint 8.x
   - PR: https://github.com/facebook/react/pull/22248
   - Code excerpts:
     - .eslintrc.js:     {
      files: ['packages/eslint-plugin-react-hooks/src/*.js'],
      plugins: ['eslint-plugin'],
      rules: {
        'eslint-plugin/prefer-object-rule': ERROR,
        'eslint-plugin/require-m
     - package.json:     "eslint-plugin-eslint-plugin": "^3.5.3",

150. Issue #22678 — Improve DevTools CSS variables situation (closed 2021-11-08T20:17:22Z)
   - Issue detail: Related to this comment: https://github.com/facebook/react/pull/22660#pullrequestreview-795368779
 
 The majority of DevTools theme colors are stored in `packages/react-devtools-shared/src/constants`:
 https://github.com/facebook/react/blob/5cccacd131242bdea2c2fe4b33fac50d2e3132b4/packages/react-devtools-shared/src/constants.js#L75-L383
 
 But some of them are also stored in `packages/react-devtools-shared/src/devtools/views/root.css`:
 https://github.com/facebook/react/blob/5cccacd131242bdea2c2
   - Issue: https://github.com/facebook/react/issues/22678
   - Fix PR #22716 — fix(devtools): expose css vars to reach-ui portal components
   - PR: https://github.com/facebook/react/pull/22716
   - Code excerpts:
     - packages/react-devtools-shared/src/devtools/views/Button.js: import Tooltip from './Components/reach-ui/tooltip';
    button = <Tooltip label={title}>{button}</Tooltip>;
     - packages/react-devtools-shared/src/devtools/views/Components/OwnersStack.js: import Tooltip from '../Components/reach-ui/tooltip';
import {
  Menu,
  MenuList,
  MenuButton,
  MenuItem,
} from '../Components/reach-ui/menu-button';

151. Issue #22705 — Timeline screenshots are sometimes way too small (depending on aspect ratio) (closed 2021-11-08T17:28:34Z)
   - Issue detail: For example:
 <img width="1904" alt="Screen Shot 2021-11-05 at 11 59 05 AM" src="https://user-images.githubusercontent.com/29597/140540816-25d6d47b-7aea-4121-aeaa-565accc65b1f.png">
   - Issue: https://github.com/facebook/react/issues/22705
   - Fix PR #22706 — Timeline: Improved snapshot view
   - PR: https://github.com/facebook/react/pull/22706
   - Code excerpts:
     - packages/react-devtools-timeline/src/CanvasPage.js:           height={height}
          width={width}
     - packages/react-devtools-timeline/src/EventTooltip.js:   height: number,
  width: number,
  height,
  width,
    content = (
      <TooltipSnapshot height={height} snapshot={snapshot} width={width} />
    );
const TooltipSnapshot = ({
  height,
  snapshot

152. Issue #22673 — Avoid duplicate boilerplate header (closed 2021-11-04T14:40:35Z)
   - Issue detail: Follow up on @rickhanlonii's comment: https://github.com/facebook/react/pull/22670#issuecomment-956569098
   - Issue: https://github.com/facebook/react/issues/22673
   - Fix PR #22688 — Fix module-boundary wrappers
   - PR: https://github.com/facebook/react/pull/22688
   - Code excerpts:
     - scripts/rollup/wrappers.js: const USE_STRICT_HEADER_REGEX = /'use strict';\n+/;

  const path = resolve(__dirname, 'wrappers', 'registerInternalModuleBegin.js');
  const file = readFileSync(path);
  return String(file).trim();
 
     - scripts/rollup/wrappers/registerInternalModuleBegin.js: 'use strict';

153. Issue #22579 — Scheduling Profiler: De-emphasize React internals (closed 2021-10-21T18:40:42Z)
   - Issue detail: Follow up to #22578
 
 Digging into certain sources of slowness (e.g. slow memoization code) requires looking at the CPU flame chart. Unfortunately this predominantly consists of React internal frames, which can be convoluted if you are not familiar with React's source code.
 
 One way to improve this would be to either filter out (remove) React internal frames or de-emphasize them visually in some other way. Because removing them would be more work, we should try dimming them instead. For examp
   - Issue: https://github.com/facebook/react/issues/22579
   - Fix PR #22588 — Scheduling Profiler: De-emphasize React internal frames
   - PR: https://github.com/facebook/react/pull/22588
   - Code excerpts:
     - packages/react-devtools-extensions/src/checkForDuplicateInstallations.js: import {
  INTERNAL_EXTENSION_ID,
  LOCAL_EXTENSION_ID,
  __DEBUG__,
} from 'react-devtools-shared/src/constants';
     - packages/react-devtools-extensions/src/constants.js: import {
  CHROME_WEBSTORE_EXTENSION_ID,
  INTERNAL_EXTENSION_ID,
  LOCAL_EXTENSION_ID,
} from 'react-devtools-shared/src/constants';


154. Issue #22613 — Scheduling Profiler flags useDeferredValue / useTransition updates as expensive (closed 2021-10-21T19:16:26Z)
   - Issue detail: This feature is meant to warn about sync priority updates that block paint (e.g. set state in layout effect) but it appears to also warn for transition priority updates. We should fix this.
   - Issue: https://github.com/facebook/react/issues/22613
   - Fix PR #22614 — Scheduling Profiler does not warn about long transitions
   - PR: https://github.com/facebook/react/pull/22614
   - Code excerpts:
     - packages/react-devtools-scheduling-profiler/src/import-worker/__tests__/preprocessData-test.internal.js: 
      it('should not warn about transition updates scheduled during commit phase', async () => {
        function Component() {
          const [value, setValue] = React.useState(0);
          // esl
     - packages/react-devtools-scheduling-profiler/src/import-worker/preprocessData.js:       // Don't warn about transition updates scheduled during the commit phase.
      // e.g. useTransition, useDeferredValue
      // These are allowed to be long-running.
      if (
        !schedul

155. Issue #22577 — [DevTools Bug]: Blank tools localhost only (closed 2021-11-03T14:35:42Z)
   - Issue detail: ### Website or app
 
 google.com
 
 ### Repro steps
 
 This started after last update 4.20.0
 ![image](https://user-images.githubusercontent.com/11052469/137713404-e6702959-7870-46a6-8566-4cfe61d25309.png)
 ![image](https://user-images.githubusercontent.com/11052469/137713464-c5e478d2-4e9e-4ee4-abdf-83d23c04704b.png)
 
 
 ### How often does this bug happen?
 
 Every time
 
 ### DevTools package (automated)
 
 _No response_
 
 ### DevTools version (automated)
 
 _No response_
 
 ### Error message
   - Issue: https://github.com/facebook/react/issues/22577
   - Fix PR #22597 — Dev Tools: Relax constraint on passing extensionId for backend init
   - PR: https://github.com/facebook/react/pull/22597
   - Code excerpts:
     - packages/react-devtools-extensions/src/backend.js: // @flow strict-local
  const extensionId = event.data.extensionId;
  setup(window.__REACT_DEVTOOLS_GLOBAL_HOOK__, extensionId);
function setup(hook, extensionId) {
          extensionId,
     - packages/react-devtools-extensions/src/contentScript.js: import {CURRENT_EXTENSION_ID} from './constants';

      extensionId: CURRENT_EXTENSION_ID,
      extensionId: CURRENT_EXTENSION_ID,
      extensionId: CURRENT_EXTENSION_ID,

156. Issue #22591 — [DevTools Bug]: Loading / parsing hook names is failing on v4.20 (closed 2021-11-04T15:46:52Z)
   - Issue detail: ### Website or app
 
 reactjs.org
 
 ### Repro steps
 
 1. Open a website that uses React.
 2. Inspect an element that uses Hooks.
 3. Attempt to load hook names.
 4. Loading hook names always fails:
 
 ![image](https://user-images.githubusercontent.com/1271509/137997605-a3f601a9-59e5-4370-b307-3ff50af22cae.png)
   - Issue: https://github.com/facebook/react/issues/22591
   - Fix PR #22590 — DevTools: Fix passing extensionId in evaled postMessage calls
   - PR: https://github.com/facebook/react/pull/22590
   - Code excerpts:
     - packages/react-devtools-extensions/src/main.js:                extensionId: "${CURRENT_EXTENSION_ID}",
                window.postMessage({
                  source: 'react-devtools-extension',
                  extensionId: "${CURRENT_EXTENSION_ID

157. Issue #21630 — Add a failing test for Suspense hydration (closed 2021-10-19T00:44:34Z)
   - Issue detail: This shows a bug in hydration where server content is incorrectly being deleted and warned about.
 
 Quoting @sebmarkbage on the cause:
 
 >So it happens because React doesn't stop rendering siblings when something suspends. Hydration or otherwise.
 
 >So when the sibling suspends, we see that ok we can't commit this. But let's see what happens next. But we don't know how many DOM nodes to skip over because the thing that suspended could render zero or many DOM nodes. So the hydration pointer is
   - Issue: https://github.com/facebook/react/pull/21630
   - Fix PR #22582 — Hydrate using SuspenseComponent as the parent
   - PR: https://github.com/facebook/react/pull/22582
   - Code excerpts:
     - packages/react-dom/src/__tests__/ReactDOMServerPartialHydration-test.internal.js:   it('can hydrate siblings of a suspended component without errors', async () => {
    let suspend = false;
    let resolve;
    const promise = new Promise(resolvePromise => (resolve = resolvePromise
     - packages/react-dom/src/client/ReactDOMHostConfig.js:   parentInstance: Instance,
export function getFirstHydratableChildWithinContainer(
  parentContainer: Container,
): null | HydratableInstance {
  return getNextHydratable(parentContainer.firstChild);

158. Issue #22572 — [DevTools Bug]: Firefox and Edge show error in console about unrecognized installation on v4.20.0 (closed 2021-10-15T21:18:20Z)
   - Issue detail: ### Website or app
 
 reactjs.org
 
 ### Repro steps
 
 1. Install React DevTools v4.20.0 in Firefox
 2. Load reactjs.org in Firefox
 3. Open Firefox DevTools
 4. Observe error in console
 
 ![image](https://user-images.githubusercontent.com/1271509/137547605-e6ad3045-c20a-4828-9895-af46b8bb4db1.png)
 
 
 ### How often does this bug happen?
 
 Every time
   - Issue: https://github.com/facebook/react/issues/22572
   - Fix PR #22571 — Only show DevTools warning about unrecognized build in Chrome
   - PR: https://github.com/facebook/react/pull/22571
   - Code excerpts:
     - packages/react-devtools-extensions/src/checkForDuplicateInstallations.js: import {getBrowserName} from './utils';
const IS_CHROME = getBrowserName() === 'Chrome';

      // TODO: Support duplicate extension detection in other browsers
      if (IS_CHROME) {
        // If we

159. Issue #22486 — Detect and warn if multiple copies of React DevTools are installed (closed 2021-10-15T15:27:13Z)
   - Issue detail: If you have more than one copy of React DevTools installed and enabled (e.g. the version in the Chrome store and a locally built version) they can interfere with each other.
 
 DevTools should detect this case and warn by showing a dialog in the DevTools UI and/or by logging to the console.
 
 Note that we _should not warn_ if a related tool like Fast Refresh is present, only another copy of DevTools.
   - Issue: https://github.com/facebook/react/issues/22486
   - Fix PR #22563 — Show warning in UI when duplicate installations of DevTools extension are detected
   - PR: https://github.com/facebook/react/pull/22563
   - Code excerpts:
     - packages/react-devtools-extensions/src/background.js: // @flow strict-local
declare var chrome: any;

const ports: {
  [tab: string]: {|devtools: any, 'content-script': any|},
} = {};
import {
  EXTENSION_INSTALL_CHECK,
  SHOW_DUPLICATE_EXTENSION_WARNING
     - packages/react-devtools-extensions/src/checkForDuplicateInstallations.js:   EXTENSION_INSTALL_CHECK,
const UNRECOGNIZED_EXTENSION_ERROR =
      console.error(UNRECOGNIZED_EXTENSION_ERROR);
        `console.error("${UNRECOGNIZED_EXTENSION_ERROR}")`,
      console.error(UNREC

160. Issue #22441 — Several tests fail on main with Node v16 (closed 2021-10-11T22:40:43Z)
   - Issue detail: I forked and cloned the repo this morning (at c88fb49d37fd01024e0a254a37b7810d107bdd1d), ran `yarn` and `yarn test`, and several tests failed.
 
 React version: main (c88fb49d37fd01024e0a254a37b7810d107bdd1d)
 
 ## Steps To Reproduce
 
 1. Clone repo
 2. `yarn` and `yarn test`
 
 I was on the latest NodeJS version (16.10.0). Note that tests pass for me when switching to the 14.x LTS release of Node.
 
 ## The current behavior
 
 13 tests fail across 5 suites. Output at https://gist.github.com/jo
   - Issue: https://github.com/facebook/react/issues/22441
   - Fix PR #22477 — Update test and stack frame code to support newer V8 stack formats
   - PR: https://github.com/facebook/react/pull/22477
   - Code excerpts:
     - packages/shared/ReactComponentStackFrame.js:                 let frame = '\n' + sampleLines[s].replace(' at new ', ' at ');

                // If our component frame is labeled "<anonymous>"
                // but we have a user-provided "displ
     - scripts/jest/matchers/toThrow.js: 'use strict';

// V8 uses a different message format when reading properties of null or undefined.
// Older versions use e.g. "Cannot read property 'world' of undefined"
// Newer versions use e.g. "Ca

161. Issue #22241 — [DevTools Bug] Could not inspect element with id "219". Error thrown:Cached data for element "219" not found (closed 2021-09-30T16:48:54Z)
   - Issue detail: ### Website or app  employer-test.apna.co  ### Repro steps  The error occurred at InspectedElementContextController (chrome-extension://fmkadmapgofadopljbjfkapdkoienihi/build/main.js:37563:3)
     at Suspense
     at ErrorBoundary_ErrorBoundary (chrome-extension://fmkadmapgofadopljbjfkapdkoienihi/build/main.js:36097:5)
     at div
     at InspectedElementErrorBoundaryWrapper (chrome-extension://fmkadmapgofadopljbjfkapdkoienihi/build/main.js:36542:3)
     at NativeStyleContextController (chrome-e
   - Issue: https://github.com/facebook/react/issues/22241
   - Fix PR #22472 — DevTools: Fixed potential cache miss when insepcting elements
   - PR: https://github.com/facebook/react/pull/22472
   - Code excerpts:
     - packages/react-devtools-shared/src/__tests__/inspectedElement-test.js:   // See github.com/facebook/react/issues/22241#issuecomment-931299972
  it('should properly recover from a cache miss on the frontend', async () => {
    let targetRenderCount = 0;

    const Wrapper
     - packages/react-devtools-shared/src/backend/agent.js:   forceFullData: boolean,
    forceFullData,
        renderer.inspectElement(requestID, id, path, forceFullData),

162. Issue #15088 — useReducer - eagerReducer optimization discussion/questions (closed 2021-09-27T23:25:10Z)
   - Issue detail: I'd like to continue the discussion started by me under a recent blog post by Dan as encouraged by Dan 😉 https://github.com/gaearon/overreacted.io/commit/99bfdca459ff4094ee523c7419b58989d18bc594#r32694433
 
 Just to summarize what I've stumbled upon when experimenting with useReducer after reading that hoisted & declared in render reducers are treated differently (I've wanted to explore how they are handled by React):
 1. I have no idea how to reenter eagerReducer calculation after first schedul
   - Issue: https://github.com/facebook/react/issues/15088
   - Fix PR #22445 — Remove usereducer eager bailout
   - PR: https://github.com/facebook/react/pull/22445
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberHooks.new.js:   hasEagerState: boolean,
  const dispatch: Dispatch<A> = (queue.dispatch = (dispatchReducerAction.bind(
          hasEagerState: update.hasEagerState,
            hasEagerState: update.hasEagerState,
     - packages/react-reconciler/src/ReactFiberHooks.old.js:   hasEagerState: boolean,
  const dispatch: Dispatch<A> = (queue.dispatch = (dispatchReducerAction.bind(
          hasEagerState: update.hasEagerState,
            hasEagerState: update.hasEagerState,

163. Issue #21419 — fix: Run reducers with the props from the queued update (closed 2021-09-27T23:25:10Z)
   - Issue detail: ## Summary
 
 Closes https://github.com/facebook/react/issues/21416
 Closes https://github.com/facebook/react/issues/17953
 I don't fully understand the fix yet but it worked so I'm trying my luck with CI :man_shrugging: and test https://twitter.com/dan_abramov/status/1402015574780170240
 
 ## Test Plan
 
 - [x] failed locally without fix
 - [x] CI greem with naive fix
   - Issue: https://github.com/facebook/react/pull/21419
   - Fix PR #22445 — Remove usereducer eager bailout
   - PR: https://github.com/facebook/react/pull/22445
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberHooks.new.js:   hasEagerState: boolean,
  const dispatch: Dispatch<A> = (queue.dispatch = (dispatchReducerAction.bind(
          hasEagerState: update.hasEagerState,
            hasEagerState: update.hasEagerState,
     - packages/react-reconciler/src/ReactFiberHooks.old.js:   hasEagerState: boolean,
  const dispatch: Dispatch<A> = (queue.dispatch = (dispatchReducerAction.bind(
          hasEagerState: update.hasEagerState,
            hasEagerState: update.hasEagerState,

164. Issue #21416 — Bug: useReducer, reducer function gets called twice (possible memory leak) (closed 2021-09-27T23:25:11Z)
   - Issue detail: <!--
   Please provide a clear and concise description of what the bug is. Include
   screenshots if needed. Please test using the latest version of the relevant
   React packages to make sure your issue has not already been fixed.
 -->
 
 
 React version: 17.0.2
 
 ## Steps To Reproduce
 
 1. Create a counter reducer with a top limit (top limit is set externally using a prop or state)
 2. Return the current state if the count reaches the top limit
 3. Try to increment the counter by calling `di
   - Issue: https://github.com/facebook/react/issues/21416
   - Fix PR #22445 — Remove usereducer eager bailout
   - PR: https://github.com/facebook/react/pull/22445
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberHooks.new.js:   hasEagerState: boolean,
  const dispatch: Dispatch<A> = (queue.dispatch = (dispatchReducerAction.bind(
          hasEagerState: update.hasEagerState,
            hasEagerState: update.hasEagerState,
     - packages/react-reconciler/src/ReactFiberHooks.old.js:   hasEagerState: boolean,
  const dispatch: Dispatch<A> = (queue.dispatch = (dispatchReducerAction.bind(
          hasEagerState: update.hasEagerState,
            hasEagerState: update.hasEagerState,

165. Issue #17953 — Bug: useReducer runs the queued updates with new props (closed 2021-09-27T23:25:11Z)
   - Issue detail: <!--
   Please provide a clear and concise description of what the bug is. Include
   screenshots if needed. Please test using the latest version of the relevant
   React packages to make sure your issue has not already been fixed.
 -->
 
 React version: 16.8.0
 
 ## Steps To Reproduce
 
 <!--
   Your bug will get fixed much faster if we can run your code and it doesn't
   have dependencies other than React. Issues without reproduction steps or
   code examples may be immediately closed as not a
   - Issue: https://github.com/facebook/react/issues/17953
   - Fix PR #22445 — Remove usereducer eager bailout
   - PR: https://github.com/facebook/react/pull/22445
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberHooks.new.js:   hasEagerState: boolean,
  const dispatch: Dispatch<A> = (queue.dispatch = (dispatchReducerAction.bind(
          hasEagerState: update.hasEagerState,
            hasEagerState: update.hasEagerState,
     - packages/react-reconciler/src/ReactFiberHooks.old.js:   hasEagerState: boolean,
  const dispatch: Dispatch<A> = (queue.dispatch = (dispatchReducerAction.bind(
          hasEagerState: update.hasEagerState,
            hasEagerState: update.hasEagerState,

166. Issue #22422 — [DevTools Bug]: Emoji as visual helper produce strange symbole (closed 2021-09-27T17:34:39Z)
   - Issue detail: ### Website or app  https://codesandbox.io/s/react-playground-forked-j4niq  ### Repro steps  Emoji seem supported but produce strange symbole
 
 ![image](https://user-images.githubusercontent.com/24865815/133793744-55a55582-90ad-425f-8a40-4c061a3c1d80.png)
 
 To test emoji on Window Os, use `[win]+[.]` 🟩
   ### How often does this bug happen?  Every time  ### DevTools package (automated)  _No response_  ### DevTools version (automated)  _No response_  ### Error message (automated)  _No response_
   - Issue: https://github.com/facebook/react/issues/22422
   - Fix PR #22424 — DevTools encoding supports multibyte characters (e.g. "🟩")
   - PR: https://github.com/facebook/react/pull/22424
   - Code excerpts:
     - packages/react-devtools-shared/src/__tests__/store-test.js:   it('should handle multibyte character strings', () => {
    const Component = () => null;
    Component.displayName = '🟩💜🔵';

    const container = document.createElement('div');

    act(() => lega
     - packages/react-devtools-shared/src/backend/renderer.js:   type StringTableEntry = {|
    encodedString: Array<number>,
    id: number,
  |};

  const pendingStringTable: Map<string, StringTableEntry> = new Map();
    pendingStringTable.forEach((entry, stri

167. Issue #17624 — React DevTools might retain references to unmounted DOM elements (and their Fibers) (closed 2021-09-17T16:53:08Z)
   - Issue detail: ![Screenshot 2019-12-16 10 51 05](https://user-images.githubusercontent.com/793565/70934095-fd91ed80-1ff1-11ea-93b5-746e816585ec.png)
 There's seems to be circumstances where unmounted DOM/Fibers are kept alive by React DevTools. They're kept alive in `primaryFibers`:
 https://github.com/facebook/react/blob/34527063083195558f98108cde10b5d6ad0d6865/packages/react-devtools-shared/src/backend/renderer.js#L772
 
 It seems like a WeakSet would be appropriate and would remove the leak. Otherwise we'd
   - Issue: https://github.com/facebook/react/issues/17624
   - Fix PR #22346 — DevTools: Fix memory leak via alternate Fiber pointer
   - PR: https://github.com/facebook/react/pull/22346
   - Code excerpts:
     - packages/react-devtools-shared/src/backend/renderer.js:     // React may detach alternate pointers during unmount;
    // Since our untracking code is async, we should explicily track the pending alternate here as well.
    const alternate = fiber.alternat

168. Issue #22293 — Bug: Maximum call stack size exceeded (React Devtools) (closed 2021-09-17T13:52:52Z)
   - Issue detail: I encountered the same issue as #20640 but using `react-devtools` as a stand-alone app instead of from the the browser.
 
 The bottom line is that the profiler becomes unresponsive after any interaction with a heavily loaded react page.
 
 React version:
 
 * React: 17.0.2
 * ReactDOM: 17.0.2
 * React Devtools: 4.18.0
 
 ## Steps To Reproduce
 
 1. Attach a react-devtools stand-alone (`yarn run react-devtools`) to a session
 2. Start profiling
 3. Do something on your app that would cause a huge
   - Issue: https://github.com/facebook/react/issues/22293
   - Fix PR #22330 — Updated the utfDecodeString() method to avoid call stack exceeded error
   - PR: https://github.com/facebook/react/pull/22330
   - Code excerpts:
     - packages/react-devtools-shared/src/utils.js:   // Avoid spreading the array (e.g. String.fromCodePoint(...array))
  // Functions arguments are first placed on the stack before the function is called
  // which throws a RangeError for large array

169. Issue #22115 — DevTools: Better Bundle Names for Dynamically Imported Modules (closed 2021-09-15T17:51:34Z)
   - Issue detail: In the DevTools extension, webpack currently uses an automatically assigned ID as the chunk name for dynamically imported modules (ie. `parseHookNames` and associated code will get bundled into `6.js`).
 
 We've tried adding `chunkFilename: '[name].js'` to `output` in `webpack.config.js` and  magic comments (ie.`/* webpackChunkName: "parseHookNames" */`) to the dynamic import to fix, but neither works.
   - Issue: https://github.com/facebook/react/issues/22115
   - Fix PR #22322 — Fixed issue for better bundles,chunks and workers name in devtools-extensions.
   - PR: https://github.com/facebook/react/pull/22322
   - Code excerpts:
     - packages/react-devtools-extensions/src/main.js:           import(
            /* webpackChunkName: 'parseHookNames' */ 'react-devtools-shared/src/hooks/parseHookNames'
          );
     - packages/react-devtools-extensions/webpack.config.js:               name: '[name]',

170. Issue #22323 — Rollup build script --unsafe-partial flag is broken (closed 2021-09-15T17:32:10Z)
   - Issue detail: The following example command sequence will fail:
 ```sh
 # Grab the latest build artifacts from CI
 scripts/release/download-experimental-build.js --commit=main
 
 # Rebuild only the local NODE bundle from the source of react-dom
 # Leave all other artifacts untouched
 yarn build --unsafe-partial --type=NODE_DEV react-dom/index
 
 # Throws
 ```
 The above sequence _should_ work but instead fails with one of the two errors below:
 > Error: ENOENT: no such file or directory
 
 > Error: SyntaxErro
   - Issue: https://github.com/facebook/react/issues/22323
   - Fix PR #22324 — Fixed broken build script --unsafe-partial flag
   - PR: https://github.com/facebook/react/pull/22324
   - Code excerpts:
     - scripts/rollup/utils.js:           } else {
            // Wait for copied files to exist; ncp() sometimes completes prematurely.
            // For more detail, see github.com/facebook/react/issues/22323
            // Also 

171. Issue #21972 — Bug: `onResize` media event is missing (closed 2021-09-07T22:28:30Z)
   - Issue detail: Note: I’m happy to make a pull request to fix this, I just wanted to log it first to ensure there’s interest.
 
 ---
 
 React’s [synthetic media events](https://reactjs.org/docs/events.html#media-events) contain several [existing media events](https://html.spec.whatwg.org/multipage/media.html#mediaevents), for instance `onLoadedMetadata` and `onVolumeChange`. But there is no `onResize` handler.
 
 [`resize` is a standard media event](https://html.spec.whatwg.org/multipage/media.html#event-media-
   - Issue: https://github.com/facebook/react/issues/21972
   - Fix PR #21973 — Fix #21972: Add `onResize` event to video elements
   - PR: https://github.com/facebook/react/pull/21973
   - Code excerpts:
     - fixtures/dom/src/components/fixtures/media-events/index.js:       onResize: false,
     - packages/react-dom/src/__tests__/ReactDOMEventListener-test.js:       onResize() {},
        case 'resize':

172. Issue #22099 — [DevTools Bug] Could not inspect element with id "1335" (closed 2021-08-23T23:22:31Z)
   - Issue detail: ### Website or app  Web app we are developing for a client.  ### Repro steps  Open the components tab - no components will display
 Close the components tab
 Open the components tab again, this time the the components show but the error shows on the right pane.
   ### How often does this bug happen?  Often  ### DevTools package (automated)  react-devtools-extensions  ### DevTools version (automated)  4.14.0-d0ec283819  ### Error message (automated)  Could not inspect element with id "1335"  ###
   - Issue: https://github.com/facebook/react/issues/22099
   - Fix PR #22160 — DevTools: Replaced WeakMap with LRU for inspected element cache
   - PR: https://github.com/facebook/react/pull/22160
   - Code excerpts:
     - packages/react-devtools-shared/src/__tests__/inspectedElement-test.js:   // Regression test for github.com/facebook/react/issues/22099
  it('should not error when an unchanged component is re-inspected after component filters changed', async () => {
    const Example = (
     - packages/react-devtools-shared/src/inspectedElementCache.js:       rejectedRecord.value = `Could not inspect element with id "${element.id}". No renderer found.`;
          rejectedRecord.value = `Could not inspect element with id "${element.id}". Error thrown:

173. Issue #22113 — react-dom@alpha UMD bundle throws when rendering (closed 2021-08-18T05:40:56Z)
   - Issue detail: <!--
   Please provide a clear and concise description of what the bug is. Include
   screenshots if needed. Please test using the latest version of the relevant
   React packages to make sure your issue has not already been fixed.
 -->
 
 React version: 18.0.0-alpha-bd255700d-20210816 or main branch
 
 ## Steps To Reproduce
 
 1. Use ReactDOM development from alpha version or main branch
 2. Call ReactDOM.render() or ReactDOM.createRoot(...).render()
 
 <!--
   Your bug will get fixed much fast
   - Issue: https://github.com/facebook/react/issues/22113
   - Fix PR #22117 — Fixed ReactSharedInternals export in UMD bundle
   - PR: https://github.com/facebook/react/pull/22117
   - Code excerpts:
     - packages/react/src/forks/ReactSharedInternals.umd.js: import ReactCurrentActQueue from '../ReactCurrentActQueue';
  ReactSharedInternals.ReactCurrentActQueue = ReactCurrentActQueue;

174. Issue #21986 — [DevTools Bug]: Component tree size too small, components can't be selected (closed 2021-08-13T00:41:56Z)
   - Issue detail: ### Website or app  https://reactjs.org/  ### Repro steps  1. Visit reactjs.org
 2. Open devtools
 3. Open "Components" tab
 
 At first the component tree won't appear. Once I'm at the "Components" tab, I then have to also refresh the page to make the tree render. And when it does render, it still doesn't work properly.
 
 As a note, this issue started happening after I had to forcibly restart my computer. Since then I have tried reinstalling the extension, restarting Chrome, restarting my pc, a
   - Issue: https://github.com/facebook/react/issues/21986
   - Fix PR #22083 — Fixed Components tree indentation bug for Chrome extension
   - PR: https://github.com/facebook/react/pull/22083
   - Code excerpts:
     - packages/react-devtools-scheduling-profiler/package.json:     "react-virtualized-auto-sizer": "^1.0.6",
     - packages/react-devtools-shared/package.json:     "react-virtualized-auto-sizer": "^1.0.6",

175. Issue #21765 — React 18: "missing act()" warnings partially missing if a prior render threw (closed 2021-07-13T21:38:26Z)
   - Issue detail: Specifically `An update to * inside a test was not wrapped in act(...)` is not logged when a prior update threw. 
 
 <details>
 <summary>failing test (#21766)</summary>
 
 ```js
 // @gate __DEV__
 it('warns if a setState is called outside of act(...) after a component threw', () => {
   let setValue = null;
   function App({defaultValue}) {
     if (defaultValue === undefined) {
       throw new Error();
     }
     const [value, _setValue] = React.useState(defaultValue);
     setValue = _setVal
   - Issue: https://github.com/facebook/react/issues/21765
   - Fix PR #21766 — fix: restore execution context after RetryAfterError completed
   - PR: https://github.com/facebook/react/pull/21766
   - Code excerpts:
     - packages/react-dom/src/__tests__/ReactTestUtilsAct-test.js:       // @gate __DEV__
      it('warns if a setState is called outside of act(...) after a component threw', () => {
        let setValue = null;
        function App({defaultValue}) {
          if (d
     - packages/react-reconciler/src/ReactFiberWorkLoop.new.js:       const prevExecutionContext = executionContext;

      executionContext = prevExecutionContext;
    const prevExecutionContext = executionContext;

    executionContext = prevExecutionContext;

176. Issue #21855 — [DevTools] Parse named source AST in a worker (closed 2021-07-21T16:16:08Z)
   - Issue detail: Hooks are the preferred way for writing stateful React components, but there are a few things about them that still lag behind the class component API: inspecting state in DevTools (since hooks aren’t “named”). Even now that this feature has been released, it remains disabled by default because the size of DEV bundles in larger apps (e.g. Facebook) makes parsing the AST very slow.
 
 To alleviate this, we plan to provide an additional compilation tool that adds hook names to an extended source m
   - Issue: https://github.com/facebook/react/issues/21855
   - Fix PR #21902 — DevTools: Parse named source AST in a worker
   - PR: https://github.com/facebook/react/pull/21902
   - Code excerpts:
     - packages/react-devtools-extensions/firefox/manifest.json:   "content_security_policy": "script-src 'self' 'unsafe-eval' blob:; object-src 'self'",
     - packages/react-devtools-extensions/package.json:     "acorn-jsx": "^5.2.0",
    "webpack-dev-server": "^3.10.3",
    "workerize-loader": "^1.3.0"

177. Issue #21796 — [DevTools] Improve Fast Refresh support for named hook detection (closed 2021-07-16T03:39:30Z)
   - Issue detail: #21641 added support to DevTools for showing hook names for the inspected component. For performance reasons, this feature caches source maps and ASTs by file name to avoid re-parsing any time a new component is inspected.
 
 As https://github.com/facebook/react/pull/21790#issuecomment-873289051 mentions:
 > A new compiled script can be loaded into the VM that has the same URL (`hookSource.fileName`), same source map URL and even the same original source URL(s) as a previously loaded script, but
   - Issue: https://github.com/facebook/react/issues/21796
   - Fix PR #21891 — Clear named hooks Suspense and AST cache after a Fast Refresh
   - PR: https://github.com/facebook/react/pull/21891
   - Code excerpts:
     - packages/react-devtools-extensions/src/__tests__/parseHookNames-test.js:     parseHookNames = require('../parseHookNames').parseHookNames;
  // TODO Test that cache purge works

  // TODO Test that cached metadata is purged when Fast Refresh scheduled

     - packages/react-devtools-extensions/src/main.js: import {parseHookNames, purgeCachedMetadata} from './parseHookNames';
              loadHookNames: parseHookNames,
              purgeCachedHookNamesMetadata: purgeCachedMetadata,

178. Issue #21868 — [DevTools] Named hooks compatibility for create-react-app DEV mode (closed 2021-07-14T18:37:28Z)
   - Issue detail: Something about the source maps config causes problems for a simple create-react-app running in DEV mode. Column numbers are always reported as 0 (by 'source-maps') which causes the AST node matching to fail so hook names can't be located. We should really fix this, since a lot of people use create-react-app for prototyping.
 
 Note that source maps work correctly in production builds.
 
 Repro: https://github.com/bvaughn/test-named-hooks
 
 create-react-app bug report: https://github.com/facebo
   - Issue: https://github.com/facebook/react/issues/21868
   - Fix PR #21874 — DevTools: Named hooks supports "cheap-module-source-map"
   - PR: https://github.com/facebook/react/pull/21874
   - Code excerpts:
     - packages/react-devtools-extensions/package.json:     "sourcemap-codec": "^1.4.8",
     - packages/react-devtools-extensions/src/__tests__/__source__/__compiled__/no-columns/ComponentWithCustomHook.js: "use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.Component = Component;

var _react = _interopRequireWildcard(require("react"));

function _getRequireWildcardCac

179. Issue #21853 — Suspense layout effects: Failing test case (closed 2021-07-14T17:37:10Z)
   - Issue detail: The key components to this are:
 1. State updater function as a `ref` setter.
 2. Render-phase update, e.g. mirrored props-to-state ([not a generally recommended patter](https://reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html#anti-pattern-unconditionally-copying-props-to-state)).
 3. Suspend in an update ([also not a common or recommended pattern](https://github.com/reactwg/react-18/discussions/31)).
 
 This causes a cycle:
 1. Ref gets set to null by React, which schedules
   - Issue: https://github.com/facebook/react/pull/21853
   - Fix PR #21875 — [Bugfix] Don't hide/unhide unless visibility changes
   - PR: https://github.com/facebook/react/pull/21875
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberCommitWork.new.js:   Visibility,
  if ((finishedWork.flags & LayoutMask) !== NoFlags) {
        commitSuspenseCallback(finishedWork);
      commitSuspenseCallback(finishedWork);
function commitSuspenseCallback(finishedW
     - packages/react-reconciler/src/ReactFiberCommitWork.old.js:   Visibility,
  if ((finishedWork.flags & LayoutMask) !== NoFlags) {
        commitSuspenseCallback(finishedWork);
      commitSuspenseCallback(finishedWork);
function commitSuspenseCallback(finishedW

180. Issue #21876 — [React 18] Bug: `Maximum update depth exceeded` on the `ref` prop when suspending (closed 2021-07-14T17:37:11Z)
   - Issue detail: Functional `ref` prop throws a `Maximum update depth exceeded` error when suspending.
 
 React version: `18.0.0-alpha-464f27572-20210713`
 
 ## Steps To Reproduce
 
 1. Click on the `suspend` button: https://codesandbox.io/s/ref-set-too-many-times-jm0c3?file=/src/App.js.
 
 ## The current behavior
 
 Clicking on the `suspend` button throws a `Maximum update depth exceeded` error.
 
 ## The expected behavior
 
 Clicking on the `suspend` button suspends.
   - Issue: https://github.com/facebook/react/issues/21876
   - Fix PR #21875 — [Bugfix] Don't hide/unhide unless visibility changes
   - PR: https://github.com/facebook/react/pull/21875
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberCommitWork.new.js:   Visibility,
  if ((finishedWork.flags & LayoutMask) !== NoFlags) {
        commitSuspenseCallback(finishedWork);
      commitSuspenseCallback(finishedWork);
function commitSuspenseCallback(finishedW
     - packages/react-reconciler/src/ReactFiberCommitWork.old.js:   Visibility,
  if ((finishedWork.flags & LayoutMask) !== NoFlags) {
        commitSuspenseCallback(finishedWork);
      commitSuspenseCallback(finishedWork);
function commitSuspenseCallback(finishedW

181. Issue #21870 — [DevTools] Handle sources that contain the string "sourceMappingURL=" (closed 2021-07-13T20:39:29Z)
   - Issue detail: It's possible that a source file may contain the string "sourceMappingURL=" _in the source_ (not part of the source map). For example, if we were to parse the source code for `parseHookNames`, the regex `/ ?sourceMappingURL=([^\s'"]+)/gm` would match itself.
 
 We should have some logic in place for filtering out invalid matches like this. I think the rule should be:
 1. Multiple inline source maps may appear in a file/bundle. Logic exists to parse these and compare the `sources` field to the pa
   - Issue: https://github.com/facebook/react/issues/21870
   - Fix PR #21871 — DevTools: Ignore multiple sourceMappingUrls for external source maps
   - PR: https://github.com/facebook/react/pull/21871
   - Code excerpts:
     - packages/react-devtools-extensions/src/__tests__/__source__/ContainingStringSourceMappingURL.js: /**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * @flow
 */
     - packages/react-devtools-extensions/src/__tests__/__source__/__compiled__/bundle/index.js: 
  const [count, setCount] = React.useState(0);
  return /*#__PURE__*/React__default.createElement("div", null, /*#__PURE__*/React__default.createElement("p", null, "You clicked ", count, " times"), /

182. Issue #21792 — [DevTools] Use line number and column number to match hook (closed 2021-07-13T17:28:01Z)
   - Issue detail: DevTools named hook parsing logic currently matches AST nodes using the original line number:
 https://github.com/facebook/react/blob/ed6c091fe961a3b95e956ebcefe8f152177b1fb7/packages/react-devtools-extensions/src/parseHookNames.js#L341-L346
 
 But this may not be sufficient, as mentioned in comment https://github.com/facebook/react/pull/21641#discussion_r662951987:
 > Are we assuming that a line number is sufficient to identify a hook call? Seems like that assumption breaks down in edge cases:
   - Issue: https://github.com/facebook/react/issues/21792
   - Fix PR #21865 — Adjust Error stack columns numbers by 1
   - PR: https://github.com/facebook/react/pull/21865
   - Code excerpts:
     - packages/react-devtools-extensions/src/astUtils.js:   // Column numbers are representated differently between tools/engines.
  // Error.prototype.stack columns are 1-based (like most IDEs) but ASTs are 0-based.
  //
  // In practice this will probably 
     - packages/react-devtools-extensions/src/parseHookNames.js:         // Error.prototype.stack columns are 1-based (like most IDEs) but ASTs are 0-based.
        // Error.prototype.stack columns are 1-based (like most IDEs) but ASTs are 0-based.

183. Issue #21834 — [DevTools] Skip loading and parsing source for unnamed built-in hooks (closed 2021-07-08T20:46:17Z)
   - Issue detail: Hooks like `useEffect` or `useLayoutEffect` will _never_ have names, so if a the only hooks for a given source file are these "unnamed" built-in hooks, we should skip loading the source code.
   - Issue: https://github.com/facebook/react/issues/21834
   - Fix PR #21835 — DevTools: Don't load source files contaning only unnamed hooks
   - PR: https://github.com/facebook/react/pull/21835
   - Code excerpts:
     - packages/react-devtools-extensions/src/__tests__/__source__/__untransformed__/ComponentWithExternalUseEffect.js: /**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * @flow
 */
     - packages/react-devtools-extensions/src/__tests__/__source__/__untransformed__/useCustom.js: /**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * @flow
 */

184. Issue #21819 — [DevTools] Improve "retry" function for inspected component props/state/hooks (closed 2021-07-08T18:07:15Z)
   - Issue detail: Currently if an error occurs when inspecting a component, an error overlay is shown in the right hand side of DevTools along with a "dismiss" button to allow the inspection to be retried. However, currently this "retry" does not clear the entry from the cache and so it will immediately fail again if the same component is re-selected. We should clear the cache entry so that we actually retry when the modal is dismissed
   - Issue: https://github.com/facebook/react/issues/21819
   - Fix PR #21821 — Reset inspected element cache in the event of an error
   - PR: https://github.com/facebook/react/pull/21821
   - Code excerpts:
     - packages/react-devtools-shared/src/devtools/views/Components/InspectedElementContext.js:   let inspectedElement = null;
     - packages/react-devtools-shared/src/devtools/views/Components/InspectedElementErrorBoundary.js: import {
  useCallback,
  useContext,
  unstable_useCacheRefresh as useCacheRefresh,
} from 'react';
import {clearCacheBecauseOfError} from '../../../inspectedElementCache';

  const refresh = useCach

185. Issue #21822 — [DevTools] Make sure named hooks Suspense cache is persisting between elements (closed 2021-07-08T17:54:17Z)
   - Issue detail: It currently looks like the `map.get(element)` returns `undefined` even for previously-loaded elements. Are we evicting from the cache prematurely? Why?
 
 Our second level caching (inside of `parseHookNames`) is working but this is still resulting in a lot of unnecessary work.
   - Issue: https://github.com/facebook/react/issues/21822
   - Fix PR #21831 — DevTool: hook names cache no longer loses entries between selection
   - PR: https://github.com/facebook/react/pull/21831
   - Code excerpts:
     - packages/react-devtools-extensions/src/parseHookNames.js: import {getHookSourceLocationKey} from 'react-devtools-shared/src/hookNamesCache';
    const locationKey = getHookSourceLocationKey(hookSource);
      // Can't be null because getHookSourceLocationKey
     - packages/react-devtools-shared/src/devtools/views/Components/InspectedElementContext.js: import {
  hasAlreadyLoadedHookNames,
  loadHookNames,
} from 'react-devtools-shared/src/hookNamesCache';
  const element =
    selectedElementID !== null ? store.getElementByID(selectedElementID) : n

186. Issue #21817 — [DevTools] Named hooks error badge (closed 2021-07-07T20:27:39Z)
   - Issue detail: The named hooks cache returns `Array<string | null> | null` The first (mixed array of string and null) indicates an overall success, even if some names couldn't be inferred. The second indicates an error (e.g. couldn't locate or load source map).
 
 In the event of the 2nd response type, the UI currently does nothing (falls back to default) but we _should_ show an error badge (maybe a disabled but red icon with a tooltip saying there was an error) since it's a confusing user experience to just d
   - Issue: https://github.com/facebook/react/issues/21817
   - Fix PR #21820 — DevTools show error icon when hook name parsing fails
   - PR: https://github.com/facebook/react/pull/21820
   - Code excerpts:
     - packages/react-devtools-shared/src/devtools/views/Components/InspectedElementHooksTree.css: }

.ToggleError {
  color: var(--color-error-text);

187. Issue #21793 — [DevTools] Support Flow syntax for named hooks parsing (closed 2021-07-07T18:29:41Z)
   - Issue detail: DevTools tells Babel to parse the source code using "jsx" and "typescript" plug-ins:
 https://github.com/facebook/react/blob/ed6c091fe961a3b95e956ebcefe8f152177b1fb7/packages/react-devtools-extensions/src/parseHookNames.js#L446-L462
 
 This will work for some simple usages of Flow, but syntax may diverge and cause the parsing to fail.
 
 Let's scan the source code for a `@flow` pragma and pass "flow" instead of "typescript" if one is found.
 
 ---
 
 We should also add tests for both Flow and Ty
   - Issue: https://github.com/facebook/react/issues/21793
   - Fix PR #21815 — DevTools named hooks: Support FLow syntax
   - PR: https://github.com/facebook/react/pull/21815
   - Code excerpts:
     - packages/react-devtools-extensions/src/parseHookNames.js:       // TypeScript is the most commonly used typed JS variant so let's default to it
      // unless we detect explicit Flow usage via the "@flow" pragma.
      const plugin =
        originalSourceC

188. Issue #21811 — [DevTools] Don't serialize hook source fileNames (URLs) (closed 2021-07-07T18:24:18Z)
   - Issue detail: This can cause long file names (URLs) to be truncated which in turn will break named hooks code (since it needs to load those file names).
   - Issue: https://github.com/facebook/react/issues/21811
   - Fix PR #21814 — DevTooks: Don't dehydrate hook source fileNames
   - PR: https://github.com/facebook/react/pull/21814
   - Code excerpts:
     - packages/react-devtools-extensions/src/parseHookNames.js:           if (!url.startsWith('http') && !url.startsWith('/')) {
     - packages/react-devtools-shared/src/backend/renderer.js: 
          if (
            path[path.length - 2] === 'hookSource' &&
            path[path.length - 1] === 'fileName'
          ) {
            // It's important to preserve the full file name (URL) 

189. Issue #21794 — [DevTools] Handle bundles (multi sources) when parsing hook names (closed 2021-07-07T17:07:58Z)
   - Issue detail: DevTools hooks name parsing code currently assumes a single "source" for the source map:
 https://github.com/facebook/react/blob/ed6c091fe961a3b95e956ebcefe8f152177b1fb7/packages/react-devtools-extensions/src/parseHookNames.js#L428-L434
 
 But as pointed out by comment https://github.com/facebook/react/pull/21641#discussion_r662947994:
 > If the compiled code is a bundle, it can consist of multiple modules - what guarantees that `sources[0]` is the correct module for the hook we'll be looking up
   - Issue: https://github.com/facebook/react/issues/21794
   - Fix PR #21790 — [WIP] DevTools: Support named hooks for >1 module in a bundle
   - PR: https://github.com/facebook/react/pull/21790
   - Code excerpts:
     - packages/react-devtools-extensions/package.json:     "acorn-jsx": "^5.2.0",
    "rollup": "^1.19.4",
    "rollup-plugin-babel": "^4.0.1",
    "rollup-plugin-commonjs": "^9.3.4",
    "rollup-plugin-node-resolve": "^2.1.1",
     - packages/react-devtools-extensions/src/__tests__/__source__/__compiled__/bundle/index.js: 'use strict';

Object.defineProperty(exports, '__esModule', { value: true });

function _interopDefault (ex) { return (ex && (typeof ex === 'object') && 'default' in ex) ? ex['default'] : ex; }

var R

190. Issue #12411 — UNSAFE_* Lifecycle hooks don't run if getDerivedStateFromProps is present (closed 2018-03-22T18:16:55Z)
   - Issue detail: https://codesandbox.io/s/xl7k7j1k6w
 
 Not sure if this is intended or not, the longer term existence of these hooks suggested to me that they have their purposes still, so might be needed in conjunction with gDSFP. The particular use-case that caused me to discover this was a migrating: https://github.com/react-bootstrap/react-bootstrap/blob/master/src/Dropdown.js#L137 where document focus needs to be checked _prior_ to an update flushing because the update changes visual state and drops focus.
   - Issue: https://github.com/facebook/react/issues/12411
   - Fix PR #12419 — Expanded DEV-only warnings for gDSFP and legacy lifecycles
   - PR: https://github.com/facebook/react/pull/12419
   - Code excerpts:
     - packages/react-dom/src/__tests__/ReactComponentLifeCycle-test.js:       'Unsafe legacy lifecycles will not be called for components using the new getDerivedStateFromProps() API.',
      'Unsafe legacy lifecycles will not be called for components using the new getDer
     - packages/react-reconciler/src/ReactFiberClassComponent.js: let didWarnAboutLegacyLifecyclesAndDerivedState;
  didWarnAboutLegacyLifecyclesAndDerivedState = {};
      if (typeof ctor.getDerivedStateFromProps === 'function') {
        if (state === null) {
    

191. Issue #21676 — Bug: Layout effects don't re-fire in 18 on Suspense re-showing (closed 2021-06-16T23:44:44Z)
   - Issue detail: Intended behavior: https://github.com/reactwg/react-18/discussions/31
 
 Sandbox: https://codesandbox.io/s/react-18-layouteffect-semantics-forked-m02w5
 
 Expected: when suspended content is hidden and then shown, we get layout cleanup followed by layout setup.
 Actual: only layout cleanup happens.
   - Issue: https://github.com/facebook/react/issues/21676
   - Fix PR #21694 — Fix for failed Suspense layout semantics
   - PR: https://github.com/facebook/react/pull/21694
   - Code excerpts:
     - packages/react-reconciler/src/ReactFiberCommitWork.new.js:         // TODO (Offscreen) Also check: subtreeFlags & LayoutMask
        const current = fiber.alternate;
        const wasHidden = current !== null && current.memoizedState !== null;
        const n
     - packages/react-reconciler/src/ReactFiberCommitWork.old.js:         // TODO (Offscreen) Also check: subtreeFlags & LayoutMask
        const current = fiber.alternate;
        const wasHidden = current !== null && current.memoizedState !== null;
        const n

192. Issue #21654 — [DevTools Bug] Crash when inspecting component using a hook that returns a Proxy (closed 2021-06-11T14:15:48Z)
   - Issue detail: ### Website or app  https://codesandbox.io/s/react-devtools-crash-with-proxy-in-hook-dxd32?file=/src/App.tsx  ### Repro steps  Provided is a code sandbox with a very simplified version of the code which triggered this bug.
 
 1. Open the code sandbox app in a new window
 2. Open developer tools
 3. Select the "Components" tab
 4. Click on the "App" component
 
 Observe that devtools crashed, and the console prints out an error similar to this:
 ```
 Uncaught TypeError: [Symbol.iterator]() return
   - Issue: https://github.com/facebook/react/issues/21654
   - Fix PR #21660 — DevTools can inspect Proxies that return broken iterator functions
   - PR: https://github.com/facebook/react/pull/21660
   - Code excerpts:
     - packages/react-devtools-shared/src/__tests__/inspectedElement-test.js:   // See github.com/facebook/react/issues/21654
  it('should support Proxies that dont return an iterator', async () => {
    const Example = () => null;
    const proxy = new Proxy(
      {},
      {
     - packages/react-devtools-shared/src/utils.js:         const iterator = data[Symbol.iterator]();
        if (!iterator) {
          // Proxies might break assumptoins about iterators.
          // See github.com/facebook/react/issues/21654
       

193. Issue #18768 — Bug: `React.lazy` throws undefined instead of an `Error` object (closed 2021-06-07T21:47:18Z)
   - Issue detail: React version: 16.13.1
 
 ## Steps To Reproduce
 
 ```js
 import React, { Suspense, lazy } from "react";
 
 const Async = lazy(() => {}); // <------
 
 let App = () => {
 	return (
 		<Suspense fallback={"Loading"}>
 			<Async />
 		</Suspense>
 	);
 };
 
 export default App;
 ```
 
 Link to code example: https://codesandbox.io/s/elegant-fermi-bxwtb
 
 Might be related to https://github.com/facebook/react/issues/15019, https://github.com/facebook/react/pull/15222
 
 ## Context
 
 I know that thi
   - Issue: https://github.com/facebook/react/issues/18768
   - Fix PR #21642 — Fix Issue with Undefined Lazy Imports By Refactoring Lazy Initialization Order
   - PR: https://github.com/facebook/react/pull/21642
   - Code excerpts:
     - packages/react-reconciler/src/__tests__/ReactLazy-test.internal.js:     expect(Scheduler).toFlushAndThrow('Element type is invalid');
      expect(console.error).toHaveBeenCalledTimes(3);
     - packages/react/src/ReactLazy.js:   _result: {default: T},
    // This might throw either because it's missing or throws. If so, we treat it
    // as still uninitialized and try again next time. Which is the same as what
    // happe

194. Issue #21558 — Remove _debugID field from Fiber (closed 2021-05-26T20:53:19Z)
   - Issue detail: This DEV-only field was added in 836331ba5f69f2cc53b273ec073fae116db14302 by @sebmarkbage but it's not being used anymore to my knowledge.
   - Issue: https://github.com/facebook/react/issues/21558
   - Fix PR #21570 — Removed _debugID field from Fiber - Issue #21558
   - PR: https://github.com/facebook/react/pull/21570
   - Code excerpts:
     - packages/react-dom/src/__tests__/ReactFunctionComponent-test.js:     // Could not be differentiated (since owner is anonymous and no source location)
    ReactTestUtils.renderIntoDocument(<AnonymousParentNotUsingJSX />);
     - packages/react-reconciler/src/ReactFiber.new.js: 



195. Issue #21445 — Error: "Cannot add child "18903" to parent "18774" because parent node was not found in the Store." (closed 2021-05-25T18:49:05Z)
   - Issue detail: <!-- Please answer both questions below before submitting this issue. -->
 
 ### Which website or app were you using when the bug happened?
 
 Please provide a link to the URL of the website (if it is public), a CodeSandbox (https://codesandbox.io/s/new) example that reproduces the bug, or a project on GitHub that we can checkout and run locally.
 
 ### What were you doing on the website or app when the bug happened?
 
 If possible, please describe how to reproduce this bug on the website or app
   - Issue: https://github.com/facebook/react/issues/21445
   - Fix PR #21562 — DevTools: Support an element mounting before its owner
   - PR: https://github.com/facebook/react/pull/21562
   - Code excerpts:
     - packages/react-devtools-shared/src/__tests__/store-test.js:   // This test is not the same cause as what's reported on GitHub,
  // but the resulting behavior (owner mounting after descendant) is the same.
  // Thec ase below is admittedly contrived and relies
     - packages/react-devtools-shared/src/backend/renderer.js:       // Ideally we should call getFiberIDThrows() for _debugOwner,
      // since owners are almost always higher in the tree (and so have already been processed),
      // but in some (rare) instanc

196. Issue #21528 — [DevTools Bug]: Fast Refresh + DevTools breaks component inspection (closed 2021-05-20T15:24:09Z)
   - Issue detail: ### Website or app
 
 https://github.com/eps1lon/react-devtools-repro-no-matching-node/
 
 ### Repro steps
 
 1. `yarn start`
 2. Open `App.js`
 3. Uncomment the `useEffect` block
 4. Click to inspect "Component" in DevTools
 5. Error: "_Could not inspect element with id 5_"
 
 Originally reported in https://github.com/facebook/react/issues/21436#issuecomment-835406075
 
 ---
 
 https://user-images.githubusercontent.com/12292047/117544707-e6a6cd80-b022-11eb-9f8f-bb8cfd9f7743.mp4
 
 ### How often
   - Issue: https://github.com/facebook/react/issues/21528
   - Fix PR #21536 — Fix edge-case Fast Refresh bug that caused Fibers with warnings/errors to be untracked prematurely
   - PR: https://github.com/facebook/react/pull/21536
   - Code excerpts:
     - packages/react-devtools-shared/src/__tests__/inspectedElement-test.js:       if (id == null) {
        throw Error(`Element at index "${index}"" not found in store`);
      }
        await getErrorsAndWarningsForElementAtIndex(0),
        await getErrorsAndWarningsForEle
     - packages/react-devtools-shared/src/backend/renderer.js:   // Tracks Fibers with recently changed number of error/warning messages.
  // These collections store the Fiber rather than the ID,
  // in order to avoid generating an ID for Fibers that never get 

197. Issue #21518 — [DevTools Bug]: console.log throws type error if one of the arguments is symbol (closed 2021-05-18T15:46:04Z)
   - Issue detail: ### Website or app  https://github.com/facebook/react/blob/0e100ed00fb52cfd107db1d1081ef18fe4b9167f/packages/react-devtools-shared/src/backend/utils.js#L199  ### Repro steps  This function will throw this error if one of the arguments is type of `symbol`.
 
 The error is swallowed [here](https://github.com/facebook/react/blob/22ab39be681251f1c0f257af7e636cb8debf31c4/packages/react-devtools-shared/src/backend/console.js#L194-L196) but it does interfere with debugging. When I run with the "pause o
   - Issue: https://github.com/facebook/react/issues/21518
   - Fix PR #21521 — Fixed another Symbol concatenation issue with DevTools format() util
   - PR: https://github.com/facebook/react/pull/21521
   - Code excerpts:
     - packages/react-devtools-shared/src/__tests__/utils-test.js: import {format} from 'react-devtools-shared/src/backend/utils';







  describe('format', () => {
    it('should format simple strings', () => {
      expect(format('a', 'b', 'c')).toEqual('a b c');
     - packages/react-devtools-shared/src/backend/utils.js:   // Symbols cannot be concatenated with Strings.
  let formatted: string =
    typeof maybeMessage === 'symbol'
      ? maybeMessage.toString()
      : '' + maybeMessage;

  // If the first argument 

