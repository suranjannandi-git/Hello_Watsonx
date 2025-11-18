#!/bin/bash

set -e

echo "📌 Step 1: Removing '.env' from .gitignore..."

# Remove any line that exactly matches ".env"
sed -i '' '/^\.env$/d' .gitignore

echo "✔ Removed '.env' entry from .gitignore"
echo ""

echo "📌 Step 2: Running git clean -Xfd ..."
git clean -Xfd
echo "✔ Cleanup complete"
echo ""

echo "📌 Step 3: Adding '.env' back to .gitignore..."
echo ".env" >> .gitignore

echo "✔ .env added back to .gitignore"
echo ""
echo "🎉 All done!"
