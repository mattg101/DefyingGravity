# Project Context: SW2URDF

This file defines the **Technical Context** for the generic SOPs. All agents must read this to understand the concrete inputs/outputs of their general roles.

## Technology Stack
-   **Core Language:** C# .NET.
-   **Framework:** .NET Framework / .NET Core (depending on SW Version).
-   **UI:** WPF (Presentation Framework), Xaml.
-   **Host Application:** Solidworks (Plugin/Add-in Development).
-   **API:** Solidworks API (COM Interop).
-   **Build System:** MSBuild (Visual Studio Solutions `.sln`).
-   **Installation:** WiX Toolset (.msi), COM Registration (`regasm`).

## Coding Standards (The "Rigor")
-   **Type Safety:** Strict static typing. Avoid `dynamic` unless interacting with late-bound COM objects.
-   **Error Handling:** Mandatory `try/catch` blocks around all Solidworks API calls to preventing crashing the host application.
-   **Memory Management:** Explicitly release COM objects (`Marshal.ReleaseComObject`) to prevent file locks or memory leaks.

## Architecture Specifics
-   **MVVM:** Use Model-View-ViewModel pattern for WPF UI.
-   **Threading:** Solidworks API calls affecting the model or UI **MUST** run on the Main Thread. Long-running tasks (Exports) must be backgrounded but marshal calls back to UI thread safely.

## Workflow Specifics
-   **Testing:**
    -   *Logic:* NUnit/XUnit.
    -   *Integration:* Manual verification in Solidworks (Task Panes, Property Pages).
-   **Deploy:** Generate `.msi` via WiX.
