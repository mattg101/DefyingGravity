# Pull Request: JSON Bridge Protocol Implementation
**PR ID:** PR-002
**Branch:** `dev`
**Target:** `main`
**Author:** Developer (Antigravity)

## 1. Description
Implements the core communication layer between the SolidWorks C# Add-in and the React/TypeScript frontend. This protocol uses a standardized JSON envelope to enable bi-directional, asynchronous messaging with correlation tracking.

- **Standardized Envelope**: `{"type": string, "correlationId": string, "payload": object, "error": string}`.
- **Handshake Support**: Implements `CONNECTION_STATUS`, `PING`/`PONG`, and `UI_READY` for reliable startup.
- **Pascal to Camel Case Translation**: Uses `[JsonProperty]` to ensure C# PascalCase properties are serialized to TypeScript camelCase.
- **Build Resilience**: Integrated `Microsoft.Net.Compilers` to support modern C# 7 syntax in restricted MSBuild 4.0 environments.

## 2. Changes

### [SolidLink.Addin] (C# Backend)
- **[MODIFY] [BridgeMessage.cs](file:///c:/Users/mattg/OneDrive/Documents/Projects/dev/antigravity_dev/SolidLink/SolidLink.Addin/Bridge/BridgeMessage.cs)**: Standardized envelope with attributes.
- **[MODIFY] [MessageBridge.cs](file:///c:/Users/mattg/OneDrive/Documents/Projects/dev/antigravity_dev/SolidLink/SolidLink.Addin/Bridge/MessageBridge.cs)**: Handlers for `PING`, `UI_READY`.
- **[MODIFY] [SolidLinkWindow.xaml.cs](file:///c:/Users/mattg/OneDrive/Documents/Projects/dev/antigravity_dev/SolidLink/SolidLink.Addin/UI/SolidLinkWindow.xaml.cs)**: Handshake trigger on navigation.
- **[MODIFY] [packages.config](file:///c:/Users/mattg/OneDrive/Documents/Projects/dev/antigravity_dev/SolidLink/SolidLink.Addin/packages.config)**: Added `Microsoft.Net.Compilers`.

### [SolidLink.UI] (TypeScript Frontend)
- **[NEW] [bridge/types.ts](file:///c:/Users/mattg/OneDrive/Documents/Projects/dev/antigravity_dev/SolidLink/SolidLink.UI/src/bridge/types.ts)**: Shared type definitions.
- **[NEW] [bridge/bridgeClient.ts](file:///c:/Users/mattg/OneDrive/Documents/Projects/dev/antigravity_dev/SolidLink/SolidLink.UI/src/bridge/bridgeClient.ts)**: Singleton communication client.
- **[NEW] [bridge/useBridge.ts](file:///c:/Users/mattg/OneDrive/Documents/Projects/dev/antigravity_dev/SolidLink/SolidLink.UI/src/bridge/useBridge.ts)**: React subscription hook.
- **[MODIFY] [App.tsx](file:///c:/Users/mattg/OneDrive/Documents/Projects/dev/antigravity_dev/SolidLink/SolidLink.UI/src/App.tsx)**: Integrated status indicators and handshake logic.

## 3. Verification Evidence
- **Build (TypeScript)**: `npm run build` passes with 0 errors.
- **Build (C#)**: Compiled successfully using Roslyn-in-NuGet path trick.
- **Runtime**: Verified in SolidWorks 2026. Handshake completes with green "Connected" status.
- **Visuals**: See [walkthrough.md](file:///c:/Users/mattg/.gemini/antigravity/brain/66fc75a8-c53d-478c-8028-6d2c88b31b74/walkthrough.md).

## 4. Compliance
- [x] **Strict Typing**: No `any` or `dynamic`.
- [x] **Error Handling**: Wrapped cross-process calls in `try/catch`.
- [x] **Aesthetics**: Follows modern dark-mode aesthetic.
- [x] **SOP Loop**: Added "Roslyn Path Trick" to `project_context.md`.
- [x] **Property Casing**: Enforced camelCase for bridge compatibility.
