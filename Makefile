.PHONY: all build bundle codex-bundle clean help list verify lint test test-unit
.DEFAULT_GOAL := help
.SECONDEXPANSION:
PYTHON ?= python3
PLUGIN_NAME := web-design-skills
SKILLS_ROOT := skills
SKILLS := $(sort $(patsubst $(SKILLS_ROOT)/%/SKILL.md,%,$(wildcard $(SKILLS_ROOT)/*/SKILL.md)))
BUILD_DIR := built
ZIP_FILES := $(addprefix $(BUILD_DIR)/,$(addsuffix -skill.zip,$(SKILLS)))
REPO_DIR := $(notdir $(CURDIR))
PARENT_DIR := $(dir $(CURDIR))
PACKAGED_ROOT := $(REPO_DIR)/$(SKILLS_ROOT)
skill_files = $(shell find $(SKILLS_ROOT)/$(1) -type f | sort)
help:
	@echo "$(REPO_DIR) Build System"
	@echo "Skills ($(words $(SKILLS))): $(SKILLS)"
$(BUILD_DIR):
	@mkdir -p $(BUILD_DIR)
$(BUILD_DIR)/%-skill.zip: $(BUILD_DIR) $$(call skill_files,$$*)
	@rm -f "$@"
	@cd "$(PARENT_DIR)" && zip -q -r "$(CURDIR)/$@" "$(PACKAGED_ROOT)/$*" -x "$(PACKAGED_ROOT)/$*/.DS_Store"
build: $(ZIP_FILES)
	@ls -lh $(BUILD_DIR)/*.zip
clean:
	@rm -rf "$(BUILD_DIR)"
verify:
	@$(PYTHON) scripts/verify_built_zips.py --build-dir $(BUILD_DIR) --skills-dir $(SKILLS_ROOT)
lint:
	@$(PYTHON) scripts/check_node_version.py || exit 1
	@markdownlint-cli2 "**/*.md" || exit 1
	@find . -name "*.yaml" -o -name "*.yml" | grep -v "^./built/" | xargs yamllint -c .yamllint.yml || exit 1
	@ruff check --select E,F,W,I --ignore E501 $$(find . -name "*.py" -not -path "./built/*") || exit 1
	@$(PYTHON) scripts/lint_skills.py || exit 1
	@$(PYTHON) scripts/validate_skills.py || exit 1
	@$(PYTHON) scripts/validate_plugin_manifests.py || exit 1
test-unit:
	@$(PYTHON) -m unittest discover -s tests -v
test: lint test-unit
list:
	@ls -lh $(BUILD_DIR)/*.zip 2>/dev/null || echo "No ZIPs built yet."
all: clean build
bundle: build
	@echo "Building $(PLUGIN_NAME)-plugin.zip..."
	@cd $(BUILD_DIR) && zip -q $(PLUGIN_NAME)-plugin.zip *-skill.zip
	@echo "  ✓ $(BUILD_DIR)/$(PLUGIN_NAME)-plugin.zip created"

codex-bundle: build
	@$(PYTHON) scripts/validate_plugin_manifests.py
	@echo "Building $(PLUGIN_NAME)-codex-plugin.zip..."
	@rm -f "$(BUILD_DIR)/$(PLUGIN_NAME)-codex-plugin.zip"
	@cd "$(PARENT_DIR)" && zip -q -r "$(CURDIR)/$(BUILD_DIR)/$(PLUGIN_NAME)-codex-plugin.zip" \
		"$(REPO_DIR)/.codex-plugin" "$(PACKAGED_ROOT)" \
		-x "$(REPO_DIR)/$(SKILLS_ROOT)/*/.DS_Store"
	@echo "  ✓ $(BUILD_DIR)/$(PLUGIN_NAME)-codex-plugin.zip created"
