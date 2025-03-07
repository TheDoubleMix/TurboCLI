# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]
### Added
- Undefined character parameter to hexdump function

### Changed
- The name of the module from "TurboCLI" to "turbocli" for ease of use
- _cli.py to _core.py
- "showhex" function name to "hexdump"

### Fixed
- The module (changed "from _cli..." to "from ._core..." )

### Removed
- Testing code that slipped in (showhex(b'\xde\xad\xbe\xef'))

## [0.2.0] - 2025-03-03 **NOTE: Broken**
### Changed
- The name of the module from "cli" to "TurboCLI"


## [0.1.0] - 2025-03-03 **NOTE: Broken**
### Added
- A Hex editor-like way to show binary data
