# vscode merged PRs referencing issues via "Fix #"
- entries: 211

1. Issue #275126 — Toggle model visibility has a 2 second lag (closed 2025-11-19T16:58:46Z)
   - Issue detail: Testing #274343 https://github.com/user-attachments/assets/8e0bde1c-b49f-498a-b98a-1e1ca8b01c65 Can we make this instant - without the lag?
   - Issue: https://github.com/microsoft/vscode/issues/275126
   - Fix PR #278383 — fix #275126
   - PR: https://github.com/microsoft/vscode/pull/278383
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatManagement/chatModelsViewModel.ts: +export type IViewModelEntry = IModelItemEntry | IVendorItemEntry; + +export interface IViewModelChangeEvent { +	at: number; +	removed: number; +	added: IViewModelEntry[]; +} + +	private readonly _onD
     - src/vs/workbench/contrib/chat/browser/chatManagement/chatModelsWidget.ts: +		private readonly viewModel: ChatModelsViewModel, +			run: async () => this.viewModel.toggleVisibility(entry) +		this.delayedFiltering = new Delayer<void>(200); +		const loadingPromise = this.extens

2. Issue #277782 — Settings: default formatter made it to the top (closed 2025-11-18T14:13:51Z)
   - Issue detail: <img width="634" height="288" alt="Image" src="https://github.com/user-attachments/assets/93a421be-c290-4d41-a97a-757f8d0edace" /> The default formatter was not first <img width="637" height="619" alt="Image" src="https://github.com/user-attachments/assets/6b02d092-b68c-46e7-849e-eec89bac1e46" /> Bisect points to...
   - Issue: https://github.com/microsoft/vscode/issues/277782
   - Fix PR #278103 — fix #277782
   - PR: https://github.com/microsoft/vscode/pull/278103
   - Code excerpts:     - src/vs/workbench/contrib/preferences/browser/settingsEditor2.ts: +		resolvedSettingsRoot.children!.unshift(getCommonlyUsedData(groups, toggleData?.commonlyUsed));
     - src/vs/workbench/contrib/preferences/browser/settingsLayout.ts: +import { ISetting, ISettingsGroup } from '../../../services/preferences/common/preferences.js'; +export function getCommonlyUsedData(settingGroups: ISettingsGroup[], commonlyUsed: string[] = defaultC

3. Issue #276882 — Do not make request to Marketplace for built in extensions (closed 2025-11-12T10:32:31Z)
   - Issue detail: Steps to reproduce: 1. Enable log level to trace 2. Open Shared Process Log 3. Install GitHub.vscode-pull-request-github extension 🐛 A request is made to `vscode.github-authentication` built in extension - `https://marketplace.visualstudio.com/_apis/public/gallery/vscode/vscode/github-authentication/latest` This is because the extension to be installed has dependency to this built in extension...
   - Issue: https://github.com/microsoft/vscode/issues/276882
   - Fix PR #276883 — fix #276882
   - PR: https://github.com/microsoft/vscode/pull/276883
   - Code excerpts:     - src/vs/platform/extensionManagement/common/abstractExtensionManagementService.ts: +			const dependecies: string[] = manifest.extensionDependencies ? manifest.extensionDependencies.filter(dep => !installed.some(e => areSameExtensions(e.identifier, { id: dep }))) : [];
     - src/vs/platform/extensionManagement/common/extensionGalleryService.ts: +		const resourceApi = this.getResourceApi(extensionGalleryManifest); +	private getResourceApi(extensionGalleryManifest: IExtensionGalleryManifest): { uri: string; fallback?: string } | undefined {

4. Issue #276579 — VS Code Insiders Install/Registry Links Broken for all servers – Likely URL Encoding Issue (closed 2025-11-11T16:01:09Z)
   - Issue detail: <!-- Please search existing issues to avoid creating duplicates --> <!-- Please attach logs to help us diagnose your issue --> ### Summary https://github.com/user-attachments/assets/fdfbf927-7ac1-4c4e-8f0f-c2ac1bdafc76 Attempting to install a server from the Github MCP [registry](https://github.com/mcp) via the VS Code Insiders registry links currently always returns a 404 error. Investigation...
   - Issue: https://github.com/microsoft/vscode/issues/276579
   - Fix PR #276591 — fix #276579
   - PR: https://github.com/microsoft/vscode/pull/276591
   - Code excerpts:     - src/vs/platform/mcp/common/mcpGalleryService.ts: +		return format2(latestVersionResourceUriTemplate, { name: encodeURIComponent(name) });

5. Issue #278478 — Can't approve/allow input for terminal (closed 2025-11-21T18:21:48Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/278478
   - Fix PR #278824 — fix output monitor bug
   - PR: https://github.com/microsoft/vscode/pull/278824
   - Code excerpts:     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/tools/monitoring/outputMonitor.ts: +		let instanceDisposedDisposable: IDisposable = Disposable.None; +			let settled = false; +			const settle = (value: boolean, state: OutputMonitorState) => { +				if (settled) { +					return; +				} 
     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/tools/monitoring/types.ts: +	instance: Pick<ITerminalInstance, 'sendText' | 'instanceId' | 'onDidInputData' | 'onDisposed' | 'onData' | 'focus' | 'registerMarker'>;

6. Issue #275104 — Open the model editor pinned (closed 2025-11-10T10:50:59Z)
   - Issue detail: Testing #274343 I would not expect the editor to be in preview: <img width="249" height="103" alt="Image" src="https://github.com/user-attachments/assets/5f753088-c8f0-46bc-b292-e64c8f161141" />
   - Issue: https://github.com/microsoft/vscode/issues/275104
   - Fix PR #276459 — fix #275104
   - PR: https://github.com/microsoft/vscode/pull/276459
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatManagement/chatManagement.contribution.ts: +		return editorGroupsService.activeGroup.openEditor(new ModelsManagementEditorInput(), { pinned: true });

7. Issue #277080 — Leaked disposable: `ToolSet.addTool` (closed 2025-11-13T13:43:38Z)
   - Issue detail: ``` lifecycle.js:24 [LEAKED DISPOSABLE] Error: CREATED via: at GCBasedDisposableTracker.trackDisposable (vscode-file://vscode…/lifecycle.js:28:23) at trackDisposable (vscode-file://vscode…lifecycle.js:204:24) at new FunctionDisposable (vscode-file://vscode…/lifecycle.js:281:9) at toDisposable (vscode-file://vscode…lifecycle.js:301:12) at ToolSet.addTool (vscode-...
   - Issue: https://github.com/microsoft/vscode/issues/277080
   - Fix PR #277127 — Fix addTool leaks
   - PR: https://github.com/microsoft/vscode/pull/277127
   - Code excerpts:     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/terminal.chatAgentTools.contribution.ts: +		this._register(runCommandsToolSet.addTool(GetTerminalOutputToolData)); +			this._register(runCommandsToolSet.addTool(runInTerminalToolData)); +		this._register(runCommandsToolSet.addTool(GetTermina

8. Issue #275478 — MCP related actions need to hide when AI features are disabled (closed 2025-11-07T09:40:09Z)
   - Issue detail: <img width="713" height="210" alt="Image" src="https://github.com/user-attachments/assets/28211e3c-89b2-4972-a2e1-fd62ac4a71d4" /> <img width="363" height="99" alt="Image" src="https://github.com/user-attachments/assets/b7329568-b261-4ace-9876-e4bcd3108130" /> @sandy081 there is actually a smoke test we can then update to include the `mcp` term:...
   - Issue: https://github.com/microsoft/vscode/issues/275478
   - Fix PR #276022 — fix #275478
   - PR: https://github.com/microsoft/vscode/pull/276022
   - Code excerpts:     - src/vs/workbench/contrib/mcp/browser/mcpCommands.ts: +			precondition: ContextKeyExpr.and(McpContextKeys.toolsCount.greater(0), ChatContextKeys.Setup.hidden.negate()), +			precondition: ContextKeyExpr.and(HasInstalledMcpServersContext, ChatContextKeys.S
     - src/vs/workbench/contrib/mcp/browser/mcpServersView.ts: +				when: ContextKeyExpr.and(DefaultViewsContext, HasInstalledMcpServersContext, ChatContextKeys.Setup.hidden.negate()), +				when: ContextKeyExpr.and(SearchMcpServersContext, ChatContextKeys.Setup.h

9. Issue #276852 — Leaked disposable: `RunSubagentTool` (closed 2025-11-12T19:48:46Z)
   - Issue detail: ``` [LEAKED DISPOSABLE] Error: CREATED via: at GCBasedDisposableTracker.trackDisposable (vscode-file://vscode-app/Users/bpasero/Development/Microsoft/vscode/out/vs/base/common/lifecycle.js:28:23) at trackDisposable (vscode-file://vscode-app/Users/bpasero/Development/Microsoft/vscode/out/vs/base/common/lifecycle.js:204:24) at new Disposable (vscode-file://vscode-...
   - Issue: https://github.com/microsoft/vscode/issues/276852
   - Fix PR #276986 — Fix leaked disposable
   - PR: https://github.com/microsoft/vscode/pull/276986
   - Code excerpts:     - src/vs/workbench/contrib/chat/common/tools/tools.ts: +		const runSubagentTool = this._register(instantiationService.createInstance(RunSubagentTool));

10. Issue #275674 — Copilot Usage does not show correct stats (closed 2025-11-06T08:28:38Z)
   - Issue detail: 1. Login to GH Copilot in VS Code using your FREE account 2. Click on the status bar Copilot Usage 3. Notice that the stats say Included 🐛 I would expect to see how many chat / premium requests I have left <img width="403" height="423" alt="Image" src="https://github.com/user-attachments/assets/1aa50eb1-57b2-475c-8c83-f6349981fff1" />
   - Issue: https://github.com/microsoft/vscode/issues/275674
   - Fix PR #275759 — fix #275674
   - PR: https://github.com/microsoft/vscode/pull/275759
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatStatus.ts: +import { safeIntl } from '../../../../base/common/date.js'; +import { language } from '../../../../base/common/platform.js'; +import { ChatEntitlement, ChatEntitlementService, IChatEntitlementService

11. Issue #275160 — Unclear what the add models button does (closed 2025-11-05T17:55:22Z)
   - Issue detail: Testing #274343 1. Click add models button 2. Click a provider 3. 🤔 Nothing It also changes what providers are shown when filters are applied
   - Issue: https://github.com/microsoft/vscode/issues/275160
   - Fix PR #275629 — fix #275160
   - PR: https://github.com/microsoft/vscode/pull/275629
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatManagement/chatModelsWidget.ts: +		const configuredVendors = new Set(this.viewModel.getConfiguredVendors().map(cv => cv.vendorEntry.vendor)); +		const vendorsWithoutModels = vendors.filter(v => !configuredVendors.has(v.vendor));

12. Issue #275099 — Cannot press `Escape` to close this suggest widget (closed 2025-11-05T13:50:43Z)
   - Issue detail: Testing #274343 <img width="430" height="170" alt="Image" src="https://github.com/user-attachments/assets/ecc4a94b-fa4b-4de2-a9f5-f91a46e15654" /> Pressing `Escape`, nothing happens.
   - Issue: https://github.com/microsoft/vscode/issues/275099
   - Fix PR #275564 — fix #275099
   - PR: https://github.com/microsoft/vscode/pull/275564
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatManagement/chatManagement.contribution.ts: +import { KeyCode } from '../../../../../base/common/keyCodes.js'; +import { KeybindingWeight } from '../../../../../platform/keybinding/common/keybindingsRegistry.js'; +import { IEditorService } from
     - src/vs/workbench/contrib/chat/browser/chatManagement/chatManagementEditor.ts: +import { IContextKey, IContextKeyService } from '../../../../../platform/contextkey/common/contextkey.js'; +import { CONTEXT_MODELS_EDITOR } from '../../common/constants.js'; +	private readonly inMod

13. Issue #275092 — Rename manage models editor (closed 2025-11-05T11:49:19Z)
   - Issue detail: Testing #274343 <img width="275" height="106" alt="Image" src="https://github.com/user-attachments/assets/3dee4eb3-5203-431d-8c4a-116ff5fea3c6" /> I would bring the name closer to the name of the action that brought me here. We typically do not use "Copilot" nor its icon.
   - Issue: https://github.com/microsoft/vscode/issues/275092
   - Fix PR #275536 — fix #275092
   - PR: https://github.com/microsoft/vscode/pull/275536
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatManagement/chatManagementEditorInput.ts: +const ModelsManagementEditorIcon = registerIcon('models-management-editor-label-icon', Codicon.settings, nls.localize('modelsManagementEditorLabelIcon', 'Icon of the Models Management editor label.')

14. Issue #275340 — Searching for a hidden advanced setting is case sensitive (closed 2025-11-05T11:09:01Z)
   - Issue detail: Testing #274344 Searching for `terminal.integrated.developer.devMode` reveals the advanced setting, but `terminal.integrated.developer.devmode` does not. This seems overly specific and I think we should still show the advanced setting in this case.
   - Issue: https://github.com/microsoft/vscode/issues/275340
   - Fix PR #275531 — fix #275340
   - PR: https://github.com/microsoft/vscode/pull/275531
   - Code excerpts:     - src/vs/workbench/contrib/preferences/browser/settingsEditor2.ts: +		if (this.viewState.query?.toLowerCase().includes(setting.key.toLowerCase())) {

15. Issue #242367 — In Inspect Token and Scopes, the character count doesn't represent the number of characters in the scope (closed 2025-11-15T13:48:51Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/242367
   - Fix PR #277628 — Fix character count rendering
   - PR: https://github.com/microsoft/vscode/pull/277628
   - Code excerpts:     - src/vs/workbench/contrib/codeEditor/browser/inspectEditorTokens/inspectEditorTokens.ts: +		const semTokenLength = semanticTokenInfo && this._model.getValueLengthInRange(semanticTokenInfo.range); +		const tmTokenLength = textMateTokenInfo && (textMateTokenInfo.token.endIndex - textMateTok

16. Issue #203945 — Scroll position is revealed only after delay (closed 2025-11-09T08:23:40Z)
   - Issue detail: When I am horizontally scrolled and goto definition to another editor and then close that editor, I am first put into the beginning of the line and then scrolled to where I was. ![Image](https://github.com/microsoft/vscode/assets/900690/3ad53a13-45e9-4b8a-9dca-8545d82693d9)
   - Issue: https://github.com/microsoft/vscode/issues/203945
   - Fix PR #276346 — Fix missing NOT
   - PR: https://github.com/microsoft/vscode/pull/276346
   - Code excerpts:     - src/vs/editor/browser/viewParts/viewLines/viewLines.ts: +		if (!this._asyncUpdateLineWidths.isScheduled()) {

17. Issue #275388 — `chatTerminalToolProgressPart.ts` —  Trying to add a disposable to a DisposableStore (closed 2025-11-06T21:24:31Z)
   - Issue detail: Seeing this after running some terminal commands in chat ``` lifecycle.ts:477 Error: Trying to add a disposable to a DisposableStore that has already been disposed of. The added object will be leaked! at r2i.add (lifecycle.ts:477:18) at _rt.D (lifecycle.ts:555:22) at _rt.P (chatTerminalToolProgressPart.ts:260:41) at s (chatTerminalToolProgressPart.ts:180:9) at _rt.L...
   - Issue: https://github.com/microsoft/vscode/issues/275388
   - Fix PR #275878 — fix disposable leak
   - PR: https://github.com/microsoft/vscode/pull/275878
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts: +		const initialInstance = await this._terminalChatService.getTerminalInstanceByToolSessionId(terminalToolSessionId); +		await attachInstance(initialInstance); +		if (this._store.isDisposed) { +			ret

18. Issue #274281 — Manage Language Models: Too many commands (closed 2025-10-31T09:36:28Z)
   - Issue detail: It's confusing that there are 3 commands regarding Managing Language Models. I suggest only having one which leads to your new view. From there the user should be able to perform the same actions as the other commands. <img width="649" height="117" alt="Image" src="https://github.com/user-attachments/assets/553be836-1e47-4453-b4da-79715f9ff4d9" />
   - Issue: https://github.com/microsoft/vscode/issues/274281
   - Fix PR #274295 — fix #274281
   - PR: https://github.com/microsoft/vscode/pull/274295
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatManagement/chatManagement.contribution.ts: +			title: localize2('openAiManagement', "Manage Language Models (Preview)"),

19. Issue #251874 — terminal.integrated.mouseWheelZoom": true This configuration is repeated with the scroll bar (closed 2025-11-21T18:16:52Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/251874
   - Fix PR #278663 — Fix terminal mouse wheel zoom interference with scrollbar
   - PR: https://github.com/microsoft/vscode/pull/278663
   - Code excerpts:     - src/vs/workbench/contrib/terminalContrib/zoom/browser/terminal.zoom.contribution.ts: +import { Disposable, MutableDisposable } from '../../../../../base/common/lifecycle.js'; +import * as dom from '../../../../../base/browser/dom.js'; +		const wheelListener = (browserEvent: WheelEvent

20. Issue #274322 — Refactor ChatTerminalToolProgressPart to make simpler (closed 2025-11-14T15:47:52Z)
   - Issue detail: https://github.com/microsoft/vscode/pull/273175 really ramped up how complex `ChatTerminalToolProgressPart` is, consider what we can pull out and simplify. For example the part that does the actual rendering of the output could be its own class such that it's not intermingled with the rest of the part.
   - Issue: https://github.com/microsoft/vscode/issues/274322
   - Fix PR #277234 — extract `ChatTerminalToolOutputSection`, fix a bug
   - PR: https://github.com/microsoft/vscode/pull/277234
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts: +import { IChatCodeBlockInfo, IChatWidgetService } from '../../chat.js'; +import { Disposable, MutableDisposable, toDisposable, type IDisposable } from '../../../../../../base/common/lifecycle.js'; +i
     - src/vs/workbench/contrib/terminal/browser/terminal.ts: +	readonly elementIndex: number; +	readonly contentIndex: number; +	toggleOutputFromKeyboard(): Promise<void>;

21. Issue #277174 — Terminal tabs view shows when there's only a single terminal (closed 2025-11-13T17:50:17Z)
   - Issue detail: <img width="905" height="283" alt="Image" src="https://github.com/user-attachments/assets/584b47ef-e0bc-474f-a594-2851d50ce4e5" /> Before, it only showed when there was more than one cc @Tyriar
   - Issue: https://github.com/microsoft/vscode/issues/277174
   - Fix PR #277210 — fix when terminal tabs show 
   - PR: https://github.com/microsoft/vscode/pull/277210
   - Code excerpts:     - src/vs/workbench/contrib/terminal/browser/terminalTabbedView.ts: +		switch (hide) { +			case 'never': +				return true; +			case 'singleTerminal': +				if (this._terminalGroupService.instances.length > 1) { +					return true; +				} +				break; +			case 'singleGrou

22. Issue #278871 — HoverStyle.Mouse isn't working properly (closed 2025-11-21T23:06:03Z)
   - Issue detail: Passing this `style` into `setupDelayedHover` doesn't work currently as this style requires the mouse event to be set as the mouse position which doesn't happen currently. Repro: Try use a hover setup with `setupDelayedHover` and `style: HoverStyle.Mouse`, it'll show adjacent to the element, not beside the current cursor position.
   - Issue: https://github.com/microsoft/vscode/issues/278871
   - Fix PR #278877 — Fix HoverStyle.Mouse when setupDelayedHover is used
   - PR: https://github.com/microsoft/vscode/pull/278877
   - Code excerpts:     - src/vs/platform/hover/browser/hoverService.ts: +import { HoverStyle, isManagedHoverTooltipMarkdownString, type IHoverLifecycleOptions, type IHoverOptions, type IHoverTarget, type IHoverWidget, type IManagedHover, type IManagedHoverContentOrFactory

23. Issue #278790 — TypeError: Cannot read properties of undefined (reading 'toString') (closed 2025-11-21T21:23:13Z)
   - Issue detail: Just clicking on the action to create a new Chat Editor: ``` ERR Cannot read properties of undefined (reading 'toString'): TypeError: Cannot read properties of undefined (reading 'toString') at ChatModelStore.toKey (vscode-file://vscode-app/Users/bpasero/Development/Microsoft/vscode/out/vs/workbench/contrib/chat/common/chatServiceImpl.js:126:20) at ChatModelStore.get (vscode-file://vscode-...
   - Issue: https://github.com/microsoft/vscode/issues/278790
   - Fix PR #278867 — Fix possible NPE when opening chat editor
   - PR: https://github.com/microsoft/vscode/pull/278867
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatSessions/chatSessionTracker.ts: +			const editor = e.editor; +			const model = editor.sessionResource && this.chatService.getSession(editor.sessionResource);
     - src/vs/workbench/contrib/chat/browser/chatSessions/common.ts: +export function isChatSession(schemes: readonly string[], editor?: EditorInput): editor is ChatEditorInput {

24. Issue #274236 — SessionViewPane leaks dropdown, menu items (closed 2025-11-03T20:11:41Z)
   - Issue detail: Open VSCode and bring up chat sessions pane and create a new chat editor. Dropdown action and menu are leaked. ``` "[LEAKED DISPOSABLE] Error: CREATED via: at GCBasedDisposableTracker.trackDisposable (vscode-file://vscode-app/c:/Repos/vscode/out/vs/base/common/lifecycle.js:28:23) at trackDisposable (vscode-file://vscode-app/c:/Repos/vscode/out/vs/base/common/lifecycle.js:204:24) at new...
   - Issue: https://github.com/microsoft/vscode/issues/274236
   - Fix PR #274239 — Fix SessionViewPane leaks
   - PR: https://github.com/microsoft/vscode/pull/274239
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatSessions/view/sessionsViewPane.ts: +import { IAction, toAction } from '../../../../../../base/common/actions.js'; +		const actions = this.menuService.getMenuActions(MenuId.ChatSessionsMenu, this.scopedContextKeyService, { shouldForward

25. Issue #264451 — Tools Picker does not maintain expand/collapse state (closed 2025-11-19T01:50:29Z)
   - Issue detail: 1. Click on the tools picker to view the available tools list 2. Collapse the Built-In tools list, and click `OK` 3. Click on the tools picker again to view the available tools list 🐛 The Built-in tools list is expanded.
   - Issue: https://github.com/microsoft/vscode/issues/264451
   - Fix PR #277348 — Fix Tools Picker collapse state preservation
   - PR: https://github.com/microsoft/vscode/pull/277348
   - Code excerpts:     - src/vs/platform/quickinput/browser/tree/quickInputTreeController.ts: +import { IIdentityProvider } from '../../../../base/browser/ui/list/list.js'; +class QuickInputTreeIdentityProvider implements IIdentityProvider<IQuickTreeItem> { +	private readonly _elementIds = new

26. Issue #265096 — Leaked disposable: WebWorkerExtensionHost (closed 2025-10-25T20:56:32Z)
   - Issue detail: I ran OSS and toggled the AI enablement setting 2 times with Copilot installed: ``` [LEAKED DISPOSABLE] Error: CREATED via: at GCBasedDisposableTracker.trackDisposable (vscode-file://vscode-app/Users/bpasero/Development/Microsoft/vscode/out/vs/base/common/lifecycle.js:28:23) at trackDisposable (vscode-file://vscode-...
   - Issue: https://github.com/microsoft/vscode/issues/265096
   - Fix PR #273324 — Fixes #265096
   - PR: https://github.com/microsoft/vscode/pull/273324
   - Code excerpts:     - src/vs/workbench/services/extensions/common/lazyCreateExtensionHostManager.ts: +	override dispose(): void { +		if (!this._actual) { +			this._extensionHost.dispose(); +		} +		super.dispose(); +	} +

27. Issue #266103 — HTML tags are stripped from user messages in Chat (closed 2025-11-13T00:35:41Z)
   - Issue detail: Name: GitHub Copilot Chat Id: GitHub.copilot-chat Description: AI chat features powered by Copilot Version: 0.31.2025091003 Publisher: GitHub VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat Version: 1.104.0-insider Commit: f220831ea2d946c0dcb0f3eaa480eb435a2c1260 Date: 2025-09-09T22:13:39.933Z Electron: 37.3.1 ElectronBuildId: 12342881 Chromium:...
   - Issue: https://github.com/microsoft/vscode/issues/266103
   - Fix PR #276890 — fix: use childNodes instead of children in DOM.reset for markdown rendering. Fix #266103
   - PR: https://github.com/microsoft/vscode/pull/276890
   - Code excerpts:     - src/vs/base/browser/markdownRenderer.ts: +		DOM.reset(target, ...renderedContent.childNodes);

28. Issue #277582 — Task tool stuck on "press ctrl-c to detach" suggestion from deemon (closed 2025-11-17T22:12:46Z)
   - Issue detail: It's checking the output of the task and thinks the terminal is stuck. Since we have a problem matcher for this task, doesn't it know that the task is in a settled state? Not sure if something changed, I don't remember seeing this before. And I'm not sure how to continue, because I don't want to give any input. <img width="1014" height="423" alt="Image" src="https://github.com/user-...
   - Issue: https://github.com/microsoft/vscode/issues/277582
   - Fix PR #277890 — do not proceed when `Focus Terminal` option is taken until input has happened, prevent build daemon prompt
   - PR: https://github.com/microsoft/vscode/pull/277890
   - Code excerpts:     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/tools/monitoring/outputMonitor.ts: +import { Disposable, type IDisposable } from '../../../../../../../base/common/lifecycle.js'; +			const receivedTerminalInput = await this._requestFreeFormTerminalInput(token, this._execution, confir

29. Issue #272118 — `(Modified elsewhere)` tool-tip in `Settings` no longer links to modified scopes (closed 2025-11-18T02:34:24Z)
   - Issue detail: Type: <b>Bug</b> 1. Open VS Code and go to Settings (File > Preferences > Settings or press Ctrl+,). 2. Search for the setting ``` "editor.defaultFormatter" ``` 3. If the setting is modified by another source (e.g., workspace settings, a remote settings sync, or an extension), you should see the label ``` "(Modified elsewhere)" ``` next to the setting. 4. Hover your mouse over the `(Modified...
   - Issue: https://github.com/microsoft/vscode/issues/272118
   - Fix PR #274935 — Fix markdown setting scope links
   - PR: https://github.com/microsoft/vscode/pull/274935
   - Code excerpts:     - src/vs/base/browser/markdownRenderer.ts: +		Schemas.vscodeNotebookCell, +		// For links that are handled entirely by the action handler +		Schemas.internal,
     - src/vs/base/common/htmlContent.ts: +export function createMarkdownLink(text: string, href: string, title?: string, escapeTokens = true): string { +	return `[${escapeTokens ? escapeMarkdownSyntaxTokens(text) : text}](${href}${title ? ` 

30. Issue #272405 — Disposable leak: `ContributedChatSessionData` (closed 2025-11-03T22:16:34Z)
   - Issue detail: ``` [LEAKED DISPOSABLE] Error: CREATED via: at GCBasedDisposableTracker.trackDisposable (vscode-file://vscode-app/Users/bpasero/Development/Microsoft/vscode/out/vs/base/common/lifecycle.js:28:23) at trackDisposable (vscode-file://vscode-app/Users/bpasero/Development/Microsoft/vscode/out/vs/base/common/lifecycle.js:202:24) at new DisposableStore (vscode-file://vscode-...
   - Issue: https://github.com/microsoft/vscode/issues/272405
   - Fix PR #274892 — Fix leak for ContributedChatSessionData
   - PR: https://github.com/microsoft/vscode/pull/274892
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatSessions.contribution.ts: +import { raceCancellationError } from '../../../../base/common/async.js'; +class ContributedChatSessionData extends Disposable { +		super(); + + +		this._register(this.session.onWillDispose(() => { +

31. Issue #269173 — `Enable MCP Servers Marketplace?` modal setting link has ugly tooltip (closed 2025-10-02T09:52:49Z)
   - Issue detail: Testing #268911 Hovering over the setting link, I see this: <img width="822" height="383" alt="Image" src="https://github.com/user-attachments/assets/f702f6f4-0acd-4269-9c13-f8147c862dcc" />
   - Issue: https://github.com/microsoft/vscode/issues/269173
   - Fix PR #269504 — fix #269173
   - PR: https://github.com/microsoft/vscode/pull/269504
   - Code excerpts:     - src/vs/base/common/htmlContent.ts: +export function markdownCommandLink(command: { title: string; id: string; arguments?: unknown[]; tooltip?: string }, escapeTokens = true): string { +	return `[${escapeTokens ? escapeMarkdownSyntaxTok
     - src/vs/workbench/contrib/mcp/browser/mcpServersView.ts: +import { markdownCommandLink, MarkdownString } from '../../../../base/common/htmlContent.js'; +		const settingsCommandLink = markdownCommandLink({ id: 'workbench.action.openSettings', arguments: [`@i

32. Issue #272598 — [BUG] MCP registry URL allowed servers showing up as disabled on VSCode window reload (closed 2025-10-22T11:36:58Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/272598
   - Fix PR #272685 — fix #272598
   - PR: https://github.com/microsoft/vscode/pull/272685
   - Code excerpts:     - src/vs/platform/mcp/common/mcpGalleryManifest.ts: +	McpServerIdUri = 'McpServerIdUriTemplate',
     - src/vs/platform/mcp/common/mcpGalleryManifestService.ts: +	'v0', +	'v0.1', +		if (version === 'v0') { +			resources.push({ +				id: `${serversUrl}/{id}`, +				type: McpGalleryResourceType.McpServerIdUri +			}); +		} +

33. Issue #269218 — Alt hides the `+`? (closed 2025-10-01T19:36:26Z)
   - Issue detail: Steps to Reproduce: 1. Open chat 2. Hold Alt & release Alt 3. 🐛 New Chat goes away? https://github.com/user-attachments/assets/5abad38f-b2ff-47a4-b1fe-e3f8fcf982ea I think @digitarald did you make this change?
   - Issue: https://github.com/microsoft/vscode/issues/269218
   - Fix PR #269421 — Fix #269218
   - PR: https://github.com/microsoft/vscode/pull/269421
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/actions/chatClearActions.ts: +							icon: Codicon.newFile,

34. Issue #269032 — Browse MCP Servers icon is confusing (closed 2025-10-01T10:42:15Z)
   - Issue detail: Testing #268910 <img width="990" height="103" alt="Image" src="https://github.com/user-attachments/assets/2ae748a4-9164-40f5-908b-edd4e87d52a8" /> I think the globe usually means you'll be taken to your browser. I expected it to be the magnifying glass.
   - Issue: https://github.com/microsoft/vscode/issues/269032
   - Fix PR #269326 — fix #269032
   - PR: https://github.com/microsoft/vscode/pull/269326
   - Code excerpts:     - src/vs/workbench/contrib/mcp/browser/mcpCommands.ts: +			icon: Codicon.search,

35. Issue #269170 — Include help link on MCP extension welcome view? (closed 2025-10-01T10:18:48Z)
   - Issue detail: Testing #268911 <img width="592" height="456" alt="Image" src="https://github.com/user-attachments/assets/7c462584-c32f-42b8-ae95-7546b6bc8b30" /> Looking at this text as a new user, I have a few questions: 1. What is mcp and what does it add to VS Code? How can I use it once installed 2. What does enabling the marketplace do? Why do I need to enable it when the normal extension marketplace is...
   - Issue: https://github.com/microsoft/vscode/issues/269170
   - Fix PR #269315 — fix #269170
   - PR: https://github.com/microsoft/vscode/pull/269315
   - Code excerpts:     - src/vs/workbench/contrib/mcp/browser/mcpServersView.ts: +		const settingsCommandLink = createCommandUri('workbench.action.openSettings', { query: `@id:${mcpGalleryServiceEnablementConfig}` }).toString(); +			localize('mcp.welcome.descriptionWithLink', "Bro

36. Issue #269177 — MCP extension list doesn't show any info if no server are found (closed 2025-10-01T11:29:38Z)
   - Issue detail: Testing #268911 1. Enable the MCP gallery 2. Search for something that doesn't exist, such as `@mcp typescript` **bug** The view is blank: <img width="461" height="405" alt="Image" src="https://github.com/user-attachments/assets/72fdb9a6-b0c6-4728-acd9-42106dea7683" /> For extensions we show an alert about no results being found: <img width="343" height="215" alt="Image"...
   - Issue: https://github.com/microsoft/vscode/issues/269177
   - Fix PR #269304 — fix #269177
   - PR: https://github.com/microsoft/vscode/pull/269304
   - Code excerpts:     - src/vs/workbench/contrib/mcp/browser/mcpServersView.ts: +import { INotificationService, Severity } from '../../../../platform/notification/common/notification.js'; +import { alert } from '../../../../base/browser/ui/aria/aria.js'; +import { SeverityIcon } 

37. Issue #269205 — MCP gallery welcome view flashes with already installed servers (closed 2025-10-01T11:34:44Z)
   - Issue detail: Testing #268911 1) Have a mcp server installed 2) In setting disable gallery `"chat.mcp.gallery.enabled": false` 3) Reload window 4) See that MCP welcome view momentarily flashes before the `MCP Servers - Installed` view is loaded https://github.com/user-attachments/assets/8779c0c6-0a9e-4b76-8ab2-4bf1206e127d
   - Issue: https://github.com/microsoft/vscode/issues/269205
   - Fix PR #269297 — fix #269205
   - PR: https://github.com/microsoft/vscode/pull/269297
   - Code excerpts:     - src/vs/workbench/contrib/mcp/browser/mcpWorkbenchService.ts: +		mcpWorkbenchService.queryLocal().finally(() => { +			hasInstalledMcpServersContextKey.set(mcpWorkbenchService.local.length > 0); +			this._register(mcpWorkbenchService.onChange(() => hasInstalledMc

38. Issue #277669 — Cannot read properties of undefined (reading 'isExpanded') (closed 2025-11-17T23:20:05Z)
   - Issue detail: - Use the agent, run terminal commands - I see this error many times Looks like you are accessing `this._outputView.isExpanded` from the constructor before it has been instantiated ``` ERR Cannot read properties of undefined (reading 'isExpanded'): TypeError: Cannot read properties of undefined (reading 'isExpanded') at wot.Y (vscode-file://vscode-...
   - Issue: https://github.com/microsoft/vscode/issues/277669
   - Fix PR #277959 — ensure outputView is initialized before it can be referenced
   - PR: https://github.com/microsoft/vscode/pull/277959
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts: + +		const outputViewOptions: ChatTerminalToolOutputSectionOptions = { +			container: elements.output, +			title: elements.title, +			displayCommand, +			terminalData: this._terminalData, +			accessib

39. Issue #278048 — No auth flow from inline chat gets broken by welcome view open (closed 2025-11-18T11:25:14Z)
   - Issue detail: 1. code-insiders --transient 2. Turn on inlineChat v2 (might not be required) 3. Start the sign-in experience from inline chat 4. Notice how I get signed in, and the welcome view gets opened 🐛 My flow is broken. I would expect inline chat to remain in focus, and that I get results. https://github.com/user-attachments/assets/519cf3ed-81f8-46a4-8175-f388580cf723 fyi @cwebster-99 @jrieken
   - Issue: https://github.com/microsoft/vscode/issues/278048
   - Fix PR #278058 — No auth flow from inline chat gets broken by welcome view open (fix #278048)
   - PR: https://github.com/microsoft/vscode/pull/278058
   - Code excerpts:     - src/vs/workbench/contrib/welcomeGettingStarted/browser/gettingStarted.contribution.ts: +		const inactive = typeof optionsOrToSide === 'object' ? optionsOrToSide.inactive : false; +				options = { selectedCategory, selectedStep, showWelcome: false, preserveFocus: toSide ?? false, inactiv

40. Issue #277307 — Closing and reopening chat agent window hides chat history. (closed 2025-11-16T06:06:41Z)
   - Issue detail: In the October 2025 release, sometimes if I'm in the middle of making edits in Agent mode and I close the side chat panel using `Ctrl+Alt+b`, when I reopen it there is no chat history shown. If I attempt to bring it back by clicking on the chat history button, it says: > Switching chats will end your current edit session. Do you want to keep pending edits to 1 files? Restarting VS Code will...
   - Issue: https://github.com/microsoft/vscode/issues/277307
   - Fix PR #277670 — Skip updateElementHeight when ChatWidget is not visible
   - PR: https://github.com/microsoft/vscode/pull/277670
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatWidget.ts: +			if (this.tree.hasElement(e.element) && this.visible) { +			if (heightUpdated && lastItem && this.visible) {

41. Issue #273167 — Accept user action required action should have context key (closed 2025-10-27T14:50:53Z)
   - Issue detail: The accept chat action keybinding intentionally does not have a strict `when` clause so that it can be accepted from anywhere within the workbench. However, this causes the notification action with the same kb to not work. We should set the weight of notification one to be higher. ``` { "key": "ctrl+shift+a", "command": "workbench.action.chat.focusConfirmation", "when":...
   - Issue: https://github.com/microsoft/vscode/issues/273167
   - Fix PR #273568 — fix kb conflict
   - PR: https://github.com/microsoft/vscode/pull/273568
   - Code excerpts:     - src/vs/workbench/browser/parts/notifications/notificationsCommands.ts: +		weight: KeybindingWeight.WorkbenchContrib + 1,

42. Issue #270087 — Quick chat is broken (closed 2025-10-07T03:26:36Z)
   - Issue detail: <img width="687" height="170" alt="Image" src="https://github.com/user-attachments/assets/73067f5f-4cc2-4c11-b6d6-bea15678cb7b" />
   - Issue: https://github.com/microsoft/vscode/issues/270087
   - Fix PR #270097 — Fix quick chat
   - PR: https://github.com/microsoft/vscode/pull/270097
   - Code excerpts:     - build/lib/stylelint/vscode-known-variables.json: +		"--chat-setup-dialog-glow-angle", +		"--vscode-chat-font-family", +		"--vscode-chat-font-size-body-l", +		"--vscode-chat-font-size-body-m", +		"--vscode-chat-font-size-body-s", +		"--vscode-chat-fo
     - src/vs/workbench/contrib/chat/browser/media/chat.css: +.quick-input-widget .interactive-session { +	width: 100%; +} +

43. Issue #267116 — Two items can have focus in quick pick tree (closed 2025-11-21T21:17:07Z)
   - Issue detail: repro: 1. open tools from panel chat 2. click on `>` icon next to `built-in` 3. click on another `>` icon for another tree entry demo: https://github.com/user-attachments/assets/c7dd1d33-5901-4cbe-9f4d-ac2473fc6e18 Version: 1.105.0-insider Commit: 59baae6ece2474b2b41a28440629983ebd1cac64 Date: 2025-09-15T05:03:28.880Z Electron: 37.3.1 ElectronBuildId: 12342881 Chromium: 138.0.7204.235 Node.js:...
   - Issue: https://github.com/microsoft/vscode/issues/267116
   - Fix PR #276847 — Fix multiple items showing selection in tree when clicking twisties
   - PR: https://github.com/microsoft/vscode/pull/276847
   - Code excerpts:     - src/vs/platform/quickinput/browser/tree/quickInputTreeController.ts: +		this.registerOnDidChangeFocus(); +	registerOnDidChangeFocus() { +		// Ensure that selection follows focus +		this._register(this._tree.onDidChangeFocus(e => { +			const item = this._tree.getFocus()

44. Issue #266256 — Tool invocation for extension tools are not announced to screen reader users (closed 2025-11-06T18:43:58Z)
   - Issue detail: We only know about them in the rendering code, so would need a way to set / check for the ID to ensure it's only announced on initial render cc @roblourens
   - Issue: https://github.com/microsoft/vscode/issues/266256
   - Fix PR #275905 — fix screen reader progress announcements
   - PR: https://github.com/microsoft/vscode/pull/275905
   - Code excerpts:     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatToolProgressPart.ts: +			const shouldAnnounce = this.toolInvocation.kind === 'toolInvocation' && this.hasMeaningfulContent(completionContent) ? this.computeShouldAnnounce(key) : false; +				const shouldAnnounce = this.too

45. Issue #275592 — Dragging a terminal tab to the bottom of tab list no longer works (closed 2025-11-05T23:42:17Z)
   - Issue detail: I do this all the time, broke probably because of chat terminal item at the bottom (even when it's not there): ![Image](https://github.com/user-attachments/assets/5b2a707b-e5aa-4b2e-80b7-5970ddce7e8a)
   - Issue: https://github.com/microsoft/vscode/issues/275592
   - Fix PR #275706 — fix tab drag and drop
   - PR: https://github.com/microsoft/vscode/pull/275706
   - Code excerpts:     - src/vs/workbench/contrib/terminal/browser/media/terminal.css: +.monaco-workbench .pane-body.integrated-terminal .tabs-list-container.drop-target { +	background-color: var(--vscode-list-dropBackground); +} +
     - src/vs/workbench/contrib/terminal/browser/terminalTabbedView.ts: +import { ITerminalChatService, ITerminalConfigurationService, ITerminalGroupService, ITerminalInstance, ITerminalService, TerminalConnectionState, TerminalDataTransfers } from './terminal.js'; +impor

46. Issue #275000 — Help text doesn't update when toggling offsetmode (closed 2025-11-05T00:30:52Z)
   - Issue detail: Testing #274949 * open go to line * type `::` for offset mode * help text says "Type ... from 1 to ..." * toggle offset mode * :bug: the message never updates to "... from 0 to ..."
   - Issue: https://github.com/microsoft/vscode/issues/275000
   - Fix PR #275416 — Go To Line bug fixes
   - PR: https://github.com/microsoft/vscode/pull/275416
   - Code excerpts:     - src/vs/editor/contrib/quickAccess/browser/gotoLineQuickAccess.ts: +	constructor(private useZeroBasedOffset = { value: false }) { +			isChecked: this.useZeroBasedOffset.value, +				this.useZeroBasedOffset.value = !this.useZeroBasedOffset.value; +					label: this.useZ

47. Issue #264569 — Setting and removing `window.activeBorder` color does not reset the window border color (closed 2025-11-17T06:15:09Z)
   - Issue detail: Testing #263838 1. `window.border: default` 2. ``` "workbench.colorCustomizations": { "window.activeBorder": "#ff00ff", } ``` 3. Window color color changes to pink 4. Remove `"window.activeBorder"` from `workbench.colorCustomizations` 5. 🐍 window stays pink instead of using theme color
   - Issue: https://github.com/microsoft/vscode/issues/264569
   - Fix PR #277359 — Setting and removing `window.activeBorder` color does not reset the window border color (fix #264569)
   - PR: https://github.com/microsoft/vscode/pull/277359
   - Code excerpts:     - src/vs/platform/native/electron-main/nativeHostMainService.ts: +		let activeWindowAccentColor: string | boolean | null; +		let inactiveWindowAccentColor: string | boolean | null; +			activeWindowAccentColor = null; +			inactiveWindowAccentColor = null;
     - src/vs/workbench/contrib/relauncher/browser/relauncher.contribution.ts: +import { isLinux, isMacintosh, isNative } from '../../../../base/common/platform.js';

48. Issue #233635 — Add an action to close other windows (closed 2025-11-21T14:24:43Z)
   - Issue detail: Type: <b>Feature Request</b> It would be super useful to have a "close other windows" option, to close every vscode window other than the current one: ![Image](https://github.com/user-attachments/assets/fd151e09-8700-432b-a9fb-a67a8af60026) VS Code version: Code 1.95.2 (e8653663e8840adaf45af01eab5c627a5af81807, 2024-11-07T11:07:22.054Z) OS version: Windows_NT x64 10.0.22631 Modes: <!--...
   - Issue: https://github.com/microsoft/vscode/issues/233635
   - Fix PR #278779 — Add an action to close other windows (fix #233635)
   - PR: https://github.com/microsoft/vscode/pull/278779
   - Code excerpts:     - src/vs/workbench/electron-browser/actions/windowActions.ts: +export class CloseOtherWindowsAction extends Action2 { + +	private static readonly ID = 'workbench.action.closeOtherWindows'; + +	constructor() { +		super({ +			id: CloseOtherWindowsAction.ID, +			ti
     - src/vs/workbench/electron-browser/desktop.contribution.ts: +import { ZoomResetAction, ZoomOutAction, ZoomInAction, CloseWindowAction, SwitchWindowAction, QuickSwitchWindowAction, NewWindowTabHandler, ShowPreviousWindowTabHandler, ShowNextWindowTabHandler, Mov

49. Issue #274314 — Chat terminal button will flicker after selecting one to focus (closed 2025-11-03T20:50:17Z)
   - Issue detail: Following up on https://github.com/microsoft/vscode/pull/274149 Repro: 1. Open 2 terminals 2. `run ls` 3. Click 1 chat terminal in terminal tabs <img width="279" height="66" alt="Image" src="https://github.com/user-attachments/assets/e053c84d-0f98-47b4-abc0-22b120253bb0" /> 4. Select the single entry, 🐛 there's a focus border flicker for ~1 frame around the 1 chat terminal button Quick pick has...
   - Issue: https://github.com/microsoft/vscode/issues/274314
   - Fix PR #274862 — Fix flicker in focus terminal
   - PR: https://github.com/microsoft/vscode/pull/274862
   - Code excerpts:     - src/vs/workbench/contrib/terminalContrib/chat/browser/terminalChatActions.ts: +					qp.hide(); +				} else { +					qp.hide(); +			} else { +				qp.hide();

50. Issue #271032 — Screen reader announces “Type the command to run” prompt after pressing Ctrl to silence speech (closed 2025-11-14T03:12:04Z)
   - Issue detail: Type: <b>Bug</b> There is an accessibility issue when navigating through the Command Palette using a screen reader (tested with both NVDA and Orca). When I open the Command Palette with `Ctrl+Shift+P` and start navigating through the list of commands, if I press the `Ctrl` key to silence the screen reader speech, the initial prompt (“Type the command to run”) is spoken again — it seems to be...
   - Issue: https://github.com/microsoft/vscode/issues/271032
   - Fix PR #275955 — Fix screen reader re-announcing Command Palette prompt when pressing Ctrl
   - PR: https://github.com/microsoft/vscode/pull/275955
   - Code excerpts:     - src/vs/base/browser/keyboardEvent.ts: +import { EVENT_KEY_CODE_MAP, isModifierKey, KeyCode, KeyCodeUtils, KeyMod } from '../common/keyCodes.js'; +		if (!isModifierKey(this.keyCode)) { +		if (!isModifierKey(this.keyCode)) {
     - src/vs/base/common/keyCodes.ts: +				if ((keyCode !== KeyCode.Unknown) && (keyCode !== KeyCode.Enter) && !isModifierKey(keyCode)) { + +export function isModifierKey(keyCode: KeyCode): boolean { +	return ( +		keyCode === KeyCode.Ctrl

51. Issue #274477 — Test: agent sessions single view (closed 2025-11-04T21:36:27Z)
   - Issue detail: Refs: https://github.com/microsoft/vscode/issues/270945 - [x] anyOS @osortega - [x] anyOS @rebornix Complexity: 4 [Create Issue](https://github.com/microsoft/vscode/issues/new?template=blank&body=Testing+%23274477%0A%0A&assignees=bpasero) --- **Note:** the single view is currently not on-par with the classic view in terms of functionality, but feel free to report issues for things you miss. *...
   - Issue: https://github.com/microsoft/vscode/issues/274477
   - Fix PR #275495 — Fix link clicks in markdown triggering parent tree item actions
   - PR: https://github.com/microsoft/vscode/pull/275495
   - Code excerpts:     - src/vs/base/browser/markdownRenderer.ts: +		event.stopPropagation();

52. Issue #264754 — `git remote rename` suggestion seems to have wrong text (closed 2025-11-02T15:20:54Z)
   - Issue detail: Testing #264149 Looks like the description from `git remote remove` is being used instead of a description about `rename` <img width="1127" height="432" alt="Image" src="https://github.com/user-attachments/assets/bca2a497-d892-4977-b216-26fdb4b228d6" />
   - Issue: https://github.com/microsoft/vscode/issues/264754
   - Fix PR #274587 — Fix git remote suggest descriptions
   - PR: https://github.com/microsoft/vscode/pull/274587
   - Code excerpts:     - extensions/terminal-suggest/src/completions/git.ts: +					description: "Removes the given remote", +					description: "Renames the given remote",

53. Issue #277376 — Some setting descriptions use non-standard capitalization of the term 'status bar' (closed 2025-11-14T11:18:54Z)
   - Issue detail: Type: <b>Bug</b> By convention the term is written as 'status bar' unless it appears at the start of a sentence. However the descriptions of a few settings incorrectly capitalize it mid-sentence as 'Status bar'. <img width="1616" height="499" alt="Image" src="https://github.com/user-attachments/assets/79c0d04a-6b48-467a-926d-a26476d24cfd" /> I will submit a PR. VS Code version: Code - Insiders...
   - Issue: https://github.com/microsoft/vscode/issues/277376
   - Fix PR #277383 — Correct non-standard capitalization of term 'status bar' in some settings (fix #277376)
   - PR: https://github.com/microsoft/vscode/pull/277383
   - Code excerpts:     - src/vs/workbench/browser/workbench.contribution.ts: +				description: localize('workbench.editor.showLanguageDetectionHints', "When enabled, shows a status bar Quick Fix when the editor language doesn't match detected content language."),
     - src/vs/workbench/contrib/debug/browser/debug.contribution.ts: +			enumDescriptions: [nls.localize('never', "Never show debug item in status bar"), nls.localize('always', "Always show debug item in status bar"), nls.localize('onFirstSessionStart', "Show debug ite

54. Issue #269178 — Terminal suggest location is odd when in editor area in the side (closed 2025-11-11T22:22:20Z)
   - Issue detail: https://github.com/user-attachments/assets/269a9621-7e73-45f5-8a29-8951f8ec3326 I'm getting completions, but they are appearing in non-ideal way.
   - Issue: https://github.com/microsoft/vscode/issues/269178
   - Fix PR #276631 — Fix various terminal suggest widget layout issues
   - PR: https://github.com/microsoft/vscode/pull/276631
   - Code excerpts:
     - src/vs/workbench/contrib/terminal/browser/media/terminal.css: +.monaco-workbench .split-view-view:has(.integrated-terminal) { +	/** The suggest widget is a child of the split-view-view element so it needs to match z-index of the terminal to not be obstructed. */
     - src/vs/workbench/services/suggest/browser/simpleSuggestWidget.ts: +		// Cap list content height to a reasonable maximum (12 items worth), matching suggestWidget behavior +		const cappedListContentHeight = Math.min(this._list.contentHeight, info.itemHeight * 12); +		

55. Issue #226775 — Comments on the API (closed 2024-09-03T21:40:46Z)
   - Issue detail: Testing #226669 # Comments 1) `TextSearchProviderOptions#folderOptions` is an array; what's the expected behavior if the array is empty? 2) `TextSearchProviderOptions#folderOptions` - all props within the literal object (eg `excludes, `useIgnoreFiles`) non-optional? Is that on purpose? 3) `includes: string[]` but `excludes: GlobPattern[]` -- is that expected? 4) > If set, {@link...
   - Issue: https://github.com/microsoft/vscode/issues/226775
   - Fix PR #275872 — Fix JSDoc wording in textSearchProvider2 API
   - PR: https://github.com/microsoft/vscode/pull/275872
   - Code excerpts:
     - src/vscode-dts/vscode.proposed.textSearchProvider2.d.ts: +		 * If pattern contains a newline character (`\n`), the default search behavior +		 * Whether or not {@link pattern} should match multiple lines of text. +		 * {@link pattern} contains a newline cha

56. Issue #277149 — Chat: `chatEntitlements` is logged too early (closed 2025-11-17T14:42:28Z)
   - Issue detail: This gets called so early on startup that it misses the ExP assignment: https://github.com/microsoft/vscode/blob/769ef65cd62212cde4db47c538acfea3063f1277/src/vs/workbench/services/chat/common/chatEntitlementService.ts#L219-L227 We need to send it later when the ExP assignment has happened. //cc @cwebster-99
   - Issue: https://github.com/microsoft/vscode/issues/277149
   - Fix PR #277344 — Chat: chatEntitlements is logged too early (fix #277149)
   - PR: https://github.com/microsoft/vscode/pull/277344
   - Code excerpts:
     - src/vs/workbench/services/chat/common/chatEntitlementService.ts: +import { ILifecycleService, LifecyclePhase } from '../../lifecycle/common/lifecycle.js'; +		@ITelemetryService private readonly telemetryService: ITelemetryService, +		@ILifecycleService private read

57. Issue #264515 — Double click in empty Chat Sessions list should add new session (closed 2025-09-24T04:59:23Z)
   - Issue detail: Double click in empty Explorer area creates a new empty file (same effect as +) Same pattern should be followed for all views in the Chat Sessions view container. E.g. clicking on an empty space in Claude Code should just create a new claude code session. fyi @jo-oikawa @roblourens
   - Issue: https://github.com/microsoft/vscode/issues/264515
   - Fix PR #268092 — fix #264515.
   - PR: https://github.com/microsoft/vscode/pull/268092
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatSessions/view/sessionsViewPane.ts: +		container.classList.add('chat-sessions-view'); + +				paddingBottom: SessionsDelegate.ITEM_HEIGHT, +		this._register(this.tree.onMouseDblClick(e => { +			const scrollingByPage = this.configurationS
     - src/vs/workbench/contrib/chat/browser/media/chatSessions.css: +.chat-sessions-view { +	display: flex; +	flex-direction: column; +	height: 100%; +} + +.chat-sessions-tree-container, +.getting-started-list-container { +	flex: 1; +	display: flex; +	flex-direction: 

58. Issue #274921 — Test: terminal completion provider API (closed 2025-11-05T12:51:02Z)
   - Issue detail: Refs #224505 - [x] Windows @benibenj - [x] macOS @joshspicer - [x] Linux @joaomoreno Complexity: 4 Authors: @meganrogge, @tyriar [Create Issue](https://github.com/microsoft/vscode/issues/new?template=blank&body=Testing+%23274921%0A%0A&assignees=meganrogge&labels=terminal-suggest) --- We have finalized our terminal completion provider API. Please read through the API, make sure it all makes...
   - Issue: https://github.com/microsoft/vscode/issues/274921
   - Fix PR #275577 — Fix terminal completion provider API documentation
   - PR: https://github.com/microsoft/vscode/pull/275577
   - Code excerpts:
     - src/vs/workbench/contrib/terminalContrib/suggest/browser/terminalSuggestAddon.ts: +import { terminalSymbolAliasIcon, terminalSymbolArgumentIcon, terminalSymbolEnumMember, terminalSymbolFileIcon, terminalSymbolFlagIcon, terminalSymbolInlineSuggestionIcon, terminalSymbolMethodIcon, t
     - src/vs/workbench/contrib/terminalContrib/suggest/browser/terminalSymbolIcons.ts: +export const TERMINAL_SYMBOL_ICON_SYMBOL_TEXT_FOREGROUND = registerColor('terminalSymbolIcon.symbolText', SYMBOL_ICON_FILE_FOREGROUND, localize('terminalSymbolIcon.symbolTextForeground', 'The foregro

59. Issue #270818 — MCP registry installs should prompt to add to user or workspace config (closed 2025-10-15T10:46:09Z)
   - Issue detail: **Currently**: When I install an MCP server via typing "@mcp" in the extension menu, and selecting "Install" it installs the MCP Server globally. **Suggested**: Can I please be prompted on whether I prefer global install OR local install (.vscode/mcp.json). I tend to prefer local install over global. Thanks for considering
   - Issue: https://github.com/microsoft/vscode/issues/270818
   - Fix PR #271494 — fix #270818
   - PR: https://github.com/microsoft/vscode/pull/271494
   - Code excerpts:
     - src/vs/workbench/contrib/mcp/browser/mcpServerActions.ts: +import { ConfigurationTarget, IConfigurationService } from '../../../../platform/configuration/common/configuration.js'; +import { IWorkspaceContextService, IWorkspaceFolder, WorkbenchState } from '.
     - src/vs/workbench/contrib/mcp/browser/mcpServersView.ts: +import { DropDownAction, getContextMenuActions, InstallAction, InstallingLabelAction, ManageMcpServerAction, McpServerStatusAction } from './mcpServerActions.js'; +			const mcpServer = e.element ? th

60. Issue #277187 — Using QuickInputButton with a 'toggle' method throws an error about disallowed API proposal (closed 2025-11-13T18:30:06Z)
   - Issue detail: See https://github.com/dendronhq/dendron/issues/4007#issuecomment-3524609700 https://github.com/microsoft/vscode/issues/221397#issuecomment-2225357158 The new `toggle` member was added and is checked for this API proposal: https://github.com/microsoft/vscode/issues/144956 The customer had a `toggle` method on a class that derives from QuickInputButton and is now getting an error while they are...
   - Issue: https://github.com/microsoft/vscode/issues/277187
   - Fix PR #277216 — Check QuickPickButton property shapes before throwing an error
   - PR: https://github.com/microsoft/vscode/pull/277216
   - Code excerpts:
     - src/vs/workbench/api/common/extHostQuickOpen.ts: +			if (buttons.some(button => +				typeof button.location === 'number' || +				typeof button.toggle === 'object' && typeof button.toggle.checked === 'boolean')) { +			if (buttons.some(button => +				

61. Issue #204812 — Re-instate swipeToNavigate for Mac (closed 2025-11-09T14:24:16Z)
   - Issue detail: Per [this PR](https://github.com/microsoft/vscode/pull/23663) - original setting was ` "workbench.editor.swipeToNavigate": true` I realise that the setting was removed per [this](https://github.com/microsoft/vscode/issues/57629) but that's a long time ago and it looks like it can be supported with [this Electron event](https://www.electronjs.org/docs/latest/api/browser-window#event-swipe-macos)...
   - Issue: https://github.com/microsoft/vscode/issues/204812
   - Fix PR #276360 — Re-instate swipeToNavigate for Mac (fix #204812)
   - PR: https://github.com/microsoft/vscode/pull/276360
   - Code excerpts:
     - src/vs/platform/windows/electron-main/windowImpl.ts: +		// Swipe command support (macOS) +		if (isMacintosh && (!e || e.affectsConfiguration('workbench.editor.swipeToNavigate'))) { +			const swipeToNavigate = this.configurationService.getValue<boolean>(
     - src/vs/workbench/browser/parts/editor/editor.ts: +	swipeToNavigate: false, +		'swipeToNavigate': new BooleanVerifier(DEFAULT_EDITOR_PART_OPTIONS['swipeToNavigate']),

62. Issue #274306 — Right margin is too large when terminal output is expanded (closed 2025-11-11T22:04:18Z)
   - Issue detail: Following up on https://github.com/microsoft/vscode/pull/273175 Before clicking: <img width="660" height="151" alt="Image" src="https://github.com/user-attachments/assets/7fe961b6-eb5e-40a1-a8e0-8b2d9462d427" /> After clicking: <img width="657" height="327" alt="Image" src="https://github.com/user-attachments/assets/4acad26d-8f76-4f6d-9247-810522901652" />
   - Issue: https://github.com/microsoft/vscode/issues/274306
   - Fix PR #274942 — fix css of terminal chat output
   - PR: https://github.com/microsoft/vscode/pull/274942
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/media/chatTerminalToolProgressPart.css: +	max-width: 100%; +	box-sizing: border-box; +	margin-right: 18px; +	max-width: 100%; +	padding: 5px 9px; + +.chat-terminal-content-title.expanded { +	margin-right: 18px; +	border-bottom-left-radius: 

63. Issue #270769 — Cannot hide "MCP Servers" Panel (closed 2025-10-13T10:43:44Z)
   - Issue detail: Type: <b>Bug</b> The MCP Servers panel appeared in the Extensions panel and it cannot be hidded. The options that control it's visibility are disabled. <img width="263" height="220" alt="Image" src="https://github.com/user-attachments/assets/98017fa6-a15e-41d1-abe0-05b61b939088" /> VS Code version: Code 1.105.0 (03c265b1adee71ac88f833e065f7bb956b60550a, 2025-10-08T14:09:35.891Z) OS version:...
   - Issue: https://github.com/microsoft/vscode/issues/270769
   - Fix PR #271093 — fix #270769
   - PR: https://github.com/microsoft/vscode/pull/271093
   - Code excerpts:
     - src/vs/workbench/contrib/mcp/browser/mcpServersView.ts: +				canToggleVisibility: true

64. Issue #274775 — Terminal Tab Icons Display Scrollbar Despite Sufficient Vertical Space, Hiding Icons (closed 2025-11-03T17:40:09Z)
   - Issue detail: Type: <b>Bug</b> When users create multiple terminals (three or more) in VS Code's terminal region, the terminal icons display on the right side with a scrollbar appearing even though there is sufficient vertical space available in the panel. The scrollbar prevents all terminal icons from being fully visible and accessible at once, requiring unnecessary scrolling to view or switch between...
   - Issue: https://github.com/microsoft/vscode/issues/274775
   - Fix PR #274812 — fix bug with terminal tabs height
   - PR: https://github.com/microsoft/vscode/pull/274812
   - Code excerpts:
     - src/vs/workbench/contrib/terminal/browser/terminalTabbedView.ts: +			layout: width => this._tabList.layout(this._height || 0, width),

65. Issue #277205 — New "attach to chat" action appears even when AI is disabled (closed 2025-11-17T16:00:45Z)
   - Issue detail: 1. Turn `"chat.disableAIFeatures": true` 2. Run a terminal command and action in the gutter 3. "attach to chat" is still there 🐛
   - Issue: https://github.com/microsoft/vscode/issues/277205
   - Fix PR #277870 — don't show attach to chat if chat is disabled
   - PR: https://github.com/microsoft/vscode/pull/277870
   - Code excerpts:
     - src/vs/workbench/contrib/terminal/browser/xterm/decorationAddon.ts: +		const chatIsEnabled = this._chatWidgetService.getWidgetsByLocations(ChatAgentLocation.Chat).some(w => w.attachmentCapabilities.supportsTerminalAttachments); +		if (!chatIsEnabled) { +			return unde

66. Issue #263881 — Sticky scrolled element checkbox click does not trigger change (closed 2025-11-21T03:17:19Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/263881
   - Fix PR #276848 — Fix sticky scroll checkbox click not triggering change event
   - PR: https://github.com/microsoft/vscode/pull/276848
   - Code excerpts:
     - src/vs/platform/quickinput/browser/tree/quickInputTreeController.ts: +import { QuickInputCheckboxStateHandler, QuickInputTreeRenderer } from './quickInputTreeRenderer.js'; +import { Checkbox } from '../../../../base/browser/ui/toggle/toggle.js'; +	private readonly _che
     - src/vs/platform/quickinput/browser/tree/quickInputTreeRenderer.ts: +export class QuickInputCheckboxStateHandler<T> extends Disposable { +	private readonly _onDidChangeCheckboxState = this._register(new Emitter<{ item: T; checked: boolean | 'mixed' }>()); +	public rea

67. Issue #274470 — Terminal tool call data rendering glitches (closed 2025-11-01T20:52:54Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/274470
   - Fix PR #274543 — Fix rendering of markdown inside HEREDOC
   - PR: https://github.com/microsoft/vscode/pull/274543
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts: +			new MarkdownString([ +				`$(${Codicon.terminal.id})`, +				``, +				`\`\`\`${terminalData.language}`, +				`${command.replaceAll('```', '\\`\\`\\`')}`, +				`\`\`\`` +			].join('\n'), { supportTh

68. Issue #270029 — Bad terminal sticky scroll header when `ctrl+l`  (closed 2025-11-14T20:10:43Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/270029
   - Fix PR #277215 — Fix prompt start marker after ctrl+l (ED 2 J)
   - PR: https://github.com/microsoft/vscode/pull/277215
   - Code excerpts:
     - src/vs/platform/terminal/common/capabilities/commandDetection/terminalCommand.ts: +	/** +	 * Track temporarily if the command was recently cleared, this can be used for marker +	 * adjustments +	 */ +	wasCleared?: boolean;
     - src/vs/platform/terminal/common/capabilities/commandDetectionCapability.ts: +		this._register(this._terminal.parser.registerCsiHandler({ final: 'J' }, params => { +			if (params.length >= 1 && params[0] === 2) { +				if (!this._terminal.options.scrollOnEraseInDisplay) { +				

69. Issue #273518 — Fix codicon in iconlabel (closed 2025-10-27T09:54:25Z)
   - Issue detail: Fixes https://github.com/microsoft/vscode/issues/273507
   - Issue: https://github.com/microsoft/vscode/pull/273518
   - Fix PR #273524 — Fix codicon in iconlabel (#273518)
   - PR: https://github.com/microsoft/vscode/pull/273524
   - Code excerpts:
     - src/vs/base/browser/ui/iconLabel/iconLabel.ts: +				const supportIcons = options?.supportIcons ?? this.creationOptions?.supportIcons; +				descriptionNode.set(description || '', options ? options.descriptionMatches : undefined, undefined, options?

70. Issue #264887 — Error: Can not find provide for claude-code (closed 2025-09-18T22:30:30Z)
   - Issue detail: Getting this error in dev console on chat startup: <img width="1726" height="134" alt="Image" src="https://github.com/user-attachments/assets/7dd625c7-fcce-4a42-8009-b0a702c22a60" /> I don't have claude configured for copilot-chat chat v 0.31.2025090302
   - Issue: https://github.com/microsoft/vscode/issues/264887
   - Fix PR #267407 — fix #264887
   - PR: https://github.com/microsoft/vscode/pull/267407
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/actions/chatActions.ts: +								if (!sessions?.length) { +									continue; +								}
     - src/vs/workbench/contrib/chat/browser/chatSessions.contribution.ts: +	async canResolveItemProvider(chatViewType: string): Promise<boolean> { +			return [];

71. Issue #277260 — ChatThinkingContentPart leak errors (closed 2025-11-13T21:09:03Z)
   - Issue detail: Open VSCode Start few chat sessions that involve thinking While thinking in progress, cancel and regenerate OR Rapidly switch between sessions while previous session in progress. Get this leak error: ``` Error: Trying to add a disposable to a DisposableStore that has already been disposed of. The added object will be leaked! at DisposableStore.add (vscode-file://vscode-...
   - Issue: https://github.com/microsoft/vscode/issues/277260
   - Fix PR #277264 — Fix leak errors from disposed ChatThinkingContentPart during thinking stream
   - PR: https://github.com/microsoft/vscode/pull/277264
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/chatThinkingContentPart.ts: +		// Guard against rendering after disposal to avoid leaking disposables +		if (this._store.isDisposed) { +			return; +		} +		// If disposed, ignore late updates coming from renderer diffing +		if (t

72. Issue #274728 — Every new terminal tool call, adds an "open in terminal" button for the terminal tool (closed 2025-11-03T16:35:12Z)
   - Issue detail: Open vscode repo, agent mode and ask "Look at the git changes in the last 24 hours. And try to find the change that broke the terminal tool (that agent uses). Now the terminal tool gets stuck. So you do not need to fix it, just find the commit that is the culprit. Think hard!" <img width="957" height="279" alt="Image" src="https://github.com/user-...
   - Issue: https://github.com/microsoft/vscode/issues/274728
   - Fix PR #274791 — prevent duplicate chat terminal focus actions from being added
   - PR: https://github.com/microsoft/vscode/pull/274791
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts: +		const actionBar = this._actionBar.value; +			const existingFocus = this._focusAction.value; +			if (existingFocus) { +				const existingIndex = actionBar.viewItems.findIndex(item => item.action ===

73. Issue #259884 — The distance between the twistie and checkbox seems too big comparent to the distance between the twistie and the label in the tree (closed 2025-11-19T02:02:16Z)
   - Issue detail: > The distance between the twistie and checkbox seems too big comparent to the distance between the twistie and the label in the tree <img width="819" height="164" alt="Image" src="https://github.com/user-attachments/assets/cc659d92-fc65-4970-bd53-4b8b04c9a6e2" /> I wonder if there's an option on the tree for this... if not, maybe we can use some CSS to make the twisty container have less padding.
   - Issue: https://github.com/microsoft/vscode/issues/259884
   - Fix PR #277921 — Reduce excessive spacing between tree twistie and checkbox
   - PR: https://github.com/microsoft/vscode/pull/277921
   - Code excerpts:
     - src/vs/platform/quickinput/browser/media/quickInput.css: +	padding-right: 6px;

74. Issue #140788 — "Build Task" terminal window inconsistent scrolling behavior (closed 2022-01-21T14:44:54Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/140788
   - Fix PR #275952 — Fix quickpick checkbox toggle by removing checkboxes from tab order
   - PR: https://github.com/microsoft/vscode/pull/275952
   - Code excerpts:
     - src/vs/platform/quickinput/browser/quickInputList.ts: +			// Remove checkbox from tab order since tree items are navigable with arrow keys +			// This prevents the issue where pressing Space toggles both the tabbed checkbox and the focused item +			check

75. Issue #277389 — Opening a log entry results in a `Unable to resolve filesystem provider` error in console (closed 2025-11-14T18:52:26Z)
   - Issue detail: * use the copilot chat extension * type in a file * open the log viewer * click on a log entry * the following is logged in the console: <img width="682" height="151" alt="Image" src="https://github.com/user-attachments/assets/96156855-686d-4f73-abf3-f625aeceaa30" /> Behind the scenes, the copilot chat extension uses the `workspace.registerTextDocumentContentProvider` to define the `ccreq:`...
   - Issue: https://github.com/microsoft/vscode/issues/277389
   - Fix PR #277487 — Don't watch non-writable fs for md preview updates
   - PR: https://github.com/microsoft/vscode/pull/277487
   - Code excerpts:
     - extensions/markdown-language-features/src/preview/preview.ts: +		if (vscode.workspace.fs.isWritableFileSystem(resource.scheme)) { +			const watcher = this._register(vscode.workspace.createFileSystemWatcher(new vscode.RelativePattern(resource, '*'))); +			this._r

76. Issue #270399 — Very old version is installed if the latest version is not compatible (closed 2025-10-08T18:41:57Z)
   - Issue detail: Steps to Repro (from OSS) - Change package.json version to 1.104.0 - Set `"quality": "stable"` in product.overrides.json - Run VS Code from sources - Install Jupyter Extension - Verify that 2025.8.0 version of Jupyter is installed
   - Issue: https://github.com/microsoft/vscode/issues/270399
   - Fix PR #270402 — fix #270399
   - PR: https://github.com/microsoft/vscode/pull/270402
   - Code excerpts:
     - src/vs/platform/extensionManagement/common/extensionGalleryService.ts: +export function filterLatestExtensionVersionsForTargetPlatform(versions: IRawGalleryExtensionVersion[], targetPlatform: TargetPlatform, allTargetPlatforms: TargetPlatform[]): IRawGalleryExtensionVers
     - src/vs/platform/extensionManagement/test/common/extensionGalleryService.test.ts: +import { IRawGalleryExtensionVersion, sortExtensionVersions, filterLatestExtensionVersionsForTargetPlatform } from '../../common/extensionGalleryService.js'; + +	function aPreReleaseExtensionVersion(

77. Issue #269352 — Leaked disposable: `SelectBoxList.renderDescriptionMarkdown` (closed 2025-11-03T20:42:25Z)
   - Issue detail: ``` [LEAKED DISPOSABLE] Error: CREATED via: at GCBasedDisposableTracker.trackDisposable (vscode-file://vscode-app/Users/bpasero/Development/Microsoft/vscode/out/vs/base/common/lifecycle.js:28:23) at trackDisposable (vscode-file://vscode-app/Users/bpasero/Development/Microsoft/vscode/out/vs/base/common/lifecycle.js:199:24) at new DisposableStore (vscode-file://vscode-...
   - Issue: https://github.com/microsoft/vscode/issues/269352
   - Fix PR #274864 — Fix leak in selection box md rendering
   - PR: https://github.com/microsoft/vscode/pull/274864
   - Code excerpts:
     - src/vs/base/browser/ui/selectBox/selectBoxCustom.ts: +import { Disposable, DisposableStore, IDisposable } from '../../../common/lifecycle.js'; +import { IRenderedMarkdown, MarkdownActionHandler, renderMarkdown } from '../../markdownRenderer.js'; +	priva

78. Issue #272223 — Uncaught TypeError: Cannot read properties of undefined (reading 'map') at Object.getActions (modePickerActionItem.ts:92:28) (closed 2025-10-20T13:32:43Z)
   - Issue detail: Version: 1.106.0-insider Commit: 42943e3121fe00fcedf95b64ada12f82b54ff082 Date: 2025-10-20T05:04:36.410Z Electron: 37.7.0 ElectronBuildId: 12597478 Chromium: 138.0.7204.251 Node.js: 22.20.0 V8: 13.8.258.32-electron.0 OS: Darwin arm64 24.6.0 Name: GitHub Copilot Chat Id: GitHub.copilot-chat Description: AI chat features powered by Copilot Version: 0.33.2025102001 Publisher: GitHub VS Marketplace...
   - Issue: https://github.com/microsoft/vscode/issues/272223
   - Fix PR #272263 — fix(chat): guard against undefined customModes.custom Fix #272223 and #272236
   - PR: https://github.com/microsoft/vscode/pull/272263
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/modelPicker/modePickerActionItem.ts: +					...customModes.custom?.map(mode => makeActionFromCustomMode(mode, currentMode)) ?? []

79. Issue #277352 — Regression: Command `vscode.executeFormatDocumentProvider` Throws "Unexpected Type" Error (closed 2025-11-17T14:42:33Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/277352
   - Fix PR #277399 — Regression: Command `vscode.executeFormatDocumentProvider` Throws "Unexpected Type" Error (fix #277352)
   - PR: https://github.com/microsoft/vscode/pull/277399
   - Code excerpts:
     - src/vs/editor/contrib/format/browser/format.ts: +// eslint-disable-next-line @typescript-eslint/no-explicit-any +CommandsRegistry.registerCommand('_executeFormatRangeProvider', async function (accessor, ...args: any[]) { +// eslint-disable-next-lin

80. Issue #272716 — SCM: Latest Insider hides all inline actions on Changes view (closed 2025-10-22T15:26:52Z)
   - Issue detail: Type: <b>Bug</b> Opening new issue as requested by @lszomoru at https://github.com/microsoft/vscode/pull/272471#issuecomment-3432550116 Copilot PR feedback at https://github.com/microsoft/vscode/pull/272471#discussion_r2448317084 seems to have identified the cause. I will attempt a PR to fix. VS Code version: Code - Insiders 1.106.0-insider (55505bf0b5b7abbe820137bf8e01bed9b72675cf,...
   - Issue: https://github.com/microsoft/vscode/issues/272716
   - Fix PR #272717 — Fix unintended hiding of inline actions on SCM Changes view (fix #272716)
   - PR: https://github.com/microsoft/vscode/pull/272717
   - Code excerpts:
     - src/vs/workbench/contrib/scm/browser/menus.ts: +				let itemToAppend = menuItem; +					itemToAppend = { ...menuItem, isHiddenByDefault: true }; +				this.repositoryMenuDisposables.add(MenuRegistry.appendMenuItem(MenuId.SCMSourceControlInline, item
81. Issue #272616 — `Ctrl+R` shows folders, workspaces, and files mixed up together (closed 2025-10-22T08:20:58Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/272616
   - Fix PR #272651 — `Ctrl+R` shows folders, workspaces, and files mixed up together (fix #272616)
   - PR: https://github.com/microsoft/vscode/pull/272651
   - Code excerpts:
     - src/vs/workbench/browser/actions/windowActions.ts: +			sortByLabel: false,

82. Issue #274108 — Leaked disposables in MainThreadTerminalService (closed 2025-11-10T16:22:32Z)
   - Issue detail: Running fom main I get this in the log Version: 1.106.0 Commit: Unknown Date: Unknown Electron: 37.7.0 ElectronBuildId: undefined Chromium: 138.0.7204.251 Node.js: 22.20.0 V8: 13.8.258.32-electron.0 OS: Linux x64 5.15.0-157-generic lifecycle.ts:51 [LEAKED DISPOSABLE] Error: CREATED via: at GCBasedDisposableTracker.trackDisposable (vscode-file://vscode-...
   - Issue: https://github.com/microsoft/vscode/issues/274108
   - Fix PR #276526 — Register ext host proxy listeners
   - PR: https://github.com/microsoft/vscode/pull/276526
   - Code excerpts:
     - src/vs/workbench/api/browser/mainThreadTerminalService.ts: +		this._store.add(proxy.onInput(data => this._proxy.$acceptProcessInput(proxy.instanceId, data))); +		this._store.add(proxy.onShutdown(immediate => this._proxy.$acceptProcessShutdown(proxy.instanceId

83. Issue #270285 — Old version of extension (2023.8.*) is getting installed in stable VS Code (closed 2025-10-08T14:00:53Z)
   - Issue detail: ## Repro steps I develop an extension which adds a `JupyterServerProvider` through `createJupyterServerCollection`. The latest `ms-toolsai.jupyter` seems to have broken that functionality. ## Environment data - VS Code version: 1.104.2 - Jupyter Extension version (available under the Extensions sidebar): 2023.8.1002501831 - Python Extension version (available under the Extensions sidebar):...
   - Issue: https://github.com/microsoft/vscode/issues/270285
   - Fix PR #270351 — candidate fix for #270285
   - PR: https://github.com/microsoft/vscode/pull/270351
   - Code excerpts:
     - src/vs/platform/extensionManagement/common/extensionGalleryService.ts: +			}, allTargetPlatforms, true); +	private getRawGalleryExtensionVersionsToValidate(rawGalleryExtensionVersions: IRawGalleryExtensionVersion[], targetPlatform: TargetPlatform, allTargetPlatforms: Tar

84. Issue #272777 — Clean up code layering suppressions (closed 2025-10-23T07:28:40Z)
   - Issue detail: Tree sitter tests, both existing: https://github.com/microsoft/vscode/blob/13f1611459084bf4dca819af2b251625fe149114/src/vs/workbench/test/electron-main/treeSitterTokenizationFeature.test.ts#L43-L53 And those coming in https://github.com/microsoft/vscode/pull/272281 right now live in electron-main or electron-browser and import from node. This is required as `ITreeSitterLibraryService` needs to...
   - Issue: https://github.com/microsoft/vscode/issues/272777
   - Fix PR #272834 — Clean up code layering suppressions (fix #272777)
   - PR: https://github.com/microsoft/vscode/pull/272834
   - Code excerpts:
     - .github/copilot-instructions.md: +MANDATORY: Always check the `VS Code - Build` watch task output via #runTasks/getTaskOutput for compilation errors before running ANY script or declaring work complete, then fix all compilation error

85. Issue #264496 — Coding Agent view: Switching sessions turns remote in to local session (closed 2025-09-03T16:49:41Z)
   - Issue detail: Testing #264383 - Create new remote session - Select another session in the sessions view - Select the previously created remote session - Now it shows the local session UI. 🐛 <img width="2120" height="799" alt="Image" src="https://github.com/user-attachments/assets/58d24df0-48aa-41f8-b1ac-caf6959d0f52" />
   - Issue: https://github.com/microsoft/vscode/issues/264496
   - Fix PR #264801 — fix #264496
   - PR: https://github.com/microsoft/vscode/pull/264801
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatEditor.ts: +import { getChatSessionType } from './chatSessions/common.js'; +		const chatSessionType = getChatSessionType(input); +		if (chatSessionType !== 'local') { +			await raceCancellationError(this.chatSes
     - src/vs/workbench/contrib/chat/browser/chatSessions.contribution.ts: +						resource: ChatEditorInput.getNewEditorUri().with({ query: `chatSessionType=${type}` }),

86. Issue #264630 — Opening copilot chat session in sidebar doesn't pin agent (closed 2025-09-02T23:45:31Z)
   - Issue detail: Testing #264256 1. Using the chat session view 2. Right click an item and select `open in sidebar` **Bug** The session opens but it the agent is not pinned in the side bar. This results in a weird state where you can have normal chats after the agent chats <img width="913" height="506" alt="Image" src="https://github.com/user-attachments/assets/a15579d7-50ea-4301-9e18-4db64ee6ca77" /> I'd...
   - Issue: https://github.com/microsoft/vscode/issues/264630
   - Fix PR #264796 — fix #264630
   - PR: https://github.com/microsoft/vscode/pull/264796
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatViewPane.ts: +import { Schemas } from '../../../../base/common/network.js'; +import { IChatSessionsService, IChatSessionsExtensionPoint } from '../common/chatSessionsService.js'; +import { ChatSessionUri } from '.

87. Issue #226808 — Multi File Diff Editor: Hover Messages are cut off (closed 2025-10-20T18:39:47Z)
   - Issue detail: Testing #226665 Testing on latest VS Code Insiders on Windows 11 Insiders ``` Version: 1.93.0-insider (user setup) Commit: ff7a154d5e5e9034914f0466420f0f1407f0c95e Date: 2024-08-27T05:04:20.235Z Electron: 30.4.0 ElectronBuildId: 10073054 Chromium: 124.0.6367.243 Node.js: 20.15.1 V8: 12.4.254.20-electron.0 OS: Windows_NT x64 10.0.25987 ``` I was surprised I could add a breakpoint. Additionally,...
   - Issue: https://github.com/microsoft/vscode/issues/226808
   - Fix PR #271721 — Fix hover widget out of bounds
   - PR: https://github.com/microsoft/vscode/pull/271721
   - Code excerpts:
     - src/vs/editor/browser/widget/multiDiffEditor/diffEditorItemTemplate.ts: +			fixedOverflowWidgets: true
     - src/vs/editor/contrib/hover/browser/glyphHoverWidget.ts: +	public readonly allowEditorOverflow = true; + +		// Constrain the hover widget to stay within the editor bounds +		const editorHeight = editorLayout.height; +		const maxTop = editorHeight - nodeHeig

88. Issue #269070 — NVDA is not announcing placeholder text in the Copilot chat input field: A11y_Visual Studio Code Copilot Extensions_Inline Chat_Screen Reader (closed 2025-11-11T19:08:44Z)
   - Issue detail: ### GitHub Tags: #A11yTCS; #A11ySev2; #DesktopApp; #Win11; #Win32; #A11yMAS; #SH-Visual Studio Code Copilot Extensions-Win32-Sept25;#Visual Studio Code Client;#WCAG1.3.1;#AILimited; #Screen Reader; #NVDA; #Info and Relationships; #Element:Placeholder; ### Environment Details: Application Name: Visual Studio Code Copilot Extensions Visual studio code Version: 1.104.2 (user setup) Microsoft...
   - Issue: https://github.com/microsoft/vscode/issues/269070
   - Fix PR #276195 — get placeholder to be read by screen reader for chat inputs
   - PR: https://github.com/microsoft/vscode/pull/276195
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/contrib/chatInputEditorContrib.ts: +import { NativeEditContextRegistry } from '../../../../../editor/browser/controller/editContext/native/nativeEditContextRegistry.js'; +			this.updateAriaPlaceholder(undefined); +			const displayPlace

89. Issue #212548 — Goto implementation UI has a contrast issue? (closed 2025-10-30T19:36:56Z)
   - Issue detail: I find this representation to lack contrast: ![image](https://github.com/microsoft/vscode/assets/900690/5b2c9a93-9202-48a8-be85-cedbdd8420d5) I am not sure it meets our a18y requirements? This is the "Find Implementations" peek UI.
   - Issue: https://github.com/microsoft/vscode/issues/212548
   - Fix PR #274178 — Goto implementation UI has a contrast issue (fix #212548)
   - PR: https://github.com/microsoft/vscode/pull/274178
   - Code excerpts:
     - src/vs/editor/contrib/gotoSymbol/browser/peek/referencesWidget.css: +	color: var(--vscode-peekViewResult-fileForeground) !important; +	background-color: var(--vscode-peekViewResult-matchHighlightBackground) !important;

90. Issue #264722 — Text is not visible in settings editor search when narrow (closed 2025-09-29T18:41:38Z)
   - Issue detail: On the latest Insiders, I have "thinking" typed into the search box here <img width="556" height="135" alt="Image" src="https://github.com/user-attachments/assets/959f745e-878e-4d7b-80fd-23c6131a5908" /> I see on the monaco editor it explicitly has has `width: 5px`
   - Issue: https://github.com/microsoft/vscode/issues/264722
   - Fix PR #268924 — fix: double-counting during search widget layout
   - PR: https://github.com/microsoft/vscode/pull/268924
   - Code excerpts:
     - src/vs/workbench/contrib/preferences/browser/settingsEditor2.ts: +		// minus padding inside inputbox, controls width, and extra padding before countElement +		const monacoWidth = innerWidth - 10 - this.controlsElement.clientWidth - 12; +			this.layout(this.dimensio

91. Issue #271542 — Walkthrough Guide is not opened, Welcome tab is opened instead (no extensions) (closed 2025-10-27T18:30:55Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/271542
   - Fix PR #273423 — Walkthrough Guide is not opened, Welcome tab is opened instead (no extensions) (fix #271542)
   - PR: https://github.com/microsoft/vscode/pull/273423
   - Code excerpts:
     - src/vs/workbench/contrib/welcomeGettingStarted/browser/gettingStarted.contribution.ts: +				options = { selectedCategory, selectedStep, showWelcome: false, preserveFocus: toSide ?? false }; +				options = { selectedCategory, selectedStep, showWelcome: true, preserveFocus: toSide ?? fals
     - src/vs/workbench/contrib/welcomeGettingStarted/browser/gettingStarted.ts: +	get editorInput(): GettingStartedInput { +		return this._input as GettingStartedInput; +	} + +	override async setInput(newInput: GettingStartedInput, options: GettingStartedEditorOptions | undefined

92. Issue #271491 — Inline commands explainer in auto approve setting isn't rendered properly (closed 2025-10-19T11:18:58Z)
   - Issue detail: <img width="690" height="331" alt="Image" src="https://github.com/user-attachments/assets/d8f3e471-fb70-49de-baa8-08760e21d20b" />
   - Issue: https://github.com/microsoft/vscode/issues/271491
   - Fix PR #272149 — Remove string that can't be injecting into localized string
   - PR: https://github.com/microsoft/vscode/pull/272149
   - Code excerpts:
     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/common/terminalChatAgentToolsConfiguration.ts: +			localize('autoApprove.description.subCommands', "Note that these commands and regular expressions are evaluated for every _sub-command_ within the full _command line_, so {0} for example will need

93. Issue #276741 — terminal hints are blocking input (closed 2025-11-12T16:33:44Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/276741
   - Fix PR #276763 — allow disabling certain detail orientation, add `north` rendering 
   - PR: https://github.com/microsoft/vscode/pull/276763
   - Code excerpts:
     - src/vs/workbench/contrib/terminalContrib/suggest/browser/terminalSuggestAddon.ts: +import { SimpleSuggestDetailsPlacement } from '../../../../services/suggest/browser/simpleSuggestWidgetDetails.js'; +					preventDetailsPlacements: [SimpleSuggestDetailsPlacement.West],
     - src/vs/workbench/services/suggest/browser/simpleSuggestWidget.ts: +import { canExpandCompletionItem, SimpleSuggestDetailsOverlay, SimpleSuggestDetailsWidget, type SimpleSuggestDetailsPlacement } from './simpleSuggestWidgetDetails.js'; + +	/** +	 * Disables specific 

94. Issue #267747 — Bad Relative Path Separator (closed 2025-09-23T15:05:17Z)
   - Issue detail: Hi everyone, I’ve configured a custom relative path separator (`explorer.copyRelativePathSeparator`) in VS Code settings. It works correctly when I copy a relative path from the Explorer or a normal file tab. However, when I copy a relative path from a tab that shows Git diffs of the same file (for example, when comparing changes in Source Control), the custom separator is ignored and VS Code...
   - Issue: https://github.com/microsoft/vscode/issues/267747
   - Fix PR #267947 — Bad Relative Path Separator (fix #267747)
   - PR: https://github.com/microsoft/vscode/pull/267947
   - Code excerpts:
     - src/vs/workbench/services/label/common/labelService.ts: +const posixPathSeparatorRegexp = /\//g; // on Unix, backslash is a valid filename character +const winPathSeparatorRegexp = /[\\\/]/g; // on Windows, neither slash nor backslash are valid filename ch

95. Issue #272656 — Cannot create hidden terminals (and then display) in the editor pane (closed 2025-10-24T12:21:31Z)
   - Issue detail: * Create a terminal using `createTerminal` api using `hideFromUser: true` and `location: { viewColumn: ViewColumn.Active },` * Next show the terminal * Its displayed in terminal pane & not editor pane
   - Issue: https://github.com/microsoft/vscode/issues/272656
   - Fix PR #272692 — Handle hideFromUser properly for terminal editors
   - PR: https://github.com/microsoft/vscode/pull/272692
   - Code excerpts:
     - src/vs/workbench/contrib/terminal/browser/terminalService.ts: +interface IBackgroundTerminal { +	instance: ITerminalInstance; +	terminalLocationOptions?: ITerminalLocationOptions; +} + +	private _backgroundedTerminalInstances: IBackgroundTerminal[] = []; +		retu

96. Issue #275322 — Extra line in output on Windows (closed 2025-11-04T21:42:26Z)
   - Issue detail: cc @meganrogge Extra line at start of output: <img width="869" height="482" alt="Image" src="https://github.com/user-attachments/assets/14e67eae-4bfe-4d9d-a143-80a6ed02f6c9" /> Terminal shows C at the end of the line, I think we trim that initial specifically? <img width="496" height="138" alt="Image" src="https://github.com/user-attachments/assets/fa59dc65-d93f-4a33-8d1f-f23e4b47cc3b" />...
   - Issue: https://github.com/microsoft/vscode/issues/275322
   - Fix PR #275325 — Ignore initial line if it's whitespace after 633 C
   - PR: https://github.com/microsoft/vscode/pull/275325
   - Code excerpts:
     - src/vs/workbench/contrib/terminal/browser/xterm/xtermTerminal.ts: +			if (line && line.translateToString(true, i === startLine ? startCol : undefined).trim() === '') { +				if (i === startLine) { +					startCol = 0; +				}

97. Issue #271157 — Cannot read properties of null (reading 'webContents') (closed 2025-10-15T08:09:16Z)
   - Issue detail: ```javascript TypeError: Cannot read properties of null (reading 'webContents') at mc.Yb in out/main.js:84:2220 at <anonymous> in out/main.js:84:2347 at <anonymous> in out/main.js:30:80360 ``` [Go to Errors Site](https://errors.code.visualstudio.com/card?ch=bcbd0b4a9877c49ece744f86f4dc1e2b73477e98&bH=708c1dd2-d9c6-1cf2-ed01-cda5d6952071)
   - Issue: https://github.com/microsoft/vscode/issues/271157
   - Fix PR #271463 — Cannot read properties of null (reading 'webContents') (fix #271157)
   - PR: https://github.com/microsoft/vscode/pull/271463
   - Code excerpts:
     - src/vs/platform/windows/electron-main/windowImpl.ts: +			const stack = await this._win?.webContents.mainFrame.collectJavaScriptCallStack(); +					const fakeError = new UnresponsiveError(stack, this.id, this._win?.webContents.getOSProcessId());

98. Issue #266688 — VSCode Formatted wrong TextDocument (closed 2025-09-23T05:04:27Z)
   - Issue detail: Not sure exactly how I did it but I managed to initiate a format on one document and have it execute on another it all happened so quickly I believe I attempted to format the `yaml-1.1.tmLanguage.json` file then I think I quickly switched to the `package.json` file and all the formatting edits were applied to the `package.json` file instead of the `yaml...json` file <img width="2548"...
   - Issue: https://github.com/microsoft/vscode/issues/266688
   - Fix PR #267628 — Fix RangeFormat wrong document race condition
   - PR: https://github.com/microsoft/vscode/pull/267628
   - Code excerpts:
     - src/vs/editor/contrib/format/browser/format.ts: + +		if (cts.token.isCancellationRequested) { +			return true; +		}

99. Issue #263568 — Error "Failed to fetch MCP registry URL" in dev console (closed 2025-08-28T10:42:36Z)
   - Issue detail: Type: <b>Bug</b> This line seems to be throwing - https://github.com/microsoft/vscode/blob/d793cce20e8a5ed7a04d603c20913eb0fe66c07f/src/vs/workbench/services/accounts/common/defaultAccount.ts#L310 <img width="1484" height="724" alt="Image" src="https://github.com/user-attachments/assets/586a0ae2-cd66-4bd4-ae67-14e6592b49d9" /> VS Code version: Code - Insiders 1.104.0-insider...
   - Issue: https://github.com/microsoft/vscode/issues/263568
   - Fix PR #263787 — fix #263568
   - PR: https://github.com/microsoft/vscode/pull/263787
   - Code excerpts:
     - package.json: +  "distro": "b24b9e641896a258e9ea5ab01ac9dd5f4099b882", +}
     - src/vs/workbench/services/accounts/common/defaultAccount.ts: +		if (!mcpRegistryDataUrl) { +			return undefined; +		} +

100. Issue #269417 — Agent got stuck searching text `''` (closed 2025-10-01T21:26:01Z)
   - Issue detail: Type: <b>Bug</b> I asked a `#codebase` question in ask mode and it got stuck on a text search for what looks like an empty string <img width="975" height="486" alt="Image" src="https://github.com/user-attachments/assets/416f02f1-66d3-4362-9dc2-149e666a7c8e" /> Looking through the logs I didn't see any obvious errors VS Code version: Code - Insiders 1.105.0-insider (Universal)...
   - Issue: https://github.com/microsoft/vscode/issues/269417
   - Fix PR #269426 — Fix ripgrep when called with empty search string
   - PR: https://github.com/microsoft/vscode/pull/269426
   - Code excerpts:
     - src/vs/workbench/services/search/node/ripgrepTextSearchEngine.ts: +		if (!query.pattern) { +			return Promise.resolve({ limitHit: false }); +		} +

101. Issue #271081 — Chat: "Configure Empty State" is hard to understand (closed 2025-10-30T12:57:47Z)
   - Issue detail: <img width="250" height="123" alt="Image" src="https://github.com/user-attachments/assets/c0da1fdc-d661-4925-a3e7-8eddab33853c" /> This is a very technical menu item, for what a user probably does not understand what it is about. Can we rephrase? //cc @ntrogh
   - Issue: https://github.com/microsoft/vscode/issues/271081
   - Fix PR #274054 — Chat: "Configure Empty State" is hard to understand (fix #271081)
   - PR: https://github.com/microsoft/vscode/pull/274054
   - Code excerpts:
     - src/vs/platform/actions/common/actions.ts: +	static readonly ChatWelcomeContext = new MenuId('ChatWelcomeContext');
     - src/vs/workbench/contrib/chat/browser/actions/chatActions.ts: +				menu: [{ +				}, +				{ +					id: MenuId.ChatWelcomeContext, +					group: '2_settings', +					order: 1 +				}] +			precondition: ChatContextKeys.enabled, +			toggled: ContextKeyExpr.equals('confi

102. Issue #269451 — Agent fails to give input to compound tasks consistently (closed 2025-10-15T18:29:11Z)
   - Issue detail: Found while verifying https://github.com/microsoft/vscode/issues/264656 Notice how the `tunnel web` task doesn't require input but `serve web does`. The agent _says_ it looks for `serve web` task output but doesn't notice the "ok to proceed?". This behavior consistently repros in the scenario where `tunnel web` worked but `serve web` didn't. https://github.com/user-...
   - Issue: https://github.com/microsoft/vscode/issues/269451
   - Fix PR #270839 — Fix issues with monitoring dependency tasks
   - PR: https://github.com/microsoft/vscode/pull/270839
   - Code excerpts:
     - src/vs/workbench/contrib/tasks/browser/terminalTaskSystem.ts: +export interface IReconnectionTaskData {
     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/executeStrategy/executeStrategy.ts: +// Confirmation prompts ending with (y) e.g. "Ok to proceed? (y)" +const CONFIRM_Y_RE = /\(y\)\s*$/i; + +	return PS_CONFIRM_RE.test(cursorLine) || YN_PAIRED_RE.test(cursorLine) || YN_AFTER_PUNCT_RE.t

103. Issue #275774 — Suggest widget is cut off (closed 2025-11-07T09:27:04Z)
   - Issue detail: Testing #8078 * open a comment * type with completions * :bug: the suggest widget is behind the comment container fyi - the editor supports a overflowDomNode which should be used here <img width="684" height="327" alt="Image" src="https://github.com/user-attachments/assets/affb9952-59a9-4bbb-8d63-61bf94907849" />
   - Issue: https://github.com/microsoft/vscode/issues/275774
   - Fix PR #275775 — Revert "Fix suggest widget positioning in comment editors within diff views (#274093)"
   - PR: https://github.com/microsoft/vscode/pull/275775
   - Code excerpts:
     - src/vs/workbench/contrib/comments/browser/simpleCommentEditor.ts: +			fixedOverflowWidgets: true,

104. Issue #236318 — SCM - remove more debt from the quick diff (closed 2024-12-17T09:14:27Z)
   - Issue detail: <!-- Thank you for submitting a Pull Request. Please: * Read our Pull Request guidelines: https://github.com/microsoft/vscode/wiki/How-to-Contribute#pull-requests * Associate an issue with the Pull Request. * Ensure that the code is up-to-date with the `main` branch. * Include a description of the proposed changes and how to test them. -->
   - Issue: https://github.com/microsoft/vscode/pull/236318
   - Fix PR #269713 — Fix terminal voice indicator to move with dictated text
   - PR: https://github.com/microsoft/vscode/pull/269713
   - Code excerpts:
     - src/vs/workbench/contrib/terminalContrib/voice/browser/terminalVoice.ts: +					this._updateDecoration(); +		this._decoration?.dispose(); +		this._marker?.dispose(); + +		// Calculate x position based on current cursor position and input length +		const inputLength = this._

105. Issue #268367 — terminal input prompt shown count is off (closed 2025-09-25T18:33:39Z)
   - Issue detail: See how there are many times more accepts recorded than prompt shown events <img width="633" height="464" alt="Image" src="https://github.com/user-attachments/assets/25d5b620-bb8d-410a-aabe-fe2cffac4384" />
   - Issue: https://github.com/microsoft/vscode/issues/268367
   - Fix PR #268368 — replace observable with callback to fix telemetry
   - PR: https://github.com/microsoft/vscode/pull/268368
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatElicitationRequestPart.ts: +	private _hideOrDisposeCalled = false; +		public readonly onHideOrDispose?: () => void, +		if (!this._hideOrDisposeCalled && this.onHideOrDispose) { +			this.onHideOrDispose(); +			this._hideOrDispos
     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/tools/monitoring/outputMonitor.ts: +				undefined, // source +				moreActions, +				() => this._outputMonitorTelemetryCounters.inputToolManualShownCount++

106. Issue #272407 — Pressing Enter to confirm Japanese IME conversion simultaneously submits the "Create Branch" form (closed 2025-10-31T21:47:43Z)
   - Issue detail: Type: <b>Bug</b> **Bug Version:** 1.105.1 **Working Version (after downgrade):** 1.104.3 (Universal) **OS:** macOS **Steps to Reproduce:** 1. **Run VSCode with all extensions disabled** (`Code > Command Palette... > Developer: Reload With Extensions Disabled`). 2. Set the macOS input method to the default "Japanese - Romaji" IME (日本語 - ローマ字入力). 3. Open a project with a Git repository. 4. Try to...
   - Issue: https://github.com/microsoft/vscode/issues/272407
   - Fix PR #273453 — Prevent quickInput.accept from firing during IME composition. Fix #272407
   - PR: https://github.com/microsoft/vscode/pull/273453
   - Code excerpts:
     - src/vs/platform/quickinput/browser/quickInputActions.ts: +		inQuickInputContext, +		ContextKeyExpr.not('isComposing')

107. Issue #266235 — Release notes in product don't show TOC (closed 2025-09-16T23:12:28Z)
   - Issue detail: 1. Open release notes in product **bug** Toc is missing on left Here's what it should look like: <img width="506" height="505" alt="Image" src="https://github.com/user-attachments/assets/3c5089a3-298a-4e4a-b02b-be398d98140c" />
   - Issue: https://github.com/microsoft/vscode/issues/266235
   - Fix PR #266239 — Fix TOC in release notes
   - PR: https://github.com/microsoft/vscode/pull/266239
   - Code excerpts:
     - src/vs/workbench/contrib/update/browser/releaseNotesEditor.ts: +		// Remove HTML comment markers around table of contents navigation +		const rawFileContent = fileContent.text +			.replace(/<!--\s*TOC\s*/gi, '') +			.replace(/\s*Navigation End\s*-->/gi, ''); + +	

108. Issue #238058 — workaround for https://github.com/microsoft/vscode-copilot/issues/11639 (closed 2025-01-16T16:09:01Z)
   - Issue: https://github.com/microsoft/vscode/pull/238058
   - Fix PR #270080 — Fix: Rerun task not working for npm tasks in monorepos
   - PR: https://github.com/microsoft/vscode/pull/270080
   - Code excerpts:
     - src/vs/workbench/contrib/tasks/browser/abstractTaskService.ts: + +		// If task wasn't found in workspace configuration, check contributed tasks from providers +		// This is important for tasks from extensions like npm, which are ContributedTasks +		if (Contribute

109. Issue #273076 — Chat todos: do not auto expand by default (closed 2025-10-25T18:41:03Z)
   - Issue detail: Similar to how we do not expand the changes list by default, I would not expect the todos list to be expanded: <img width="727" height="404" alt="Image" src="https://github.com/user-attachments/assets/a6f3b751-1047-4853-b72f-e0067856c1ed" />
   - Issue: https://github.com/microsoft/vscode/issues/273076
   - Fix PR #273305 — Chat todos: do not auto expand by default (fix #273076)
   - PR: https://github.com/microsoft/vscode/pull/273305
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/chatTodoListWidget.ts: +	private _isExpanded: boolean = false;

110. Issue #267800 — Focus is lost after closing chat accessibility help dialog (closed 2025-09-22T16:42:15Z)
   - Issue detail: 1. focus chat input in panel 2. `alt+f1` 3. `escape` 4. 🐛 focus is lost, should be focusing the input box
   - Issue: https://github.com/microsoft/vscode/issues/267800
   - Fix PR #267801 — fix focus loss after closing a11y help from chat
   - PR: https://github.com/microsoft/vscode/pull/267801
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/actions/chatAccessibilityHelp.ts: +		return getChatAccessibilityHelpProvider(accessor, undefined, 'panelChat'); +		return getChatAccessibilityHelpProvider(accessor, undefined, 'quickChat'); +		return getChatAccessibilityHelpProvider(a

111. Issue #274237 — hidden chat terminals not restored on window reload (closed 2025-10-31T07:56:19Z)
   - Issue detail: 1. Have default terminal output location: none so that tool terminals are `hideFromUser: true`, `forcePersist: true` 2. run some things in the terminal using agent 3. do not click to focus the terminal 4. 🐛 neither action shows up on reload
   - Issue: https://github.com/microsoft/vscode/issues/274237
   - Fix PR #274243 — check against correct process id to fix hidden tool terminal restore
   - PR: https://github.com/microsoft/vscode/pull/274243
   - Code excerpts:
     - src/vs/workbench/contrib/terminalContrib/chat/browser/terminalChatService.ts: +			const instance = this._terminalService.instances.find(i => i.shellLaunchConfig.attachPersistentProcess?.id === this._pendingRestoredMappings.get(terminalToolSessionId)); +			if (persistentProcessI

112. Issue #263184 — Copy All from the Chat Pane Fails to Copy All of the Text of the Conversation (closed 2025-08-24T21:06:18Z)
   - Issue detail: Feature Request from Reporting Bug #5667 'Copy All' from the Chat Conversation does not Copy all the context. In my case it is missing a representation of all the cli commands it suggested & executed. (See log below – it just skips over the commands. The attached screenshot of what was actually in the window) <img width="413" alt="Image" src="https://github.com/user-...
   - Issue: https://github.com/microsoft/vscode/issues/263184
   - Fix PR #263185 — Fix #263184
   - PR: https://github.com/microsoft/vscode/pull/263185
   - Code excerpts:
     - src/vs/workbench/contrib/chat/common/chatModel.ts: +import { migrateLegacyTerminalToolSpecificData } from './chat.js'; +				case 'toolInvocation': +				case 'toolInvocationSerialized': +					// Include tool invocations in the copy text +					segment =

113. Issue #259879 — If none of the items have parents do not indent the items (closed 2025-11-19T02:04:07Z)
   - Issue detail: > If none of the items have parents do not indent the items: > <img width="609" height="119" alt="Image" src="https://github.com/user-attachments/assets/86b230fd-22e0-4c10-a8de-d445d9c60711" /> From @lszomoru in https://github.com/microsoft/vscode/issues/258769 This one is a little trickier because the tree does not give me an API to hide the whole twisty container. I'd have to do some nasty...
   - Issue: https://github.com/microsoft/vscode/issues/259879
   - Fix PR #277923 — Hide twisties and indentation when tree nodes have flat hierarchy
   - PR: https://github.com/microsoft/vscode/pull/277923
   - Code excerpts:
     - src/vs/platform/quickinput/browser/media/quickInput.css: +.quick-input-tree.quick-input-tree-flat .monaco-tl-indent, +.quick-input-tree.quick-input-tree-flat .monaco-tl-twistie { +	display: none !important; +} +
     - src/vs/platform/quickinput/browser/tree/quickInputTreeController.ts: +const flatHierarchyClass = 'quick-input-tree-flat'; +	private readonly _onDidCheckedLeafItemsChange = this._register(new Emitter<ReadonlyArray<IQuickTreeItem>>()); +		let hasNestedItems = false; +			

114. Issue #265325 — MCP Elicitation email check is reversed (closed 2025-09-05T15:51:48Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/265325
   - Fix PR #265326 — fix: elicitation email validator
   - PR: https://github.com/microsoft/vscode/pull/265326
   - Code excerpts:
     - src/vs/workbench/contrib/mcp/browser/mcpElicitationService.ts: +				return value.includes('@')

115. Issue #259835 — Firefox: changes to global stylesheets are not applied live (closed 2025-10-01T12:39:11Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/259835
   - Fix PR #269126 — fix: properly update cloned stylesheets on mutation in firefox
   - PR: https://github.com/microsoft/vscode/pull/269126
   - Code excerpts:
     - src/vs/base/browser/domStylesheets.ts: +import { isFirefox } from './browser.js'; +	disposables.add(sharedMutationObserver.observe(globalStylesheet, disposables, { childList: true, subtree: isFirefox, characterData: isFirefox })(() => {

116. Issue #271077 — New chat dropdown alt behaviour (closed 2025-10-13T08:38:55Z)
   - Issue detail: Nice change to add the dropdown for new chat button. However, you preserved the old behaviour of holding Alt to get the Alternative action. Now with the dropdown we should remove that (duplication and complicates things imho) fyi @roblourens <img width="99" height="92" alt="Image" src="https://github.com/user-attachments/assets/8e0c6dc4-94ce-4ec0-a1a4-63f6cc366265" />
   - Issue: https://github.com/microsoft/vscode/issues/271077
   - Fix PR #271083 — New chat dropdown alt behaviour (fix #271077)
   - PR: https://github.com/microsoft/vscode/pull/271083
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/actions/chatNewActions.ts: +import { ACTION_ID_NEW_CHAT, ACTION_ID_NEW_EDIT_SESSION, CHAT_CATEGORY, handleCurrentEditingSession } from './chatActions.js';

117. Issue #274876 — basic, none shell integration have no focus terminal action (closed 2025-11-06T20:04:23Z)
   - Issue detail: That's because `command` is undefined
   - Issue: https://github.com/microsoft/vscode/issues/274876
   - Fix PR #274893 — still show focus action even if no `command` so it's available for basic, none execute strategies
   - PR: https://github.com/microsoft/vscode/pull/274893
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts: +		const existingFocus = this._focusAction.value; +		if (existingFocus) { +			const existingIndex = actionBar.viewItems.findIndex(item => item.action === existingFocus); +			if (existingIndex >= 0) { 

118. Issue #247053 — TypeScript file semantic highlighting broken (closed 2025-10-30T16:56:39Z)
   - Issue detail: Semantic highlighting is broken in one file console spammed on every file change ![Image](https://github.com/user-attachments/assets/24cb2325-301d-46c9-9163-fbfd4eff9c88) editing the file does not fix it semantic highlighting still works in other files correctly but console still gets spammed on every file change https://github.com/user-attachments/assets/1288c452-4029-41d8-bb8a-85580021c1ba...
   - Issue: https://github.com/microsoft/vscode/issues/247053
   - Fix PR #274079 — Remove empty pieces when handling an edit
   - PR: https://github.com/microsoft/vscode/pull/274079
   - Code excerpts:
     - src/vs/editor/common/tokens/sparseTokensStore.ts: +		for (let i = 0; i < this._pieces.length; i++) { +			const piece = this._pieces[i]; + +			if (piece.isEmpty()) { +				// Remove empty pieces +				this._pieces.splice(i, 1); +				i--; +			}
     - src/vs/editor/test/common/model/tokensStore.test.ts: + +	test('piece with startLineNumber 0 and endLineNumber -1 after encompassing deletion', () => { +		const codec = new LanguageIdCodec(); +		const store = new SparseTokensStore(codec); + +		// Set ini

119. Issue #264915 — arc tracking bug (closed 2025-09-04T10:06:04Z)
   - Issue detail: This PR https://github.com/microsoft/vscode/pull/264895 caused the issue that the trackedEdit no longer leads to a document that the user edits act on, so they cannot be composed meaningfully.
   - Issue: https://github.com/microsoft/vscode/issues/264915
   - Fix PR #265111 — Fixes arc tracker bug
   - PR: https://github.com/microsoft/vscode/pull/265111
   - Code excerpts:
     - src/vs/editor/common/core/edits/stringEdit.ts: +	public removeCommonSuffixAndPrefix(source: string): TEdit { +	public applyOnText(docContents: StringText): StringText { +	public toStringEdit(filter?: (replacement: AnnotatedStringReplacement<T>) =>
     - src/vs/workbench/contrib/editTelemetry/common/arcTracker.dio.svg: +<svg host="65bd71144e" xmlns="http://www.w3.org/2000/svg" style="background: transparent; background-color: transparent;" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="721px" height

120. Issue #265932 — Images not showing in release notes (closed 2025-09-10T06:46:08Z)
   - Issue detail: 1. Open release notes or use the `open current files as release notes` command **Bug** Images and videos aren't shown
   - Issue: https://github.com/microsoft/vscode/issues/265932
   - Fix PR #265934 — Fix images in release notes
   - PR: https://github.com/microsoft/vscode/pull/265934
   - Code excerpts:
     - src/vs/base/browser/domSanitize.ts: +function hookDomPurifyHrefAndSrcSanitizer(allowedLinkProtocols: readonly string[] | '*', allowedMediaProtocols: readonly string[] | '*'): IDisposable { +		readonly override?: readonly string[] | '*';
     - src/vs/workbench/contrib/markdown/browser/markdownDocumentRenderer.ts: +		allowedMediaProtocols: sanitizerConfig?.allowedMediaProtocols, +	readonly allowedMediaProtocols?: { +		readonly override: readonly string[] | '*'; +	};

121. Issue #272352 — Terminal suggest: ability to group arg suggestions together (closed 2025-11-10T22:03:14Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/272352
   - Fix PR #276409 — Terminal suggest - include persistent options in suggestions and improve suggestion grouping
   - PR: https://github.com/microsoft/vscode/pull/276409
   - Code excerpts:
     - extensions/terminal-suggest/src/fig/figInterface.ts: +		await addSuggestions(parsedArguments.completionObj.persistentOptions, vscode.TerminalCompletionItemKind.Flag, parsedArguments);
     - extensions/terminal-suggest/src/test/fig.test.ts: +	}, +	{ +		name: 'Fig persistent options', +		completionSpecs: [ +			{ +				name: 'foo', +				description: 'Foo', +				options: [ +					{ name: '--help', description: 'Show help', isPersistent: true 

122. Issue #260819 — Allow commands in session (closed 2025-11-15T18:48:01Z)
   - Issue detail: This difference just occured to me. In other tools I can allow them in the session or the workspace. For terminal commands, it only offers to change my settings. Allowing a command just for a session would be nice. I sometimes would like to allow something riskier for a certain task but I know that I don't want it in my settings <img width="393" height="151" alt="Image"...
   - Issue: https://github.com/microsoft/vscode/issues/260819
   - Fix PR #277522 — Allow approving terminal tool for session
   - PR: https://github.com/microsoft/vscode/pull/277522
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolConfirmationSubPart.ts: +import { ITerminalChatService } from '../../../../terminal/browser/terminal.js'; +import { disableSessionAutoApprovalCommandId, openTerminalSettingsLinkCommandId } from './chatTerminalToolProgressPar
     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts: +export const disableSessionAutoApprovalCommandId = '_chat.disableSessionAutoApproval'; +CommandsRegistry.registerCommand(disableSessionAutoApprovalCommandId, async (accessor, chatSessionId: string) =

123. Issue #273084 — Chat todos: make the label briefer for the widget (closed 2025-10-27T18:19:03Z)
   - Issue detail: <img width="511" height="111" alt="Image" src="https://github.com/user-attachments/assets/f66c6b81-d6ca-4839-a8f9-a194686a89a6" /> I feel like we do not have to prefix with "Todo" for the label of the widget, just show the task its currently on.
   - Issue: https://github.com/microsoft/vscode/issues/273084
   - Fix PR #273368 — Chat todos: make the label briefer for the widget (fix #273084)
   - PR: https://github.com/microsoft/vscode/pull/273368
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/chatTodoListWidget.ts: +			? localize('chat.todoList.collapseButton', 'Collapse Todos') +			: localize('chat.todoList.expandButton', 'Expand Todos'); + +		if (this._isExpanded) { +			const titleText = dom.$('span'); +			tit
     - src/vs/workbench/contrib/chat/browser/media/chat.css: +	margin-right: 3px;

124. Issue #268595 — Terminal tool suggests to send the "any key" (closed 2025-11-10T16:54:20Z)
   - Issue detail: ``` * Executing task: npm run build source /Users/roblou/code/debugtest/.venv/bin/activate npm error Missing script: "build" npm error npm error To see a list of scripts, run: npm error npm run npm error A complete log of this run can be found in: /Users/roblou/.npm/_logs/2025-09-27T01_33_30_232Z-debug-0.log * The terminal process "/bin/zsh '-l', '-c', 'npm run build'" terminated with exit...
   - Issue: https://github.com/microsoft/vscode/issues/268595
   - Fix PR #268913 — prevent "any key" from being provided as an option
   - PR: https://github.com/microsoft/vscode/pull/268913
   - Code excerpts:
     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/tools/monitoring/outputMonitor.ts: +			`Analyze the following terminal output. If it contains a prompt requesting user input (such as a confirmation, selection, or yes/no question) and that prompt has NOT already been answered, extract

125. Issue #270736 — Auto approve rule added links aren't working (closed 2025-10-10T09:19:32Z)
   - Issue detail: <img width="409" height="808" alt="Image" src="https://github.com/user-attachments/assets/ed873ae6-b7df-4eea-9c35-5f22e82011ca" />
   - Issue: https://github.com/microsoft/vscode/issues/270736
   - Fix PR #270737 — Fix auto approve links for new rules
   - PR: https://github.com/microsoft/vscode/pull/270737
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolConfirmationSubPart.ts: +import { createCommandUri, MarkdownString, type IMarkdownString } from '../../../../../../base/common/htmlContent.js'; +import { openTerminalSettingsLinkCommandId } from './chatTerminalToolProgressPa

126. Issue #273973 — Debugging web server + edge shows odd coloring in chat input (closed 2025-10-30T16:35:39Z)
   - Issue detail: <img width="297" height="263" alt="Image" src="https://github.com/user-attachments/assets/4f63f7ef-2553-4413-ae2f-293fa9c948c8" /> I don't see this in codespaces though which in theory should be the same.
   - Issue: https://github.com/microsoft/vscode/issues/273973
   - Fix PR #274051 — Debugging web server + edge shows odd coloring in chat input (fix #273973)
   - PR: https://github.com/microsoft/vscode/pull/274051
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/media/chat.css: +	background-color: var(--vscode-input-background) !important;

127. Issue #272584 — Agent Handoffs: Handoff-provided agent is used for sending, but isn't sticky and resets (closed 2025-10-22T04:37:39Z)
   - Issue detail: - Use a mode with handoffs set to `send: true` and `agent` - Trigger a handoffs to be shown - Picking a handoff correctly sends it with the right `agent` - 🐛 `agent` isn't persisted in chat as current custom agent https://github.com/user-attachments/assets/5ef7499c-272e-406a-b1eb-2e08b516de21 ``` --- description: TDD Green phase handoffs: - label: 🟥 RED agent: tdd-red prompt: Next test send:...
   - Issue: https://github.com/microsoft/vscode/issues/272584
   - Fix PR #272624 — Include input state when adding history
   - PR: https://github.com/microsoft/vscode/pull/272624
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatInputPart.ts: +			this.history.add({ text: '', state: this.getInputState() });

128. Issue #270701 — Build failed (closed 2025-10-10T04:37:43Z)
   - Issue detail: Build: https://dev.azure.com/monacotools/a6d41577-0fa3-498e-af22-257312ff0545/_build/results?buildId=363562 Changes: https://github.com/Microsoft/vscode/compare/a361925...691bcc6
   - Issue: https://github.com/microsoft/vscode/issues/270701
   - Fix PR #270695 — Fixes build issue caused by extensionMcpDiscovery tests
   - PR: https://github.com/microsoft/vscode/pull/270695
   - Code excerpts:
     - src/vs/workbench/contrib/mcp/test/common/discovery/extensionMcpDiscovery.test.ts: + +	public handleExtensionChangeTest( +			fixture.extensionMcpDiscovery.handleExtensionChangeTest([], delta); +			fixture.extensionMcpDiscovery.handleExtensionChangeTest([], delta); +			fixture.extens

129. Issue #261554 — Chat tile should immediately reflect coding agent PR title (closed 2025-10-20T22:38:12Z)
   - Issue detail: Steps to Reproduce: 1. Open a GitHub Copilot coding agent PR from the chat sessions view. Expected: Chat immediately shows name from the "GitHub Copilot Coding agent" section that was clicked on. Actual: Chat shows "Chat 6" until the full log is loaded into chat. However, the chat tile was already available locally and should have immediately been reflected in the chat title name as a tab.
   - Issue: https://github.com/microsoft/vscode/issues/261554
   - Fix PR #272360 — Show chat item title while loading in editor
   - PR: https://github.com/microsoft/vscode/pull/272360
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatEditorInput.ts: +		// If a preferred title was provided in options, use it +		if (this.options.title?.preferred) { +			return this.options.title.preferred; +		} +

130. Issue #271507 — Empty placeholders show empty hovers (closed 2025-10-18T22:28:13Z)
   - Issue detail: Repro: - Set `"files.simpleDialog.enable": true` - Open a file - Save as - Hover the input <img width="673" height="211" alt="Image" src="https://github.com/user-attachments/assets/96c53d98-118a-4289-a6e1-7c8741b901c1" />
   - Issue: https://github.com/microsoft/vscode/issues/271507
   - Fix PR #272108 — Prevent hover creation if content is empty string
   - PR: https://github.com/microsoft/vscode/pull/272108
   - Code excerpts:
     - src/vs/editor/browser/services/hoverService/hoverService.ts: +		if (options.content === '') { +			return undefined; +		} +

131. Issue #249963 — Git - Missing action to "Open File" from a staged new file (closed 2025-11-02T18:21:46Z)
   - Issue detail: Steps to Reproduce: 1. stage a new file to index 2. click it => I am missing the action to "Open File" ![Image](https://github.com/user-attachments/assets/1592cdf9-5e74-49dd-b265-8efea6301a63)
   - Issue: https://github.com/microsoft/vscode/issues/249963
   - Fix PR #274182 — Git - Missing action to "Open File" from a staged new file (fix #249963)
   - PR: https://github.com/microsoft/vscode/pull/274182
   - Code excerpts:
     - extensions/git/package.json: +        { +          "command": "git.openFile", +          "group": "navigation", +          "when": "config.git.enabled && !git.missing && gitOpenRepositoryCount != 0 && !isInDiffEditor && !isInNote

132. Issue #271624 — When I edit and resubmit a previous request, `.github/instructions/*.instructions.md` files are ignored (closed 2025-10-21T17:10:13Z)
   - Issue detail: Version: 1.106.0-insider (Universal) Commit: f030344cf19e76e6b47d2d8ab003780a7fdb8171 Date: 2025-10-15T05:02:11.625Z Electron: 37.6.0 ElectronBuildId: 12506819 Chromium: 138.0.7204.251 Node.js: 22.19.0 V8: 13.8.258.32-electron.0 OS: Darwin arm64 24.6.0 Name: GitHub Copilot Chat Id: GitHub.copilot-chat Description: AI chat features powered by Copilot Version: 0.33.2025101503 Publisher: GitHub VS...
   - Issue: https://github.com/microsoft/vscode/issues/271624
   - Fix PR #272020 — chat: always apply prompt file and auto-attach instructions. Fix #271624
   - PR: https://github.com/microsoft/vscode/pull/272020
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatWidget.ts: +			// process the prompt command +			await this._applyPromptFileIfSet(requestInputs); +			await this._autoAttachInstructions(requestInputs);

133. Issue #5545 — optimize glob.match for common cases (closed 2016-04-21T07:21:34Z)
   - Issue detail: Assuming many, many glob patterns look like `**/*.txt` or `{**/*.js,**/*.ts}` it's IMO fair to optimise those `string#endsWith` checks
   - Issue: https://github.com/microsoft/vscode/pull/5545
   - Fix PR #265341 — Fix #5545 using onDidRefetchAssignments event
   - PR: https://github.com/microsoft/vscode/pull/265341
   - Code excerpts:
     - src/vs/workbench/services/configuration/browser/configurationService.ts: +import { Disposable, DisposableStore } from '../../../../base/common/lifecycle.js'; +import { Queue, Barrier, Promises, Delayer, Throttler } from '../../../../base/common/async.js'; +	private readonl

134. Issue #275957 — Infinite loop with UI flicker when delegating to Copilot CLI Agent (closed 2025-11-07T01:16:44Z)
   - Issue detail: Type: <b>Bug</b> I typed in a prompt in the chat pane, clicked the Delegate to Agent button, selected the CLI agent, and this happened: https://github.com/user-attachments/assets/3676e1f5-be29-43a5-8a57-0d425c46b420 Extension version: 0.33.2025110604 VS Code version: Code - Insiders 1.106.0-insider (Universal) (a756ce92e43f0e762c8899e64df123eb2d7101b1, 2025-11-06T21:20:04.075Z) OS version:...
   - Issue: https://github.com/microsoft/vscode/issues/275957
   - Fix PR #275972 — Targeted fix for supporting non-local sessions in code paths that aren't using uris
   - PR: https://github.com/microsoft/vscode/pull/275972
   - Code excerpts:
     - src/vs/workbench/api/browser/mainThreadChatAgents2.ts: +				const chatSession = this._chatService.getSessionByLegacyId(request.sessionId);
     - src/vs/workbench/contrib/chat/common/chatService.ts: +	getSessionByLegacyId(sessionId: string): IChatModel | undefined;

135. Issue #266059 — dictation actions are appearing in chat toolbar (closed 2025-09-10T15:54:39Z)
   - Issue detail: <img width="406" height="133" alt="Image" src="https://github.com/user-attachments/assets/f7d14f81-ad16-42a5-8e2e-33ba5be32df4" />
   - Issue: https://github.com/microsoft/vscode/issues/266059
   - Fix PR #266060 — fix terminal voice action menu config
   - PR: https://github.com/microsoft/vscode/pull/266060
   - Code excerpts:
     - src/vs/workbench/contrib/terminal/browser/terminalMenus.ts: +				}, +			}, +			{ +				id: MenuId.ViewTitle, +				item: { +					command: { +						id: TerminalCommandId.StartVoice, +						title: localize('workbench.action.terminal.startVoice', "Start Voice"), +	

136. Issue #136574 — Change Focus Area Issue While Debugging (closed 2025-10-09T23:25:55Z)
   - Issue detail: Issue Type: <b>Bug</b> When I have multiple windows open and I have different focus areas set for each. Then when I try to debug the code and if it returns an error, it shows an error on both windows on that line and also changes the position to that error for both windows and I have re-navigate to the desired area again, however, it should only change position for the active window and not the...
   - Issue: https://github.com/microsoft/vscode/issues/136574
   - Fix PR #270615 — Fix debug exception navigation appearing in all editor groups
   - PR: https://github.com/microsoft/vscode/pull/270615
   - Code excerpts:
     - src/vs/workbench/contrib/debug/browser/debugEditorContribution.ts: +import { IEditorService } from '../../../services/editor/common/editorService.js'; +		@ILanguageFeatureDebounceService featureDebounceService: ILanguageFeatureDebounceService, +		@IEditorService priv

137. Issue #272829 — Chat: "Pick Model" appears with empty picker if aborting chat setup (closed 2025-10-31T08:50:49Z)
   - Issue detail: Steps to Reproduce: 1. fresh setup 2. send a chat message 3. cancel sign in dialog => 🐛 <img width="332" height="180" alt="Image" src="https://github.com/user-attachments/assets/58f3e66f-4f31-41e0-9c95-91427a40083d" />
   - Issue: https://github.com/microsoft/vscode/issues/272829
   - Fix PR #274272 — Chat: "Pick Model" appears with empty picker if aborting chat setup (fix #272829)
   - PR: https://github.com/microsoft/vscode/pull/274272
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/modelPicker/modelPickerActionItem.ts: +					tooltip: localize('chat.manageModels.tooltip', "Manage Language Models"), +			// Add sign-in / upgrade option if entitlement is anonymous / free / new user +			const isNewOrAnonymousUser = !chat

138. Issue #275320 — Agent sessions single view: clicking on PR number opens session and PR description (closed 2025-11-06T11:26:42Z)
   - Issue detail: Testing #274477 Clicking on the PR number on the description of a copilot agent session will first open the chat session in the editor and then open the PR description. <img width="789" height="324" alt="Image" src="https://github.com/user-attachments/assets/91655314-e83b-407e-9c67-41a37c8317e7" />
   - Issue: https://github.com/microsoft/vscode/issues/275320
   - Fix PR #275790 — Agent sessions single view: clicking on PR number opens session and PR description (fix #275320)
   - PR: https://github.com/microsoft/vscode/pull/275790
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/agentSessions/agentSessionsViewer.ts: +import { addDisposableListener, EventType, h } from '../../../../../base/browser/dom.js'; + +			// TODO@bpasero this is needed so that a user can click into a link of the session +			// without openi

139. Issue #270711 — Move accent normalization into filters.ts (closed 2025-11-11T23:58:08Z)
   - Issue detail: https://github.com/microsoft/vscode/pull/270248 adds special handling of characters with accents to commandQuickAccess.ts, a similar mechanism exists for Korean characters currently here: https://github.com/microsoft/vscode/blob/f1b211e5ebf03457cd55e869dc33af09e681e358/src/vs/base/common/filters.ts#L138-L163 We should move the accent logic here as well, that way it's handled in more parts of...
   - Issue: https://github.com/microsoft/vscode/issues/270711
   - Fix PR #276798 — Move accent-insensitive filtering to common
   - PR: https://github.com/microsoft/vscode/pull/276798
   - Code excerpts:
     - src/vs/base/common/filters.ts: +import { tryNormalizeToBase } from './normalization.js'; +	if (word.length > wordToMatchAgainst.length) { +		return null; +	} + +export function matchesBaseContiguousSubString(word: string, wordToMat
     - src/vs/base/common/normalization.ts: +/** + * Attempts to normalize the string to Unicode base format (NFD -> remove accents -> lower case). + * When original string contains accent characters directly, only lower casing will be performe

140. Issue #265797 — Leaked disposable: `LocalTerminalBackend.createProcess` (closed 2025-09-09T14:40:24Z)
   - Issue detail: I was going through some ext host restarts: ``` [94394:0909/103019.483796:INFO:CONSOLE:24] "[LEAKED DISPOSABLE] Error: CREATED via: at GCBasedDisposableTracker.trackDisposable (vscode-file://vscode-app/Users/bpasero/Development/Microsoft/vscode/out/vs/base/common/lifecycle.js:28:23) at trackDisposable (vscode-file://vscode-...
   - Issue: https://github.com/microsoft/vscode/issues/265797
   - Fix PR #265852 — Fix disposable leak in terminal backends
   - PR: https://github.com/microsoft/vscode/pull/265852
   - Code excerpts:
     - src/vs/workbench/contrib/terminal/browser/remoteTerminalBackend.ts: +				pty.dispose();
     - src/vs/workbench/contrib/terminal/electron-browser/localTerminalBackend.ts: +					pty.dispose();
141. Issue #268390 — Secondary side bar shouldnt open by default in vscode.dev (closed 2025-09-27T05:12:56Z)
   - Issue detail: When we switched to show the secondary side bar with the walkthrough or in a new workspace, this is also getting applied in vscode.dev. We shouldn't open the secondary side bar in these scenarios as Copilot is not supported <img width="2540" height="1382" alt="Image" src="https://github.com/user-attachments/assets/57c03b29-9abd-4ffa-b7ae-5472750e80db" /> Thanks @kieferrm for pointing this out!
   - Issue: https://github.com/microsoft/vscode/issues/268390
   - Fix PR #268606 — Secondary side bar shouldnt open by default in vscode.dev (fix #268390)
   - PR: https://github.com/microsoft/vscode/pull/268606
   - Code excerpts:
     - src/vs/workbench/browser/layout.ts: +		this.stateModel = new LayoutStateModel(this.storageService, this.configurationService, this.contextService, this.environmentService); +		private readonly environmentService: IBrowserWorkbenchEnviro

142. Issue #264465 — Node.js Debugger - Watch contect menu 'Copy Value' not copying value (closed 2025-09-08T22:09:22Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/264465
   - Fix PR #265746 — debug: fix watch 'copy value' not working
   - PR: https://github.com/microsoft/vscode/pull/265746
   - Code excerpts:
     - src/vs/workbench/contrib/debug/browser/debug.contribution.ts: +registerDebugViewMenuItem(MenuId.DebugWatchContext, COPY_EVALUATE_PATH_ID, COPY_EVALUATE_PATH_LABEL, 50, CONTEXT_VARIABLE_EVALUATE_NAME_PRESENT, CONTEXT_IN_DEBUG_MODE, '3_modification');
     - src/vs/workbench/contrib/debug/browser/variablesView.ts: +			elements = [arg]; +	handler: async (accessor: ServicesAccessor, context: IVariablesContext | Variable) => { +		if (context instanceof Variable) { +			await clipboardService.writeText(context.evalu

143. Issue #277296 — Moving chat into editor from secondary side bar results in error in 1.106 (closed 2025-11-14T21:19:19Z)
   - Issue detail: Steps to Reproduce: 1. Open secondary side bar Chat 2. Click the ... > Move Chat into editor area <img width="2553" height="1338" alt="Image" src="https://github.com/user-attachments/assets/26ab6e7f-da38-45fb-8107-ce7e2f37c9ad" /> ``` 2025-11-13 16:28:12.802 [error] [Window] ChatSessionStore: Error reading chat session file 6f413a8b-4ebb-4b80-9316-f27b70908638 Unable to read file 'vscode-...
   - Issue: https://github.com/microsoft/vscode/issues/277296
   - Fix PR #277523 — Fall back to opening new session if local session restore fails
   - PR: https://github.com/microsoft/vscode/pull/277523
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatEditorInput.ts: +		if (this._sessionResource) { +			this.model = await this.chatService.loadSessionForResource(this._sessionResource, ChatAgentLocation.Chat, CancellationToken.None); + +			// For local session only, 

144. Issue #274298 — Chat: Title of desktop notification should be static: "Copilot" or "Visual Studio Code" (closed 2025-10-31T10:38:26Z)
   - Issue detail: It always confuses me whenever a desktop notification shows up from our Copilot since it uses literally the conversation title (defaulting to the first message) and a bit of the response: <img width="410" height="164" alt="Image" src="https://github.com/user-attachments/assets/6ad86dae-3df3-46d6-8e38-857e28333515" /> It really isn't intuitive for me to understand its meaning and I have to open...
   - Issue: https://github.com/microsoft/vscode/issues/274298
   - Fix PR #274305 — Chat: Title of desktop notification should be static: "Copilot" or "Visual Studio Code" (fix #274298)
   - PR: https://github.com/microsoft/vscode/pull/274305
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatAccessibilityService.ts: +		const title = widget?.viewModel?.model.title ? localize('chatTitle', "Chat: {0}", widget.viewModel.model.title) : localize('chat.untitledChat', "Untitled Chat"); +		const notification = await dom.t
     - src/vs/workbench/contrib/chat/browser/chatContentParts/chatConfirmationWidget.ts: +import { IRenderedMarkdown } from '../../../../../base/browser/markdownRenderer.js'; +	async notify(targetWindow: Window, sessionId: string): Promise<void> { +		const widget = this._chatWidgetService

145. Issue #268298 — Chat sessions view hover uses `mouse` placement. It should however use `element` placement (closed 2025-11-08T18:39:14Z)
   - Issue detail: The hover in the chat sessions view will render above other entries in the view. <img width="706" height="196" alt="Image" src="https://github.com/user-attachments/assets/cef6ec58-aa50-411f-9fd3-9010e69a3b41" /> This is not ideal. When a tree item has a large hover, we normally ty to render them to the side of the tree items so it doesn't block other entries. See how we do it for the scm graph...
   - Issue: https://github.com/microsoft/vscode/issues/268298
   - Fix PR #269780 — Update chat sessions hover to not block the items
   - PR: https://github.com/microsoft/vscode/pull/269780
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatSessions/view/chatSessionsView.ts: +					const viewId = `${VIEWLET_ID}.${provider.chatSessionType}`; +						id: viewId, +						ctorDescriptor: new SyncDescriptor(SessionsViewPane, [provider, this.sessionTracker, viewId]), +					ctorDes
     - src/vs/workbench/contrib/chat/browser/chatSessions/view/sessionsTreeRenderer.ts: +import { HoverPosition } from '../../../../../../base/browser/ui/hover/hoverWidget.js'; +import { IWorkbenchLayoutService, Position } from '../../../../../services/layout/browser/layoutService.js'; +

146. Issue #252934 — When there is only one level of nodes and all of them display checkboxes, CustomTreeView has indentation issues (closed 2025-11-14T16:43:11Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/252934
   - Fix PR #277461 — Improve checkbox alignment in trees
   - PR: https://github.com/microsoft/vscode/pull/277461
   - Code excerpts:
     - src/vs/workbench/browser/parts/views/treeView.ts: +		container.parentElement!.classList.toggle('align-icon-with-twisty', this.aligner.alignIconWithTwisty(treeItem)); +		if (!this.hasIconOrCheckbox(treeItem)) { +			const root = this._tree.getInput(); 

147. Issue #264772 — Leak warnings when opening chat sessions view (closed 2025-09-02T22:10:31Z)
   - Issue detail: Testing https://github.com/microsoft/vscode/issues/264256 1. Open chat sessions view **Bug** Dev tools shows a number of potential leak warnings
   - Issue: https://github.com/microsoft/vscode/issues/264772
   - Fix PR #264773 — Fix chat session view leak warnings
   - PR: https://github.com/microsoft/vscode/pull/264773
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatSessions.ts: +	readonly container: HTMLElement; +	readonly resourceLabel: IResourceLabel; +	readonly actionBar: ActionBar; +	readonly elementDisposable: DisposableStore; +	readonly timestamp: HTMLElement; +	readon

148. Issue #278394 — Decorations Flicker (closed 2025-11-19T20:01:17Z)
   - Issue detail: In the diff editor, decorations (and even selections) sometimes flicker / are not rendered immediately: ![Image](https://github.com/user-attachments/assets/fc71df67-f1ef-453c-bc00-064f7742f871) * To repro in Code OSS, you need gitlens installed * Open the "agentSessionsViewer.ts" from 59af9cbe461df446c9d5e86f66c10749ccbcf756 in the git graph view * You also need this turned on: <img width="373"...
   - Issue: https://github.com/microsoft/vscode/issues/278394
   - Fix PR #278419 — Avoid re-rendering unnecessarily and remove unnecessary dom reading guard
   - PR: https://github.com/microsoft/vscode/pull/278419
   - Code excerpts:
     - src/vs/editor/browser/viewParts/viewLines/viewLines.ts: +		return this._visibleLines.onScrollChanged(e) || e.scrollTopChanged || e.scrollLeftChanged;

149. Issue #257095 — When chat response contains diff marking, diff sounds play (closed 2025-10-10T19:31:12Z)
   - Issue detail: From @jooyoungseo Accessibility.signals like `accessibility.signals.diffLineDeleted` are being used when they shouldn't be
   - Issue: https://github.com/microsoft/vscode/issues/257095
   - Fix PR #270808 — don't play diff sounds unless relevant in accessible view
   - PR: https://github.com/microsoft/vscode/pull/270808
   - Code excerpts:
     - src/vs/workbench/contrib/accessibility/browser/accessibleView.ts: +		if (this._currentProvider?.id !== AccessibleViewProviderId.DiffEditor && this._currentProvider?.id !== AccessibleViewProviderId.InlineCompletions) { +			return; +		}

150. Issue #277164 — Both terminal suggest providers off by default in stable (closed 2025-11-14T18:05:30Z)
   - Issue detail: <img width="467" height="136" alt="Image" src="https://github.com/user-attachments/assets/5f040c47-d95a-4654-906d-383d2fab3df1" /> https://github.com/microsoft/vscode/blob/6f121ab5a7ea4b28993911c5da76a1e2ffdaaab8/src/vs/workbench/contrib/terminalContrib/suggest/common/terminalSuggestConfiguration.ts#L200
   - Issue: https://github.com/microsoft/vscode/issues/277164
   - Fix PR #277169 — enable suggest providers by default
   - PR: https://github.com/microsoft/vscode/pull/277169
   - Code excerpts:
     - src/vs/workbench/contrib/terminalContrib/suggest/common/terminalSuggestConfiguration.ts: +			default: true, +				markdownDescription: localize('suggest.providersEnabledByDefault', "Controls which suggestions automatically show up while typing. Suggestion providers are enabled by default."

151. Issue #264122 — `instance LanguageModelToolResultPart` is false for tool results (closed 2025-09-04T23:49:30Z)
   - Issue detail: 1. Implement a chat language model provider that supports tool calling and performs a `instance LanguageModelToolResultPart` check as part of converting from VS Code chat types to OpenAI chat messages 2. Use it in agent mode 3. :bug: `instance LanguageModelToolResultPart` is always false for `LanguageModelChatMessage.content` parts that contain tool results cc @lramos15
   - Issue: https://github.com/microsoft/vscode/issues/264122
   - Fix PR #264362 — Fix LanguageModelToolResultPart2 inheritance for instanceof checks
   - PR: https://github.com/microsoft/vscode/pull/264362
   - Code excerpts:
     - src/vs/workbench/api/common/extHostTypes.ts: +export class LanguageModelToolResultPart2 extends LanguageModelToolResultPart implements vscode.LanguageModelToolResultPart2 { +	declare content: (LanguageModelTextPart | LanguageModelPromptTsxPart |
     - src/vs/workbench/api/test/browser/extHostTypes.test.ts: + +	test('LanguageModelToolResultPart2 instanceof LanguageModelToolResultPart', function () { +		// Test that LanguageModelToolResultPart2 extends LanguageModelToolResultPart for instanceof checks +		

152. Issue #258022 — Changing textEditor size breaks wrap on newline feature (closed 2025-09-15T22:27:28Z)
   - Issue detail: Just want to say I love the new wrap on newline feature * https://github.com/microsoft/vscode/pull/231120 however when changing the size of the textEditor, it breaks the feature returning back to normal wordwrap and completely destroys the editor in large files Steps to Reproduce: 1. enable setting `"editor.wrapOnEscapedLineFeeds": true` 2. open JSON file containing strings with newlines 3....
   - Issue: https://github.com/microsoft/vscode/issues/258022
   - Fix PR #258407 — Fix soft wrapping on \n
   - PR: https://github.com/microsoft/vscode/pull/258407
   - Code excerpts:
     - src/vs/editor/common/viewModel/monospaceLineBreaksComputer.ts: +					const lineText = requests[i]; +					const isLineFeedWrappingEnabled = wrapOnEscapedLineFeeds && lineText.includes('"') && lineText.includes('\\n'); +					if (previousLineBreakData && !previousLi
     - src/vs/editor/test/common/viewModel/monospaceLineBreaksComputer.test.ts: +	test('issue #258022: wrapOnEscapedLineFeeds: should work correctly after editor resize', () => { +		const text = '"Short text with\\nescaped newline and an escaped\\\\nbackslash"';

153. Issue #274871 — move setNextCommandId to ptyService from processManager (closed 2025-11-12T18:13:32Z)
   - Issue detail: This isn't great that there are a bunch of no-op ones. That's due to being on `ITerminalChildProcess`? Could we put it on `IPtyService` instead? _Originally posted by @Tyriar in https://github.com/microsoft/vscode/pull/274417#discussion_r2483718516_
   - Issue: https://github.com/microsoft/vscode/issues/274871
   - Fix PR #276967 — move `setNextCommandId` from `ITerminalChildProcess` to `IPtyService`
   - PR: https://github.com/microsoft/vscode/pull/276967
   - Code excerpts:
     - src/vs/platform/terminal/common/terminal.ts: +	setNextCommandId(id: number, commandLine: string, commandId: string): Promise<void>;

154. Issue #265382 — Button should not grow vertically when there's horizontal space (closed 2025-09-05T18:42:01Z)
   - Issue detail: From @digitarald cc @connor4312 and @justschen for the chat elicitation request part <img width="421" height="183" alt="Image" src="https://github.com/user-attachments/assets/15925c8e-6ae3-4a81-8431-de65de62811b" />
   - Issue: https://github.com/microsoft/vscode/issues/265382
   - Fix PR #265390 — fix button growing vertically in confirmation widget
   - PR: https://github.com/microsoft/vscode/pull/265390
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/media/chatConfirmationWidget.css: +.chat-confirmation-widget .monaco-text-button { +	padding: 0 12px; +	min-height: 2em; +	box-sizing: border-box; +} +

155. Issue #274411 — Allow setting keybinding to focus the chat terminal and to focus /expand last chat terminal output (closed 2025-11-13T19:01:50Z)
   - Issue detail: cc @jooyoungseo, @rperez030 Currently, this action is not registered, so a user cannot set this https://github.com/microsoft/vscode/blob/b770d1f0fa2dbc440735e7b9e1d67e4257f8c06a/src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts#L527-L541
   - Issue: https://github.com/microsoft/vscode/issues/274411
   - Fix PR #276941 — Add keybindings to reveal/focus last chat terminal, focus output
   - PR: https://github.com/microsoft/vscode/pull/276941
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/actions/chatAccessibilityHelp.ts: +		content.push(localize('chat.focusMostRecentTerminal', 'To focus the last chat terminal that ran a tool, invoke the Focus Most Recent Chat Terminal command{0}.', '<keybinding:workbench.action.chat.f
     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts: +import { KeyCode, KeyMod } from '../../../../../../base/common/keyCodes.js'; +import { IInstantiationService, ServicesAccessor } from '../../../../../../platform/instantiation/common/instantiation.js

156. Issue #275317 — Go To Line command: Improve Discoverability of Offset Mode (closed 2025-11-11T22:54:34Z)
   - Issue detail: Testing #274949 IMO, I think we can add a new command "Go To Offset" which can pre-populate the bar with `::`, similar to how "Go To Line/Column" pre-populates with `:`. This can help with some discoverability even if there is no keybinding for it.
   - Issue: https://github.com/microsoft/vscode/issues/275317
   - Fix PR #276632 — Add 'Go to Offset...' command
   - PR: https://github.com/microsoft/vscode/pull/276632
   - Code excerpts:
     - src/vs/editor/common/standaloneStrings.ts: +	export const gotoOffsetActionLabel = nls.localize('gotoOffsetActionLabel', "Go to Offset...");
     - src/vs/editor/contrib/quickAccess/browser/gotoLineQuickAccess.ts: +	static readonly GO_TO_LINE_PREFIX = ':'; +	static readonly GO_TO_OFFSET_PREFIX = '::'; +		const label = localize('gotoLine.noEditor', "Open a text editor first to go to a line or an offset."); +			c

157. Issue #236827 — Method moved from file A to B. It caused both editor and source control issues (closed 2025-01-29T11:25:38Z)
   - Issue detail: Type: <b>Bug</b> Before you close it as a duplicate: It is NOT the known line ending issue. A whole function misses. Steps that I did: - Added a method `ManageUrlsHandler` to a file dashboard.go - Later, I moved it to shortener_handler.go (I used CTRL-X; CTRL-V) Experienced: - When I open dashboard.go, it doesn't show any change ![Image](https://github.com/user-...
   - Issue: https://github.com/microsoft/vscode/issues/236827
   - Fix PR #278316 — Update inline chat dialog to use correct product terminology
   - PR: https://github.com/microsoft/vscode/pull/278316
   - Code excerpts:
     - src/vs/workbench/contrib/inlineChat/browser/inlineChatSessionServiceImpl.ts: +					// Use previously stored user preference: true = 'Continue in Chat view', false = 'Rephrase' (Cancel) +						title: localize('confirm.title', "Do you want to continue in Chat view?"), +						mes

158. Issue #208434 — Do not recommend extensions if language is set via auto detection (closed 2025-10-07T21:20:26Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/208434
   - Fix PR #269776 — Do not recommend extensions if language is set via auto detection
   - PR: https://github.com/microsoft/vscode/pull/269776
   - Code excerpts:
     - src/vs/workbench/contrib/extensions/browser/fileBasedRecommendations.ts: +import { IUntitledTextEditorService } from '../../../services/untitled/common/untitledTextEditorService.js'; +// Minimum length of untitled file to allow triggering extension recommendations for auto

159. Issue #263926 — Window hangs when prompting to continue waiting for terminal (closed 2025-08-29T00:50:53Z)
   - Issue detail: Reported by Simon originally but I can repro <img width="2245" height="1274" alt="Image" src="https://github.com/user-attachments/assets/de36292c-3145-42a3-bbad-06db197ac456" /> First I made this modification hoping to be able to trigger it faster <img width="495" height="238" alt="Image" src="https://github.com/user-attachments/assets/88c67ded-039c-47f0-aa12-6510581c5dbe" /> Then "run top in a...
   - Issue: https://github.com/microsoft/vscode/issues/263926
   - Fix PR #263934 — fix state issue with terminal polling
   - PR: https://github.com/microsoft/vscode/pull/263934
   - Code excerpts:
     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/tools/monitoring/outputMonitor.ts: +	private _promptPart: ChatElicitationRequestPart | undefined; + +							this._promptPart?.hide(); +							this._promptPart?.dispose(); +							this._promptPart = undefined; +			this._promptPart?.hide

160. Issue #275605 — Copilot Agent blocked by "Press any key to continue ..." - Loss of autonomous capabilities (closed 2025-11-10T18:10:12Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/275605
   - Fix PR #276554 — detect `press any/a key` and ask if user wants to send `a` to terminal
   - PR: https://github.com/microsoft/vscode/pull/276554
   - Code excerpts:
     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/executeStrategy/executeStrategy.ts: +const ANY_KEY = /press any key|press a key/i; + +	return PS_CONFIRM_RE.test(cursorLine) || YN_PAIRED_RE.test(cursorLine) || YN_AFTER_PUNCT_RE.test(cursorLine) || CONFIRM_Y_RE.test(cursorLine) || LINE
     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/tools/monitoring/outputMonitor.ts: +			`Analyze the following terminal output. If it contains a prompt requesting user input (such as a confirmation, selection, or yes/no question) and that prompt has NOT already been answered, extract

161. Issue #276458 — Comments fail to re-expand after collapse in outdated/specific-commit-version files (closed 2025-11-10T15:32:51Z)
   - Issue detail: Attempting to expand/uncollapse comment after collapsing does not appear to work when viewing outdated or specific version of a file in a PR. Versions in question: - Extension version: github.vscode-pull-request-github 0.121.2025110514 - VSCode Version: 1.106.0-insider (Universal) 18d828e5d596e56b516fac7baa53e4b32cf087be - OS: Darwin arm64 24.6.0- Repository Clone Configuration (single...
   - Issue: https://github.com/microsoft/vscode/issues/276458
   - Fix PR #276464 — Comments fail to re-expand after collapse in outdated/specific-commit-version files
   - PR: https://github.com/microsoft/vscode/pull/276464
   - Code excerpts:
     - src/vs/workbench/contrib/comments/browser/commentsController.ts: +		this.mouseDownInfo = (e.target.element?.className.indexOf('comment-range-glyph') ?? -1) >= 0 ? parseMouseDownInfoFromEvent(e) : null;

162. Issue #276833 — No keyboard shortcut for "wait for task"? (closed 2025-11-12T17:07:10Z)
   - Issue detail: I expected this to have the cmd+enter keybinding like other confirmations <img width="564" height="232" alt="Image" src="https://github.com/user-attachments/assets/6c307499-7409-4b6f-8b04-71398d4ef858" /> Never mind that it used the task tool to run a test task instead of the test tool...
   - Issue: https://github.com/microsoft/vscode/issues/276833
   - Fix PR #276938 — Add `ctrlCmd+enter` accept for chat elicitation request
   - PR: https://github.com/microsoft/vscode/pull/276938
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/actions/chatElicitationActions.ts: +/*--------------------------------------------------------------------------------------------- + *  Copyright (c) Microsoft Corporation. All rights reserved. + *  Licensed under the MIT License. See
     - src/vs/workbench/contrib/chat/browser/chat.contribution.ts: +import { registerChatElicitationActions } from './actions/chatElicitationActions.js'; +registerChatElicitationActions();

163. Issue #259253 — Support for MCP resources with `https://` scheme (closed 2025-11-12T00:31:11Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! feature_request_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- Please search existing issues to avoid creating duplicates. --> <!-- Describe the feature you'd like. --> Currently, it looks like the only way for MCP servers to return images is by using `ResourceBlobContents`. However, this bloats up...
   - Issue: https://github.com/microsoft/vscode/issues/259253
   - Fix PR #276580 — Enable support for Http based MCP resources
   - PR: https://github.com/microsoft/vscode/pull/276580
   - Code excerpts:
     - src/vs/workbench/contrib/mcp/common/mcpResourceFilesystem.ts: +import { IWebContentExtractorService } from '../../../../platform/webContentExtractor/common/webContentExtractor.js'; +import { canLoadMcpNetworkResourceDirectly } from './mcpTypesUtils.js'; +		@IWeb
     - src/vs/workbench/contrib/mcp/common/mcpTypesUtils.ts: +import { IMcpServer, IMcpServerStartOpts, IMcpService, McpConnectionState, McpServerCacheState, McpServerTransportType } from './mcpTypes.js'; + + + +/** + * Validates whether the given HTTP or HTTPS

164. Issue #275275 — Add tooltip on chat terminal button (closed 2025-11-12T17:21:17Z)
   - Issue detail: Testing #274924 nit but I feel it would be useful to show a tooltip on this button that provides a hint what clicking it will do <img width="285" height="123" alt="Image" src="https://github.com/user-attachments/assets/ba160179-def2-4c61-aead-abdf2f298022" />
   - Issue: https://github.com/microsoft/vscode/issues/275275
   - Fix PR #276944 — add tooltip for chat entry
   - PR: https://github.com/microsoft/vscode/pull/276944
   - Code excerpts:
     - src/vs/workbench/contrib/terminal/browser/terminalTabsChatEntry.ts: +			this._entry.removeAttribute('title'); +		const tooltip = localize('terminal.tabs.chatEntryTooltip', "Show hidden chat terminals"); +		this._entry.setAttribute('title', tooltip);

165. Issue #267022 — High GPU Usage by WindowServer When Opening Projects in VS Code After macOS 26 Update (closed 2025-09-24T17:27:17Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/267022
   - Fix PR #267724 — Fix: Disable window shadows on macOS Tahoe to prevent GPU performance issues
   - PR: https://github.com/microsoft/vscode/pull/267724
   - Code excerpts:
     - src/vs/base/common/platform.ts: + +export function isTahoe(osVersion: string): boolean { +	return parseFloat(osVersion) === 25; +}
     - src/vs/platform/windows/electron-main/windows.ts: +import { release } from 'os'; +import { IProcessEnvironment, isLinux, isMacintosh, isTahoe, isWindows } from '../../../base/common/platform.js'; + +		// Mac OS 26.?.? has a `WindowServer` bug that ca

166. Issue #237782 — Cannot read properties of null (reading 'isDisposed') (closed 2025-08-08T03:06:11Z)
   - Issue detail: ```javascript TypeError: Cannot read properties of null (reading 'isDisposed') at QFe.update in src/vs/workbench/contrib/chat/common/codeBlockModelCollection.ts:155:17 ``` [Go to Errors Site](https://errors.code.visualstudio.com/card?ch=2569d71b0491afddb23e173ee6cc2eb284f1b0b9&bH=030af23d-7be3-0c49-d3eb-05d22678ac02)
   - Issue: https://github.com/microsoft/vscode/issues/237782
   - Fix PR #260445 — Fix strange NPE
   - PR: https://github.com/microsoft/vscode/pull/260445
   - Code excerpts:
     - src/vs/workbench/contrib/chat/common/codeBlockModelCollection.ts: +		if (!textModel || textModel.isDisposed()) { +			// Somehow we get an undefined textModel sometimes - #237782

167. Issue #274870 — store command output so it persists after the terminal is killed (closed 2025-11-12T15:34:56Z)
   - Issue detail: When terminal command is finished, we should serialize the command output in addition to the command URI so that we can toggle the show output action even when the terminal's long gone. We'll put those on `toolSpecificData` in `runInTerminalTool`. _Originally posted by @Tyriar in https://github.com/microsoft/vscode/pull/274417#discussion_r2483717854_
   - Issue: https://github.com/microsoft/vscode/issues/274870
   - Fix PR #276601 — store command and output so it can persist when the terminal is killed
   - PR: https://github.com/microsoft/vscode/pull/276601
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts: +import { URI } from '../../../../../../base/common/uri.js'; +	private _terminalCommandUri: URI | undefined; +	private _storedCommandId: string | undefined; +	private readonly _isSerializedInvocation:
     - src/vs/workbench/contrib/chat/common/chatService.ts: +	/** Serialized URI for the command that was executed in the terminal */ +	terminalCommandUri?: UriComponents; +	/** Serialized output of the executed command */ +	terminalCommandOutput?: { +		text: 

168. Issue #259057 — Chat participant contributed from `chatSessions` contribution shows up in the panel chat (closed 2025-07-31T22:24:06Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/259057
   - Fix PR #259085 — fix #259057
   - PR: https://github.com/microsoft/vscode/pull/259085
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatSessions.contribution.ts: +import { MarkdownString } from '../../../../base/common/htmlContent.js'; +const CODING_AGENT_DOCS = 'https://code.visualstudio.com/docs/copilot/copilot-coding-agent'; + +			locations: [ChatAgentLocat

169. Issue #258586 — Session is initializing... and Working... stuck at top of coding agent chat view (closed 2025-07-31T00:06:35Z)
   - Issue detail: Testing #258320 Repro: 1. Create a chat editor 2. Send some messages 3. Delegate to coding agent <img width="1043" height="862" alt="Image" src="https://github.com/user-attachments/assets/e44736df-73a1-4f4f-b57a-3dc517077d90" />
   - Issue: https://github.com/microsoft/vscode/issues/258586
   - Fix PR #258916 — Fix #258586.
   - PR: https://github.com/microsoft/vscode/pull/258916
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatWidget.ts: +		this.renderer.updateOptions({ restorable: false, editable: false, progressMessageAtBottomOfResponse: true }); +		this.renderer.updateOptions({ restorable: true, editable: true, progressMessageAtBot

170. Issue #277530 — nl command should be auto approved by default (closed 2025-11-14T21:59:24Z)
   - Issue: https://github.com/microsoft/vscode/issues/277530
   - Fix PR #277531 — Auto approve nl by default
   - PR: https://github.com/microsoft/vscode/pull/277531
   - Code excerpts:
     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/common/terminalChatAgentToolsConfiguration.ts: +			nl: true,
     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/test/electron-browser/runInTerminalTool.test.ts: +			'nl -ba path/to/file.txt',

171. Issue #277512 — Clean up new ITerminalChatService entries (closed 2025-11-14T21:30:11Z)
   - Issue detail: https://github.com/microsoft/vscode/blob/191c38830ed4c44cba1faec8d5e86b6bccf7980b/src/vs/workbench/contrib/terminal/browser/terminal.ts#L168-L174
   - Issue: https://github.com/microsoft/vscode/issues/277512
   - Fix PR #277529 — Simplify progress part APIs, add jsdoc
   - PR: https://github.com/microsoft/vscode/pull/277529
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts: +		this._register(this._terminalChatService.registerProgressPart(this)); +		this._terminalChatService.setFocusedProgressPart(this); +		this._terminalChatService.clearFocusedProgressPart(this); +		this
     - src/vs/workbench/contrib/chat/browser/chatTerminalOutputAccessibleView.ts: +		const part = terminalChatService.getFocusedProgressPart();

172. Issue #263017 — [BUG] preLaunchTask runs before confirmation when starting a concurrent debug session. (closed 2025-09-02T22:13:55Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/263017
   - Fix PR #263294 — Fix preLaunchTask running before concurrent session confirmation
   - PR: https://github.com/microsoft/vscode/pull/263294
   - Code excerpts:
     - src/vs/workbench/contrib/debug/browser/debugService.ts: + +				// Check for concurrent sessions before running preLaunchTask to avoid running the task if user cancels +				let userConfirmedConcurrentSession = false; +				if (options?.startedByUser && resol

173. Issue #276157 — Adopt isObject, isNumber and isString in terminal (closed 2025-11-14T19:38:21Z)
   - Issue: https://github.com/microsoft/vscode/issues/276157
   - Fix PR #277494 — Adopt is* functions in contrib/terminal*
   - PR: https://github.com/microsoft/vscode/pull/277494
   - Code excerpts:
     - src/vs/workbench/contrib/terminal/browser/baseTerminalBackend.ts: +import { isNumber, isObject } from '../../../../base/common/types.js'; +		'version' in obj && isNumber(obj.version) &&
     - src/vs/workbench/contrib/terminal/browser/terminal.ts: +import { isNumber, type SingleOrMany } from '../../../../base/common/types.js'; +export const isDetachedTerminalInstance = (t: ITerminalInstance | IDetachedTerminalInstance): t is IDetachedTerminalIn

174. Issue #265334 — Adopt `IChatEntitlementService` in `chatWidget.ts` (closed 2025-10-03T20:49:30Z)
   - Issue detail: Noticed how you rely on context keys to drive logic: https://github.com/microsoft/vscode/blob/fa6188bc91d2b0f16ce980b62f7fcbbfe100c1ff/src/vs/workbench/contrib/chat/browser/chatWidget.ts#L387 A better approach is to use `IChatEntitlementService` that has events for `entitlement` and `sentiment` changes: * `entitlement: ChatEntitlement.Available` maps to if the user can sign up for free *...
   - Issue: https://github.com/microsoft/vscode/issues/265334
   - Fix PR #265731 — Adopt IChatEntitlementService in chatWidget.ts to replace context key logic
   - PR: https://github.com/microsoft/vscode/pull/265731
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatWidget.ts: +import { ChatContextKeys } from '../common/chatContextKeys.js'; +import { ChatEntitlement, IChatEntitlementService } from '../../../services/chat/common/chatEntitlementService.js'; +	private shouldSh

175. Issue #258533 — Unsure what the difference is between the two options and why one of them is enabled (closed 2025-07-30T17:10:14Z)
   - Issue detail: Testing #258320 1. What is the difference between "Send" and "Send and Dispatch"? 2. Why is "Send and Dispatch" still enabled with a check mark when the coding agent request is still running? <img width="354" height="128" alt="Send and Send and Dispatch given as options in dropdown next to the stop button" src="https://github.com/user-attachments/assets/867ae0a2-3971-403d-8ae1-5c13e4061afb" />
   - Issue: https://github.com/microsoft/vscode/issues/258533
   - Fix PR #258842 — fix #258533
   - PR: https://github.com/microsoft/vscode/pull/258842
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/actions/chatExecuteActions.ts: +					when: ContextKeyExpr.and(precondition, ChatContextKeys.lockedToCodingAgent.negate()),

176. Issue #258691 — can send empty msg in PR chat (closed 2025-07-30T16:34:36Z)
   - Issue detail: Testing #258320 in the chat panel to talk with the coding agent about a PR you can press enter with no context (I checked and don't even have a random space) and the button allows you to send a message but it only says `@copilot` <img width="884" height="816" alt="Image" src="https://github.com/user-attachments/assets/5d2677f8-231b-4c57-a17f-ed9cb1e64c3d" />
   - Issue: https://github.com/microsoft/vscode/issues/258691
   - Fix PR #258829 — fix #258691
   - PR: https://github.com/microsoft/vscode/pull/258829
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatWidget.ts: +				if (!currentValue.length) { +					return; +				}

177. Issue #275789 — Chat terminals amount represents all visible and hidden terminals (closed 2025-11-10T15:21:25Z)
   - Issue detail: Repro: 1. Run ls 2. Run ls in a background terminal 3. Click the chat terminals button and show one, 🐛 the bottom button still says 2, it should show the count of hidden terminals <img width="1601" height="1395" alt="Image" src="https://github.com/user-attachments/assets/c5f53fc3-787b-4a57-8a78-01b6ccfc5fd5" />
   - Issue: https://github.com/microsoft/vscode/issues/275789
   - Fix PR #275907 — make show chat terminals action only apply to hidden ones
   - PR: https://github.com/microsoft/vscode/pull/275907
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/actions/chatAccessibilityHelp.ts: +		content.push(localize('chat.showHiddenTerminals', 'If there are any hidden chat terminals, you can view them by invoking the View Hidden Chat Terminals command{0}.', '<keybinding:workbench.action.t
     - src/vs/workbench/contrib/terminal/browser/terminalTabsChatEntry.ts: +			void this._commandService.executeCommand('workbench.action.terminal.chat.viewHiddenChatTerminals'); +				? localize('terminal.tabs.chatEntryLabelSingle', "{0} Hidden Terminal", chatTerminalCount) 

178. Issue #266354 — Chat status: Progress for chat sessions seems not perfectly aligned to text (closed 2025-09-17T15:51:12Z)
   - Issue detail: <img width="332" height="99" alt="Image" src="https://github.com/user-attachments/assets/b0bdc5d4-1e0d-4331-939e-8b4d615e2efa" />
   - Issue: https://github.com/microsoft/vscode/issues/266354
   - Fix PR #267218 — Chat status: Progress for chat sessions seems not perfectly aligned to text (fix #266354)
   - PR: https://github.com/microsoft/vscode/pull/267218
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatStatus.ts: +			const chatSessionsInProgressCount = this.chatSessionsService.getInProgress().reduce((total, item) => total + item.count, 0); +			// Sessions in progress +			else if (chatSessionsInProgressCount > 
     - src/vs/workbench/contrib/chat/browser/media/chatStatus.css: +	display: flex; +	align-items: center; +	gap: 3px;

179. Issue #274344 — Test advanced settings (closed 2025-11-04T21:54:37Z)
   - Issue detail: Refs: https://github.com/microsoft/vscode/issues/270142 - [x] anyOS @sbatten - [x] anyOS @hediet Complexity: 3 [Create Issue](https://github.com/microsoft/vscode/issues/new?template=blank&body=Testing+%23274344%0A%0A&assignees=sandy081) --- ## Testing ### 1. Test Advanced Settings Filter Visibility - Open Settings editor - Verify filter dropdown menu includes "Advanced" option - Verify...
   - Issue: https://github.com/microsoft/vscode/issues/274344
   - Fix PR #275526 — Make Stable, Preview, and Experimental filters mutually exclusive in Settings Editor
   - PR: https://github.com/microsoft/vscode/pull/275526
   - Code excerpts:
     - src/vs/workbench/contrib/preferences/browser/settingsSearchMenu.ts: +	private createMutuallyExclusiveToggleAction(id: string, label: string, tooltip: string, filter: string, excludeFilters: string[]): IAction { +		const isFilterEnabled = this.searchWidget.getValue().s

180. Issue #275033 — Chat view: Terminal commands rendered with wrong font (closed 2025-11-05T21:56:22Z)
   - Issue detail: Testing #274904 I have a font set: ```json "terminal.integrated.fontFamily": "FiraCode Nerd Font Mono" ``` The confirmation shows correctly it seems: <img width="480" height="400" alt="Image" src="https://github.com/user-attachments/assets/8f1dc40e-ca9f-4c79-9f3d-ced5ff704018" /> But then the font changes: <img width="514" height="353" alt="Image" src="https://github.com/user-...
   - Issue: https://github.com/microsoft/vscode/issues/275033
   - Fix PR #275686 — Use correct fallback font in md code blocks
   - PR: https://github.com/microsoft/vscode/pull/275686
   - Code excerpts:
     - src/vs/editor/browser/widget/markdownRenderer/browser/editorMarkdownCodeBlockRenderer.ts: +import { BareFontInfo } from '../../../../common/config/fontInfo.js'; +import { createBareFontInfoFromRawSettings } from '../../../../common/config/fontInfoFromSettings.js'; +import { ICodeEditor, is

181. Issue #275651 — Setting `accessibility.openChatEditedFiles` to `false` does not prevent new files from opening (closed 2025-11-05T21:27:33Z)
   - Issue detail: Steps to Reproduce: 1. ask AI to create a new file 2. it opens 🐛 This is because of: https://github.com/microsoft/vscode/blob/750eab4d3f32a8c3afca4c7c77d60df0e9015ec3/src/vs/workbench/contrib/chat/browser/chatEditing/chatEditingSession.ts#L910 //cc @roblourens @pierceboggan @digitarald
   - Issue: https://github.com/microsoft/vscode/issues/275651
   - Fix PR #275681 — only open chat created editor if `accessibility.openChatEditedFiles === true`
   - PR: https://github.com/microsoft/vscode/pull/275681
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatEditing/chatEditingSession.ts: +import { IConfigurationService } from '../../../../../platform/configuration/common/configuration.js'; +		@IConfigurationService private readonly configurationService: IConfigurationService, +			if (

182. Issue #275202 — `yo code` input isn't detected, looks like terminal hangs without focus button (closed 2025-11-11T19:36:32Z)
   - Issue detail: Notice there's no focus button, also no input required dialog: <img width="616" height="398" alt="Image" src="https://github.com/user-attachments/assets/6e1d3dc3-0aae-48af-a84e-758e28964871" /> State of the terminal (I showed it via the focus button for the previous terminal tool call): <img width="1619" height="368" alt="Image" src="https://github.com/user-...
   - Issue: https://github.com/microsoft/vscode/issues/275202
   - Fix PR #276572 — Detect questions, request for password in terminal output, provide more lines
   - PR: https://github.com/microsoft/vscode/pull/276572
   - Code excerpts:
     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/tools/monitoring/outputMonitor.ts: +							this._state = OutputMonitorState.PollingForIdle; +		const lastLines = execution.getOutput(this._lastPromptMarker).trimEnd().split('\n').slice(-15).join('\n'); +			9. Output: "Password:" +				R

183. Issue #255699 — VS Code Terminal Stack Overflow (-1073741571) Triggered by fnm PATH Injection (closed 2025-09-04T22:33:22Z)
   - Issue detail: 🐞 Bug Report: PowerShell 7 Crashes in Integrated Terminal with Exit Code -1073741571 When `fnm` Is Active VS Code Version: 1.102.0 PowerShell Version: 7.5.2 Node Manager: fnm OS: Windows 10/11 Shell: PowerShell 7 (pwsh.exe) Error Message: The terminal process "C:\Program Files\PowerShell\7\pwsh.exe" terminated with exit code: -1073741571 💥 Issue Summary When launching PowerShell 7 in VS Code’s...
   - Issue: https://github.com/microsoft/vscode/issues/255699
   - Fix PR #263452 — Fix SI double install issue in pwsh
   - PR: https://github.com/microsoft/vscode/pull/263452
   - Code excerpts:
     - src/vs/workbench/contrib/terminal/common/scripts/shellIntegration.ps1: +if ($Global:__VSCodeState.OriginalPrompt -ne $null) {

184. Issue #274960 — attach to chat sometimes doesn't work (closed 2025-11-04T10:16:22Z)
   - Issue detail: because sometimes there's no last focused widget
   - Issue: https://github.com/microsoft/vscode/issues/274960
   - Fix PR #274963 — if no focused chat widget, get the first one for chat
   - PR: https://github.com/microsoft/vscode/pull/274963
   - Code excerpts:
     - src/vs/workbench/contrib/terminal/browser/xterm/decorationAddon.ts: +				const widget = this._chatWidgetService.lastFocusedWidget ?? this._chatWidgetService.getWidgetsByLocations(ChatAgentLocation.Chat)?.find(w => w.attachmentCapabilities.supportsTerminalAttachments);

185. Issue #271500 — Incorrect role assigned to "More Options" button as link: A11y_Visual Studio Code Client_Name (closed 2025-11-08T05:52:25Z)
   - Issue detail: ### GitHub Tags: #A11yTCS; #A11ySev3; #Visual Studio Code Client; #BM_Visual Studio Code Client_Win32_JULY2024; #DesktopApp; #Win32; #Benchmark;#Name Role Value;#MAS4.1.2; ### Environment and OS details: Application Name: Visual Studio Code Version: 1.106.0-insider (user setup) OS build :26100.4770 ### Reproduction Steps: Open Visual studio code insider. Tab till more options button. Observed...
   - Issue: https://github.com/microsoft/vscode/issues/271500
   - Fix PR #276186 — add proper role to dropdown action
   - PR: https://github.com/microsoft/vscode/pull/276186
   - Code excerpts:
     - src/vs/base/browser/ui/dropdown/dropdownActionViewItem.ts: +			this.setAriaLabelAttributes(this.element);

186. Issue #273108 — Performance: UriIdentityService uses non-optimal caching strategy (closed 2025-11-12T14:37:46Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/273108
   - Fix PR #273111 — Improve performance of UriIdentityService (#273108)
   - PR: https://github.com/microsoft/vscode/pull/273111
   - Code excerpts:
     - src/vs/platform/uriIdentity/common/uriIdentityService.ts: +import { quickSelect } from '../../../base/common/arrays.js'; +	private readonly _canonicalUris: Map<string, Entry>; +			const oldIgnorePathCasingValue = schemeIgnoresPathCasingCache.get(e.scheme); +
     - src/vs/platform/uriIdentity/test/common/uriIdentityService.test.ts: +	test('[perf] clears cache when overflown with respect to access time', () => { +		const CACHE_SIZE = 2 ** 16; +		const getUri = (i: number) => URI.parse(`foo://bar/${i}`); + +		const FIRST = 0; +		c

187. Issue #272404 — Disposable leak: `ChatService.loadSessionForResource` (closed 2025-11-03T18:39:52Z)
   - Issue detail: ``` LEAKED DISPOSABLE] Error: CREATED via: at GCBasedDisposableTracker.trackDisposable (vscode-file://vscode-app/Users/bpasero/Development/Microsoft/vscode/out/vs/base/common/lifecycle.js:28:23) at trackDisposable (vscode-file://vscode-app/Users/bpasero/Development/Microsoft/vscode/out/vs/base/common/lifecycle.js:202:24) at new DisposableStore (vscode-file://vscode-...
   - Issue: https://github.com/microsoft/vscode/issues/272404
   - Fix PR #274831 — Make sure to dispose of provided session listeners
   - PR: https://github.com/microsoft/vscode/pull/274831
   - Code excerpts:
     - src/vs/workbench/contrib/chat/common/chatServiceImpl.ts: +	private readonly _contentProviderSessionModels = this._register(new DisposableResourceMap<{ readonly model: IChatModel } & IDisposable>()); +		this._contentProviderSessionModels.set(chatSessionResou

188. Issue #276094 — Chat history: Old chat sessions disappear and cannot be resumed in the new version (closed 2025-11-11T15:08:18Z)
   - Issue detail: - Create a few chat sessions in 1.105. - Install 1.106 and 0.33 candidates. - Click history toolbar item in chat panel. <img width="39" height="43" alt="Image" src="https://github.com/user-attachments/assets/a2ba6f74-bbc9-4d26-bfb4-7209c1a1e458" /> - Click history entry in QuickPick. - Observed: Nothing happens. 🐛 - Click history toolbar item again. - Observed: The entry disappeared. 🐛 The...
   - Issue: https://github.com/microsoft/vscode/issues/276094
   - Fix PR #276613 — Ignore obsolete chat content part type
   - PR: https://github.com/microsoft/vscode/pull/276613
   - Code excerpts:
     - src/vs/workbench/contrib/chat/common/chatModel.ts: +				case 'mcpServersInteractionRequired' as string: // obsolete part, ignore

189. Issue #274455 — Editing a comment freezes VS Code (closed 2025-11-03T10:16:31Z)
   - Issue detail: Editing a comment from a PR review crashes VS Code Version: 1.106.0-insider (user setup) Commit: e637e2ef735545f15caaeb95cfa6c5998dab8124 Date: 2025-10-31T05:02:33.136Z Electron: 37.7.0 ElectronBuildId: 12597478 Chromium: 138.0.7204.251 Node.js: 22.20.0 V8: 13.8.258.32-electron.0 OS: Windows_NT x64 10.0.26200 The comment I was trying to edit:...
   - Issue: https://github.com/microsoft/vscode/issues/274455
   - Fix PR #274708 — Editing a comment freezes VS Code
   - PR: https://github.com/microsoft/vscode/pull/274708
   - Code excerpts:
     - src/vs/workbench/contrib/comments/browser/commentThreadBody.ts: +	private _containerClientArea: dom.Dimension | null = null; +		if ((dimensions.height === 0 && dimensions.width === 0) || (this._containerClientArea && this._containerClientArea.height === dimensions

190. Issue #268450 — Command `Chat: Learn How to Hide AI Features` is missing from Command Palette (closed 2025-10-22T11:54:52Z)
   - Issue detail: Type: <b>Bug</b> Release Notes for 1.104 have a section titled "Hide and disable GitHub Copilot AI features" https://code.visualstudio.com/updates/v1_104#_hide-and-disable-github-copilot-ai-features which includes this sentence: > The command to "Hide AI Features" was renamed to reflect this change and will now reveal this new setting in the settings editor. But it doesn't name the command, nor...
   - Issue: https://github.com/microsoft/vscode/issues/268450
   - Fix PR #268462 — Show the `Learn How to Hide AI Features` in more situations (fix #268450)
   - PR: https://github.com/microsoft/vscode/pull/268462
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatSetup.ts: +					precondition: ChatContextKeys.Setup.hidden.negate(),

191. Issue #276548 — runSubagent creates recursive subagents (closed 2025-11-10T22:24:52Z)
   - Issue detail: The runSubagent tool is not filtered out when running a subagent, and this scenario doesn't work well, so it can create recursive subagents forever. The Todo tool also needs to be disabled.
   - Issue: https://github.com/microsoft/vscode/issues/276548
   - Fix PR #276552 — Filter subagent and todo tools from subagent requests
   - PR: https://github.com/microsoft/vscode/pull/276552
   - Code excerpts:
     - src/vs/workbench/contrib/chat/common/tools/runSubagentTool.ts: +import { ManageTodoListToolToolId } from './manageTodoListTool.js'; +			if (modeTools) { +				modeTools[RunSubagentToolId] = false; +				modeTools[ManageTodoListToolToolId] = false; +			} +

192. Issue #275351 — Chat context custom hover blocks chat list view scrolling (closed 2025-11-05T15:53:19Z)
   - Issue detail: Testing #274928 <img width="548" height="493" alt="Image" src="https://github.com/user-attachments/assets/c5348a71-867f-45f0-9f6e-3255fa08d862" /> - Move cursor into the hover widget of the terminal chat context - Scroll with trackpad: no op 🐛
   - Issue: https://github.com/microsoft/vscode/issues/275351
   - Fix PR #275590 — Truncate terminal attachment hover contents
   - PR: https://github.com/microsoft/vscode/pull/275590
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatAttachmentWidgets.ts: +const enum TerminalConstants { +	MaxAttachmentOutputLineCount = 5, +	MaxAttachmentOutputLineLength = 80, +} +		const outputTitle = dom.$('div', {}, localize('chat.terminalCommandHoverOutputTitle', "O

193. Issue #274311 — Focus terminal button doesn't work after reloading window (closed 2025-10-31T21:48:27Z)
   - Issue detail: Repro: 1. `run ls` in chat 2. Expand and click focus terminal, the command is revealed 3. Reload the window 4. Click focus terminal, 🐛 nothing happens despite the terminal being visible <img width="1037" height="840" alt="Image" src="https://github.com/user-attachments/assets/125138da-4c07-4581-a5ed-56e58fdc2943" />
   - Issue: https://github.com/microsoft/vscode/issues/274311
   - Fix PR #274417 — persist command in pty service, refactor how commands are restored on window reload for inline chat terminal
   - PR: https://github.com/microsoft/vscode/pull/274417
   - Code excerpts:
     - src/vs/platform/terminal/common/capabilities/capabilities.ts: +	/** +	 * Sets the command ID to use for the next command that starts. +	 * This allows pre-assigning an ID before the shell sends the command start sequence, +	 * which is useful for linking command
     - src/vs/platform/terminal/common/capabilities/commandDetection/terminalCommand.ts: +	id: string | undefined; +	id: string | undefined; +		this.id = id;

194. Issue #265324 — Multiple MCP sampling dialogs shown for concurrent sampling requests (closed 2025-09-08T16:52:11Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/265324
   - Fix PR #265698 — mcp: fix multiple sampling dialogs shown for concurrent sampling requests
   - PR: https://github.com/microsoft/vscode/pull/265698
   - Code excerpts:
     - src/vs/workbench/contrib/mcp/common/mcpSamplingService.ts: +import { Sequencer } from '../../../../base/common/async.js'; +	private readonly _modelSequencer = new Sequencer(); + +		const model = await this._modelSequencer.queue(() => this._getMatchingModel(op

195. Issue #254011 — Installing mcp server is stuck on "Installing" (closed 2025-07-25T12:36:48Z)
   - Issue detail: - Find an mcp server - Click Install - It says "installing" forever but _does_ install the server I don't see any interesting errors anywhere. The server is installed but I was waiting on the UI <img width="505" height="387" alt="Image" src="https://github.com/user-attachments/assets/305b43f4-2549-492c-8e35-a28c96b27c4c" />
   - Issue: https://github.com/microsoft/vscode/issues/254011
   - Fix PR #257821 — fix #254011
   - PR: https://github.com/microsoft/vscode/pull/257821
   - Code excerpts:
     - src/vs/workbench/contrib/mcp/browser/mcpWorkbenchService.ts: +				const local = this.local.find(e => e.name === name && e.local?.scope !== LocalMcpServerScope.Workspace) +					?? this.instantiationService.createInstance(McpWorkbenchServer, e => this.getInstallS

196. Issue #275555 — Terminal Completion API: No spacing between label and detail (closed 2025-11-07T17:10:29Z)
   - Issue detail: Testing #274921 ```ts provideTerminalCompletions(terminal: vscode.Terminal, context: vscode.TerminalCompletionContext, token: vscode.CancellationToken): vscode.ProviderResult<vscode.TerminalCompletionItem[] | vscode.TerminalCompletionList<vscode.TerminalCompletionItem>> { return new vscode.TerminalCompletionList([ new vscode.TerminalCompletionItem({ label: "HELLO", detail: "What about hello",...
   - Issue: https://github.com/microsoft/vscode/issues/275555
   - Fix PR #275588 — add space if needed before label detail 
   - PR: https://github.com/microsoft/vscode/pull/275588
   - Code excerpts:
     - src/vs/workbench/services/suggest/browser/simpleSuggestWidgetRenderer.ts: +			const labelDetail = stripNewLines(completion.label.detail || ''); +			data.parametersLabel.textContent = normalizeLabelDetail(labelDetail); + +const LEADING_PUNCTUATION_OR_SPACE = /^[\s()[\]{}<>"'

197. Issue #265988 — Copilot Chat uses Azure MCP Server despite extension being disabled (closed 2025-10-09T23:34:41Z)
   - Issue detail: I've got the Azure MCP Server VSCode extension installed but disabled. I also have no additional MCP Servers installed. After submitting a prompt to GitHub Copilot Chat I see that it's using the Azure MCP Server despite it being disabled. <img width="3638" height="3054" alt="Image" src="https://github.com/user-attachments/assets/ec5e5ab2-2b0c-481a-a2a9-859b67c74609" /> VSCode: Version: 1.103.2...
   - Issue: https://github.com/microsoft/vscode/issues/265988
   - Fix PR #270476 — Refreshing cached MCP servers when the extension MCP's are disabled. 
   - PR: https://github.com/microsoft/vscode/pull/270476
   - Code excerpts:
     - src/vs/workbench/contrib/mcp/common/discovery/extensionMcpDiscovery.ts: +import { ExtensionPointUserDelta, IExtensionPointUser } from '../../../../services/extensions/common/extensionsRegistry.js'; +	Delete +	private _extensionCollections?: DisposableMap<string>; +				if 
     - src/vs/workbench/contrib/mcp/common/mcpRegistry.ts: +				this._collections.set(currentCollections.filter(c => c.id !== collection.id), undefined);

198. Issue #260281 — Clicking on a change pill should preserve focus in chat (closed 2025-10-08T10:10:23Z)
   - Issue detail: Steps to Reproduce: 1. have chat output with change pills 2. click on a pill => notice how focus immediately moves into the editor Rather it should focus the pill but keep focus. <img width="327" height="350" alt="Image" src="https://github.com/user-attachments/assets/49595c00-a0ad-44f8-a254-a5eb5e815f3a" /> In addition: * double click should move focus * keyboard enter/space should move focus...
   - Issue: https://github.com/microsoft/vscode/issues/260281
   - Fix PR #270341 — Clicking on a change pill should preserve focus in chat (fix #260281)
   - PR: https://github.com/microsoft/vscode/pull/270341
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/chatMarkdownContentPart.ts: +import '../media/chatCodeBlockPill.css'; +import './media/chatMarkdownPart.css'; +import { IEditorService, SIDE_GROUP } from '../../../../services/editor/common/editorService.js'; +import { StandardK
     - src/vs/workbench/contrib/chat/browser/chatEditing/chatEditingActions.ts: +			const editor = await editorService.openEditor({ resource: snapshot, label: localize('chatEditing.snapshot', '{0} (Snapshot)', basename(context.uri)), options: { activation: EditorActivation.ACTIVA

199. Issue #275064 — Handoff Example causes squiggles to show (closed 2025-11-04T10:52:13Z)
   - Issue detail: Testing #274957 I accept the handoffs example and I got squiggles: <img width="1079" height="193" alt="Image" src="https://github.com/user-attachments/assets/34f201d1-ef42-4ea2-9191-82c6b8596ca4" />
   - Issue: https://github.com/microsoft/vscode/issues/275064
   - Fix PR #275072 — prompt files: set editor.insertSpaces: true
   - PR: https://github.com/microsoft/vscode/pull/275072
   - Code excerpts:
     - extensions/prompt-basics/package.json: +        "editor.insertSpaces": true, +        "editor.tabSize": 2, +        "editor.autoIndent": "advanced", +        "editor.insertSpaces": true, +        "editor.tabSize": 2, +        "editor.autoI

200. Issue #263533 — Perf: startup regression in main bundle (closed 2025-08-29T07:52:52Z)
   - Issue detail: Our perf bots show a sizeable increase in startup time to load the main bundle: <img width="891" height="547" alt="Image" src="https://github.com/user-attachments/assets/ae906367-4f80-41dd-b95e-99f6ca2a0659" /> This is the time from `performance.timeOrigin` until the very first line of code executes in `main.ts`:...
   - Issue: https://github.com/microsoft/vscode/issues/263533
   - Fix PR #263975 — Perf: startup regression in main bundle (fix #263533)
   - PR: https://github.com/microsoft/vscode/pull/263975
   - Code excerpts:
     - src/vs/base/parts/ipc/node/ipc.net.ts: +import type * as http from 'http'; +export function upgradeToISocket(req: http.IncomingMessage, socket: Socket, { +	const hash = createHash('sha1');// CodeQL [SM04514] SHA1 must be used here to respe
     - src/vs/platform/debug/electron-main/extensionHostDebugIpc.ts: +	private async openCdpServer(ident: string, onSocket: (socket: ISocket) => void) { +		const { createServer } = await import('http'); // Lazy due to https://github.com/microsoft/vscode/issues/263533 +

201. Issue #274333 — Auto-expand terminal commands with a non-zero (and non-undefined) exit code (closed 2025-11-03T20:06:35Z)
   - Issue detail: This would solve a big part of the feedback with the new output location. There's a somewhat conflicting effort we'll explore in November https://github.com/microsoft/vscode/issues/273444, but I think for now we should auto expand and see if it works with that new design too.
   - Issue: https://github.com/microsoft/vscode/issues/274333
   - Fix PR #274442 — reveal terminal output if command failed
   - PR: https://github.com/microsoft/vscode/pull/274442
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts: +			if (command.exitCode) { +				this._toggleOutput(true); +			}

202. Issue #275073 — Terminal tool: can expand when there is no output (closed 2025-11-05T21:48:01Z)
   - Issue detail: Testing #274909 <img width="641" height="568" alt="Image" src="https://github.com/user-attachments/assets/60b10b7c-b09b-41b1-9149-3cdd60c68ade" /> In this case there was no output, but I can still expand it.
   - Issue: https://github.com/microsoft/vscode/issues/275073
   - Fix PR #275687 — provide info message when no terminal output 
   - PR: https://github.com/microsoft/vscode/pull/275687
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatContentParts/media/chatTerminalToolProgressPart.css: +.chat-terminal-output-empty { +	font-style: italic; +	color: var(--vscode-descriptionForeground); +	line-height: normal; +} +
     - src/vs/workbench/contrib/chat/browser/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts: +		if (theme && !content.classList.contains('chat-terminal-output-content-empty')) { +		if (result.text.trim() === '') { +			container.classList.add('chat-terminal-output-content-empty'); +			const em

203. Issue #257612 — Nothing happens when downloading specific version of VSIX for all platforms (closed 2025-07-24T13:46:06Z)
   - Issue detail: Steps to Reproduce: 1. Open Extensions view and look for `ms-vscode.cpptools` extension 2. Right click on that extension and select **Download Specific Version of VSIX** action 3. Select the latest version 4. Select for all platforms 🐛 Nothing happens
   - Issue: https://github.com/microsoft/vscode/issues/257612
   - Fix PR #257659 — fix #257612
   - PR: https://github.com/microsoft/vscode/pull/257659
   - Code excerpts:
     - src/vs/platform/extensionManagement/common/extensionGalleryService.ts: +		{ targetPlatform, compatible, productVersion, version }: Omit<ExtensionVersionCriteria, 'targetPlatform'> & { targetPlatform: TargetPlatform | undefined }, +		if (targetPlatform && !isTargetPlatfor
     - src/vs/platform/extensionManagement/common/extensionManagement.ts: +	targetPlatforms: TargetPlatform[];

204. Issue #260539 — "Copilot Edits" wording leaking into agent mode? (closed 2025-08-18T22:55:47Z)
   - Issue detail: Click undo on working set: <img width="465" height="211" alt="Image" src="https://github.com/user-attachments/assets/38219228-70f5-4fd7-8344-ab6d5336d992" /> Mentions "Copilot Edits" but probably shouldn't: <img width="509" height="133" alt="Image" src="https://github.com/user-attachments/assets/6965892a-9a9c-4fc5-a2da-006f693cb2df" />
   - Issue: https://github.com/microsoft/vscode/issues/260539
   - Fix PR #262222 — Fix "Copilot Edits" leftover in message
   - PR: https://github.com/microsoft/vscode/pull/262222
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/chatEditing/chatEditingActions.ts: +				? localize('chat.editing.discardAll.confirmation.oneFile', "This will undo changes made in {0}. Do you want to proceed?", basename(entries[0].modifiedURI)) +				: localize('chat.editing.discardAl

205. Issue #274482 — Regression: Heap increase (closed 2025-11-01T14:52:21Z)
   - Issue detail: <img width="577" height="483" alt="Image" src="https://github.com/user-attachments/assets/2a7e963c-b323-4d7b-84cf-dd1cdbf3c621" /> Heap usage increased significantly between: * Good: 2025-10-23 `2e77c17d50b9e2bc71c5e41b9b0c33ab42f32a83` * Bad: 2025-10-23 `f1bd9ba91544a129a5ad74444e51e53293892310` List of commits:...
   - Issue: https://github.com/microsoft/vscode/issues/274482
   - Fix PR #274506 — Lazily init tree sitter parser
   - PR: https://github.com/microsoft/vscode/pull/274506
   - Code excerpts:
     - src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/treeSitterCommandParser.ts: +import { Lazy } from '../../../../../base/common/lazy.js'; +	private readonly _parser: Lazy<Promise<Parser>>; +		this._parser = new Lazy(() => this._treeSitterLibraryService.getParserClass().then(Par

206. Issue #274496 — Make command re-writing pluggable (closed 2025-11-01T14:59:40Z)
   - Issue detail: This file should be split into multiple: https://github.com/microsoft/vscode/blob/730feccc7e7d20245b7776f747959ec9c3a1174d/src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/commandSimplifier.ts
   - Issue: https://github.com/microsoft/vscode/issues/274496
   - Fix PR #274502 — Make command re-writing pluggable 
   - PR: https://github.com/microsoft/vscode/pull/274502
   - Code excerpts:
     - src/vs/base/common/async.ts: +/** + * Wrap a type in an optional promise. This can be useful to avoid the runtime + * overhead of creating a promise. + */ +export type MaybePromise<T> = Promise<T> | T; +

207. Issue #253521 — File pill rendering (closed 2025-10-28T18:11:41Z)
   - Issue detail: Testing #253074 I see repeatedly file pills that don't show any decorations about how many lines were changed: <img width="2152" alt="Image" src="https://github.com/user-attachments/assets/085c5cdc-cf87-4f1b-9337-574aeeab2893" /> Instant apply interaction: [f87a476b.copilotmd.txt](https://github.com/user-attachments/files/21008597/f87a476b.copilotmd.txt)
   - Issue: https://github.com/microsoft/vscode/issues/253521
   - Fix PR #273662 — refactor: edit operations timeline
   - PR: https://github.com/microsoft/vscode/pull/273662
   - Code excerpts:
     - src/vs/base/common/async.ts: +	peek(key: TKey): Promise<unknown> | undefined { +		return this.promiseMap.get(key) || undefined; +	} +

208. Issue #258316 — 2 checkmarks in model picker when selecting BYOK 4.1 (closed 2025-07-30T18:13:02Z)
   - Issue detail: <img width="679" height="720" alt="Image" src="https://github.com/user-attachments/assets/4a93247d-9d1e-4695-ad90-5e97a5aa67c5" />
   - Issue: https://github.com/microsoft/vscode/issues/258316
   - Fix PR #258859 — Fix double checkmark
   - PR: https://github.com/microsoft/vscode/pull/258859
   - Code excerpts:
     - src/vs/workbench/contrib/chat/browser/modelPicker/modelPickerActionItem.ts: +					checked: model.identifier === delegate.getCurrentModel()?.identifier,

209. Issue #257420 — Duplicate Workspace MCP servers are shown when an MCP server with same name is installed in User and Workspace (closed 2025-07-23T12:45:01Z)
   - Issue detail: Steps: - Install GitHub MCP Server in User MCP - From https://code.visualstudio.com/mcp page - Open the user mcp.json - F1 > MCP: Open User Configuration - Copy the github server config and create a mcp.json file in the workspace under `.vscode` folder and add it there with same name - Go to installed MCP Servers view and refresh 🐛 Duplicated workspace MCP servers are shown Duplicated MCP...
   - Issue: https://github.com/microsoft/vscode/issues/257420
   - Fix PR #257445 — fix #257420
   - PR: https://github.com/microsoft/vscode/pull/257445
   - Code excerpts:
     - src/vs/workbench/contrib/mcp/browser/mcpWorkbenchService.ts: +import { ILogService } from '../../../../platform/log/common/log.js'; +import { IGalleryMcpServer, IMcpGalleryService, IQueryOptions, IInstallableMcpServer, IMcpServerManifest, ILocalMcpServer } from
     - src/vs/workbench/contrib/mcp/common/discovery/installedMcpServersDiscovery.ts: +import { McpServerDefinition, McpServerTransportType, IMcpWorkbenchService, IMcpConfigPath } from '../mcpTypes.js'; +import { IWorkbenchLocalMcpServer } from '../../../../services/mcp/common/mcpWorkb

210. Issue #216858 — Memory leak in gettingStarted (closed 2025-10-27T21:40:00Z)
   - Issue detail: <!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ --> <!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ --> <!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions --> <!-- 🔎 Search existing issues to avoid creating duplicates. --> <!-- 🧪 Test using the latest Insiders build to see if your...
   - Issue: https://github.com/microsoft/vscode/issues/216858
   - Fix PR #216876 — fix: memory leak in gettingStarted
   - PR: https://github.com/microsoft/vscode/pull/216876
   - Code excerpts:
     - src/vs/workbench/contrib/welcomeGettingStarted/browser/gettingStarted.ts: +			this.mediaDisposables.clear();

211. Issue #275568 — Add git bash icon to git bash terminal profile (closed 2025-11-07T19:00:35Z)
   - Issue: https://github.com/microsoft/vscode/issues/275568
   - Fix PR #275571 — Add git bash icon to git bash profile
   - PR: https://github.com/microsoft/vscode/pull/275571
   - Code excerpts:
     - src/vs/platform/terminal/common/terminalPlatformConfiguration.ts: +import { Codicon, getAllCodicons } from '../../../base/common/codicons.js'; +					icon: Codicon.terminalPowershell.id, +					icon: Codicon.terminalCmd, +					source: 'Git Bash', +					icon: Codicon.t
     - src/vs/platform/terminal/node/terminalProfiles.ts: +			icon: Codicon.terminalGitBash,
