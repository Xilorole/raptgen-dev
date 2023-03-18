# Raptgen

```bash=poetry completions zsh > ~/.zfunc/_poetry
curl -sSL https://install.python-poetry.org | python3 -
poetry completions bash >> ~/.bash_completion
```

まずはこちらのページを読みながらdevcontainerの構築を始めている

[Developing inside a Container using Visual Studio Code Remote Development](https://code.visualstudio.com/docs/devcontainers/containers#_installation)

必要事項としては、
DockerとVSCodeとVSCodeのRemote Developmentツールが必要

see　→　<https://code.visualstudio.com/docs/devcontainers/containers#_installation>

devcontainer.jsonに関しては下記の2通りの配置方法がある

* `.devcontainer.json`
* `.devcontainer/devcontainer.json`

devcontainerの作り方は
<https://code.visualstudio.com/docs/devcontainers/create-dev-container>
を参照

## pre-building

[Developing inside a Container using Visual Studio Code Remote Development](https://code.visualstudio.com/docs/devcontainers/containers#_prebuilding-dev-container-images)で推奨されている。まずは下記を用意する必要がある。

* Node.js (version 14 or greater).
* The docker CLI.
* Python
* C/C++ compiler

その後

```bash
npm install -g @devcontainers/cli
```

を実行する。

github-actions を利用してpre-buildingをする場合は
<https://code.visualstudio.com/docs/devcontainers/devcontainer-cli>
を参照する。

devcontainer.jsonに

```json
{
  "build": {
    "dockerfile": "Dockerfile",
    "cacheFrom": "ghcr.io/your-org/your-image-name"
  },
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:1": {}
  }
}
```

を書いてdevcontainer CLIを利用して

```bash
devcontainer build --workspace-folder <my_repo> --push true --image-name <my_image_name>:<optional_image_version>
```

をすれば良さそう
