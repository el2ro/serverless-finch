'use strict';

const path = require('path');
const fs = require('fs');
const { zip } = require('zip-a-folder');

async function compressFolder(clientRoot) {
  let tmpDir = path.join(clientRoot, '..', '.tmp_upload');
  let tmpArchive = path.join(tmpDir, 'archive.zip');
  if (!fs.existsSync(tmpDir)) {
    fs.mkdirSync(tmpDir);
  }

  await zip(clientRoot, tmpArchive);

  return tmpDir;
}

module.exports = compressFolder;
