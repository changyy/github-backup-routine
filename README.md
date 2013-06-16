github-backup-routine
=====================

- 從 https://api.github.com/users/<username>/repos 取得清單
- 將所有的 repos clone 一份到本機端
  - ( test -e repo-name && cd repo-name && git pull ) || git clone https://github.com/<username>/<repo-name>.git
