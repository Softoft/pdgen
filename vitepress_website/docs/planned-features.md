# Pdgen - Python UML Generator - Planned Features

:::warning
This is a work in progress. These are just ideas for future versions!
:::

## Configuration

`pdgen` is designed to be flexible and customizable to fit various development environments and preferences. This page
explains how to configure `pdgen` to optimize its functionality for your projects.

### Basic Configuration

Upon installation, `pdgen` works out of the box with default settings that are suitable for most projects. However, you
can customize these settings to better fit your specific needs.

#### Setting Output Directory

You can specify the directory where the generated UML diagrams should be saved:

```python
pdgen --output-directory /path/to/your/directory
```

#### Diagram Customization

`pdgen` allows you to customize the appearance of the generated diagrams. You can specify colors, fonts, and line
styles:

```python
pdgen --color-scheme dark --font Arial --line-style dotted
```

### Advanced Configuration

:::warning
This is a work in progress. These are just ideas for future versions!
:::

For users who need more control over the generation process, `pdgen` offers several advanced configuration options.

#### Include Private Methods

By default, `pdgen` does not include private methods in the diagrams. To include them, use the following flag:

```python
pdgen --include-private
```

#### Filter Classes

If you want to generate diagrams for specific classes, you can use the filter option to specify which classes to
include:

```python
pdgen --filter "Class1,Class2"
```

### Configuration File

Instead of passing options through the command line every time, you can create a configuration file named
`pdgen.config.json` and store your preferences there:

```json
{
  "outputDirectory": "/path/to/your/directory",
  "colorScheme": "dark",
  "font": "Arial",
  "lineStyle": "dotted",
  "includePrivate": true,
  "filter": [
    "Class1",
    "Class2"
  ]
}
```

Use the configuration file by specifying it when running `pdgen`:

```python
pdgen --config pdgen.config.json
```

### Tips for Effective Configuration

- **Consistency**: Keep your configuration consistent across your team to ensure that everyone generates diagrams in the
  same style and format.
- **Version Control**: Consider versioning your configuration file along with your codebase to track changes over time.

### Next Steps

Explore the [Advanced Features](/guide/advanced) to learn more about what `pdgen` can do for your project.
:::warning
This is a work in progress. These are just ideas for future versions!
:::

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

:::warning
This is a work in progress. These are just ideas for future versions!
:::

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
