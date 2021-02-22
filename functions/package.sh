#!/bin/sh

set -xeuo pipefail

rm -f packages/c1ws-controltower-lifecycle.zip

cd source && zip -r ../packages/c1ws-controltower-lifecycle.zip *

