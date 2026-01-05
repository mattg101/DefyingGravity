# Pull Request: SolidLink Bootstrap
**PR ID:** PR-001
**Branch:** `dev`
**Target:** `main`
**Author:** Developer (Antigravity)

## 1. Description
Bootstraps the `SolidLink` project (SolidWorks Add-in + React Frontend).
- Implements `ISwAddin` in C# (.NET Framework 4.8).
- Implements `CommandManager` toolbar for UI entry point.
- Embeds `WebView2` control for hosting the React UI.
- Scaffolds `SolidLink.UI` using Vite + React + TypeScript.
- Implements manual `packages.config` based NuGet restore for legacy MSBuild compatibility.

## 2. Changes
- [NEW] `SolidLink.sln`
- [NEW] `SolidLink.Addin/` (C# Backend)
- [NEW] `SolidLink.UI/` (React Frontend)
- [NEW] `scripts/register.ps1` (Registration)

## 3. Verification Evidence
- **Build Success:** Verified backend compiles in `Debug|x64`.
- **Registration:** Verified add-in works in SolidWorks 2026.
- **UI Launch:** Verified "Open SolidLink" button opens WebView2 window.
- **Frontend Load:** Verified React app loads ("No Model Loaded" screen).
- **Screenshots:** See `walkthrough.md`.

## 4. Compliance
- [x] Strict Ref/Out in COM Interop.
- [x] No `dynamic` usage.
- [x] Error handling in `ConnectToSW` and `OpenSolidLink`.
- [x] WebView2 user data folder set to `%LOCALAPPDATA%` (Access Denied fix).
