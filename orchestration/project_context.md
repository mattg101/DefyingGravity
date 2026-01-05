# Project Context: SW2URDF
> [!IMPORTANT]
> **GROUND TRUTH:** This file is the primary technical context for all agents. Consult this file BEFORE searching the file tree or assuming any architectural patterns.

This file defines the **Technical Context** for the generic SOPs. All agents must read this to understand the concrete inputs/outputs of their general roles.

## Technology Stack
-   **Core Language:** C# .NET Framework 4.8 (Backend) / TypeScript (Frontend).
-   **UI:** React (Vite) hosted in WebView2.
-   **Host Application:** Solidworks (Plugin/Add-in Development).
-   **API:** Solidworks API (COM Interop) <-> JSON Bridge <-> React.
-   **Build System:** MSBuild (.sln) + Vite (npm).
-   **Installation:** WiX Toolset (.msi) + PowerShell Dev Registration.

## Coding Standards (The "Rigor")
-   **Type Safety:** Strict static typing (C#) and Strict TypeScript.
-   **Error Handling:** Mandatory `try/catch` around SW API calls.
-   **Memory Management:** Explicitly release COM objects.

## Architecture Specifics
-   **Bridge Pattern:** All UI/Backend communication occurs via async JSON messages.
-   **Threading:** Solidworks API on Main Thread; UI on WebView2 Process.
-   **Frontend:** Functional React components + Hooks.

## Workflow Specifics
-   **Testing:**
    -   *Logic:* NUnit/XUnit.
    -   *Integration:* Manual verification in Solidworks (Task Panes, Property Pages).
-   **Deploy:** Generate `.msi` via WiX.
