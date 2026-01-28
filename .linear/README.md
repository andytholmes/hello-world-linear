# Linear Integration

This directory contains configuration for the Linear + Cursor integration.

## Overview

The Linear Hello World project demonstrates an AI-native development workflow:

1. **Linear** - Planning & orchestration layer
2. **Cursor** - AI execution agent
3. **GitHub** - Source control plane
4. **Python** - Runtime platform

## Configuration Files

- `config.yaml` - Main configuration for Linear integration

## Workflow

1. Issues are created in Linear with appropriate labels
2. Cursor receives issues and creates feature branches
3. Cursor implements the changes based on issue context
4. Changes are pushed to GitHub
5. Pull requests are created and reviewed
6. Merged code is deployed

## Branch Naming

Branches follow the pattern: `cursor/{issue-id}-{issue-title-slug}`

Example: `cursor/AND-6-initial-project-setup`

## Commit Messages

Commits follow the pattern: `[{issue-id}] {message}`

Example: `[AND-6] Add initial project scaffolding`
