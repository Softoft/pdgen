# Pdgen - Python UML Generator - Advanced Features

`pdgen` offers a range of advanced features that enable users to handle complex scenarios and enhance the utility of the
generated UML diagrams. This section explores these capabilities and provides guidance on how to leverage them to their
fullest potential.

## Custom Diagram Themes

`pdgen` supports custom themes for diagrams, allowing users to tailor the visual style to match their organization's
branding or personal preference. You can define your theme settings in the configuration file:

```json
{
  "theme": {
    "backgroundColor": "#ffffff",
    "lineColor": "#000000",
    "textColor": "#333333",
    "highlightColor": "#ff0000"
  }
}
```

## Diagram Layout Options

To better manage the layout of complex diagrams, `pdgen` offers several layout algorithms:

- **Horizontal Layout**: Spreads classes horizontally, suitable for wide diagrams.
- **Vertical Layout**: Spreads classes vertically, ideal for deep inheritance hierarchies.

```python
pdgen --layout horizontal
```

## Integration with IDEs

`pdgen` can be integrated into popular Integrated Development Environments (IDEs) like Visual Studio Code or PyCharm.
This integration allows you to generate UML diagrams directly from the IDE, enhancing your workflow. For example, to set
up `pdgen` with Visual Studio Code, add the following extension settings:

```json
{
  "pdgen.enable": true,
  "pdgen.autoUpdate": true
}
```

## Command Line Scripting

`pdgen` can be used as part of automation scripts or CI/CD pipelines. You can script diagram generation for automated
documentation updates:

```bash
pdgen --auto-generate --watch /path/to/python/code
```

## Dynamic Diagrams

For projects that require dynamic updates to diagrams as code changes, `pdgen` supports live updating features, which
automatically regenerate diagrams when the source code changes.

```python
pdgen --live-update
```

## Collaborative Features

`pdgen` supports collaborative features, allowing teams to work together on the same diagrams. This includes sharing
settings and collaborative editing through a shared server setup.

```python
pdgen --collaborate --server-url "http://yourserver.com"
```

## Next Steps

After exploring the advanced features, you may want to revisit the [Configuration](/guide/configuration) page to further
customize `pdgen` according to your needs.
