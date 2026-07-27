# OLX Announcements Bot

`OlxBotAnuncios1.0` is a beta Windows desktop utility that helps repeat an OLX
announcement workflow. It presents a small form for announcement data, opens
Google Chrome, navigates the OLX "Desapega" page with keyboard and mouse
automation, uploads a fixed image filename, and repeats the flow for the
requested number of announcements.

This repository contains a Python application and generated Windows build
artifacts. It does not contain an HTML or JavaScript application. The tracked
`build/olxbot/xref-olxbot.html` file is generated PyInstaller cross-reference
output, not the application's user interface.

## Current Status

This is a beta/prototype project, not a production-ready OLX integration.

- No automated test suite is present.
- `teste.py` is only a one-line import smoke file; it is not a test runner.
- There is no `requirements.txt`, lockfile, configuration directory, or logs
  directory in the repository.
- The checked-in executable and build directories are historical artifacts and
  have not been validated on this machine.

## How It Works

1. The GUI collects a title, description, CEP, and announcement count.
2. It validates that the title and description are non-empty and that the CEP
   and count contain only decimal digits.
3. For each requested announcement, the script starts Chrome from
   `C:\Program Files\Google\Chrome\Application\chrome.exe`.
4. It opens `https://www2.olx.com.br/desapega` and uses `PyAutoGUI` keyboard
   input, fixed delays, and screen-image matching to fill the form.
5. It enters the category search text `Servi`, toggles a fixed sequence of
   options, enters the CEP, and locates `foto.png` to interact with the photo
   picker.
6. It types `Foto Anuncio.jpg` into the file picker, locates `enviar.png`,
   clicks it, waits, and closes the Chrome tab before continuing.

The script does not implement login, credential storage, upload selection from
the GUI, success verification, retries, or recovery from a changed page.

## Repository Structure

| Path | Purpose |
| --- | --- |
| `olxbot.py` | Main GUI and OLX screen-automation script. |
| `teste.py` | Minimal PySimpleGUI import file; no automated tests. |
| `foto.png` | Screen-image template used to find the photo control. |
| `enviar.png` | Screen-image template used to find the send control. |
| `Screenshot_1.png`, `Screenshot_2.png` | Checked-in screenshots. |
| `olxbot.spec` | PyInstaller specification for the `olxbot` executable. |
| `dist/` | Checked-in Windows executable and copied image assets. |
| `build/` | Checked-in PyInstaller build output, warnings, and cross-reference HTML. |
| `script.iss` | Inno Setup installer script with machine-specific source paths. |

## Prerequisites

The source workflow is designed for Windows and requires:

- Python installed and available as `python` in a terminal.
- Google Chrome installed at the exact path used by the script:
  `C:\Program Files\Google\Chrome\Application\chrome.exe`.
- An OLX account already signed in within the browser profile used by Chrome.
- A visible desktop session where PyAutoGUI can control the foreground window.
- The image templates `foto.png` and `enviar.png` available from the process
  working directory.
- A local file named `Foto Anuncio.jpg` available to the upload dialog.

## Local Run

Clone the repository using the canonical URL:

```bash
git clone https://github.com/xfelipealves/OlxBotAnuncios1.0.git
cd OlxBotAnuncios1.0
```

Create and activate a virtual environment on Windows:

```powershell
py -m venv .venv
\.venv\Scripts\Activate.ps1
```

Install the two third-party packages imported by the source:

```powershell
python -m pip install pyautogui PySimpleGUI
```

Run the GUI from the repository root so the image templates can be found:

```powershell
python olxbot.py
```

Enter the announcement values, confirm that Chrome and the expected OLX page
are ready, and click **Anunciar**. Keep the desktop and browser state
unchanged while the automation runs.

## Testing and Static Checks

There is no automated functional test suite. Running the application itself is
an interactive, Windows-only operation and was not performed as part of this
documentation update.

The source files can be checked without starting the GUI:

```bash
python -c "import ast, pathlib; [ast.parse(path.read_text(encoding='utf-8'), filename=str(path)) for path in (pathlib.Path('olxbot.py'), pathlib.Path('teste.py'))]"
```

This check validates Python syntax only; it does not verify installed
dependencies, Chrome behavior, OLX compatibility, image matching, or successful
announcement publication.

## Limitations and Operational Risks

- The automation is Windows-specific and depends on a hard-coded Chrome path.
- It relies on fixed `sleep` delays, keyboard focus, tab order, browser text,
  and screen-image matching. Browser updates, OLX layout changes, display
  scaling, or a different window state can make it fail or act on the wrong
  control.
- The category, option sequence, image control, send control, and upload name
  are hard-coded rather than configured.
- It does not confirm that an announcement was published and can continue
  after an intermediate failure.
- The source has no structured logging, exception handling, credential
  management, dependency lockfile, or reproducible build configuration.
- Recent Python versions emit a `SyntaxWarning` for the hard-coded Windows
  path in `olxbot.py`; this documentation pass does not change the source.
- `script.iss` contains absolute paths from the original development machine,
  so building the installer requires updating those paths first.
- The checked-in `dist/` and `build/` contents may be stale relative to the
  source and should not be treated as a release guarantee.

## Automation and OLX Terms of Service

Use this project only where the activity is permitted by OLX's current Terms of
Service, policies, and applicable law. Automated or repeated postings may be
restricted, require prior permission, trigger anti-abuse controls, or affect an
account. Do not use the tool to bypass CAPTCHAs, rate limits, access controls,
or other platform safeguards. Review every announcement, respect consent and
content rules, and stop if OLX blocks or challenges the activity. The project
does not provide legal or platform-policy advice.

## Contributing

Contributions are welcome through focused pull requests. Before opening one:

1. Describe the Windows and browser environment used to verify the change.
2. Explain any OLX workflow or screen-image assumptions.
3. Run the syntax check above and manually test only with an account and
   content you are authorized to use.
4. Do not commit passwords, session data, personal data, API keys, or other
   secrets.

## License

No license file or explicit open-source license is present in this repository.
Do not assume permission to use, modify, or redistribute the project beyond
rights granted by the copyright holder or applicable law.
