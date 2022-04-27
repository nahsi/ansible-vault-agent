# vault-agent

Install, configure and maintain [vault-agent](https://www.vaultproject.io/docs/agent)

## Role Philosophy

Please see
[ansible-consul](https://github.com/nahsi/ansible-consul#role-philosophy).

## Role Variables

See [defaults/](https://github.com/nahsi/ansible-vault/blob/master/defaults/) for details and examples.

#### `vault_agent_version`

- version to use

#### `vault_agent_dirs`

- a map of directories to create
- default:

```yaml
vault_agent_dir: "/opt/vault"
vault_agent_dirs:
  main:
    path: "{{ vault_agent_dir }}"
  configs:
    path: "{{ vault_agent_dir }}/config.d"
  templates:
    path: "{{ vault_agent_dir }}/template.d"
  certs:
    path: "{{ vault_agent_dir }}/certs
  logs:
    path: "/var/log/vault-agent"
```

#### `vault_agent_config`

- main [configuration](https://www.vaultproject.io/docs/agent#configuration) file
- example: please see [defaults/example.yml](https://github.com/nahsi/ansible-vault-agent/blob/master/defaults/example.yml)

#### `vault_agent_templates`

- map of templates to create in `template.d` directory

#### `vault_agent_user`

- owner of vault-agent process and files
- default: `root`

#### `vault_agent_group`

- group of `vault_agent_user`
- default: `root`

#### `vault_agent_download_url`

- url to get vault-agent archive from
- default: `https://releases.hashicorp.com`

#### `vault_agent_service`

- openrc service file
- default: see [defaults/main.yml](https://github.com/nahsi/ansible-vault-agent/blob/master/defaults/main.yml)

#### `vault_agent_unitfile`

- systemd unit file
- default: see [defaults/main.yml](https://github.com/nahsi/ansible-vault-agent/blob/master/defaults/main.yml)

#### `skip_handlers`

- skip restart/reload - useful when building images with Packer
- default: `false`

## Tags

- `config` - update vault-agent unit/service file and sync configuration files

## Author

- **Anatoly Laskaris** - [nahsi](https://github.com/nahsi)
