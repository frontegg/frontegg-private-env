#!/usr/bin/env python3
"""
GitHub App Setup Helper Script

This script helps you set up a GitHub App for the terraform-private-env sync workflow.
It will guide you through the process and extract the required values.
"""

import json
import sys
import os
from pathlib import Path

def print_header():
    print("=" * 60)
    print("GitHub App Setup for Terraform Private Env Sync")
    print("=" * 60)
    print()

def print_steps():
    print("Follow these steps to set up your GitHub App:")
    print()
    print("1. Go to: https://github.com/organizations/frontegg/settings/apps")
    print("2. Click 'New GitHub App'")
    print("3. Fill in the basic information:")
    print("   - App name: terraform-private-env-sync")
    print("   - Description: Sync private terraform environment to public repo")
    print("   - Homepage URL: https://github.com/frontegg/terraform-private-env")
    print()
    print("4. Set permissions:")
    print("   - Repository permissions:")
    print("     * Contents: Read and write")
    print("     * Metadata: Read-only")
    print("   - Organization permissions:")
    print("     * Members: Read-only (if needed)")
    print()
    print("5. Set 'Where can this GitHub App be installed' to 'Only on this account'")
    print("6. Click 'Create GitHub App'")
    print()
    print("7. After creation:")
    print("   - Note the App ID (you'll need this)")
    print("   - Click 'Generate private key' and download the .pem file")
    print("   - Go to 'Install App' and install on the organization")
    print("   - Choose repository access (All repositories or Only select repositories)")
    print("   - If selecting specific repos, choose:")
    print("     * frontegg/terraform-private-env (private)")
    print("     * frontegg/frontegg-private-env (public)")
    print()
    print("8. Note the Installation ID for the organization")
    print()

def extract_installation_ids():
    print("To get the Installation ID:")
    print("1. Go to your GitHub App settings")
    print("2. Click 'Install App'")
    print("3. Click on the organization installation")
    print("4. Note the URL:")
    print("   - It will look like: https://github.com/apps/terraform-private-env-sync/installations/12345678")
    print("   - The number at the end is the Installation ID")
    print()

def create_secrets_template():
    print("Required GitHub Secrets:")
    print()
    print("Add these secrets to your repository (Settings > Secrets and variables > Actions):")
    print()
    print("APP_ID")
    print("  - Value: Your GitHub App ID (number)")
    print()
    print("APP_PRIVATE_KEY")
    print("  - Value: The entire content of your downloaded .pem file")
    print("  - Include the BEGIN and END lines")
    print()
    print("APP_INSTALLATION_ID")
    print("  - Value: Installation ID for the organization installation")
    print("  - Get this from: https://github.com/apps/terraform-private-env-sync/installations/")
    print()

def validate_pem_file(pem_path):
    """Validate that the PEM file looks correct"""
    if not os.path.exists(pem_path):
        print(f"❌ PEM file not found: {pem_path}")
        return False
    
    with open(pem_path, 'r') as f:
        content = f.read()
    
    if "-----BEGIN RSA PRIVATE KEY-----" not in content:
        print("❌ PEM file doesn't contain RSA private key")
        return False
    
    if "-----END RSA PRIVATE KEY-----" not in content:
        print("❌ PEM file doesn't end with RSA private key")
        return False
    
    print("✅ PEM file looks valid")
    return True

def main():
    print_header()
    print_steps()
    extract_installation_ids()
    create_secrets_template()
    
    # Check if PEM file exists
    pem_files = list(Path('.').glob('*.pem'))
    if pem_files:
        print("Found PEM files:")
        for pem_file in pem_files:
            print(f"  - {pem_file}")
            validate_pem_file(pem_file)
    else:
        print("No PEM files found in current directory")
        print("Download your GitHub App private key and place it here for validation")
    
    print()
    print("After setting up the secrets, you can remove the old P2P_SYNC secret.")
    print("The workflow will now use the GitHub App for authentication.")

if __name__ == "__main__":
    main() 