# Pdgen - UML Diagram Generator - Configuration

:::warning
This is a work in progress. These are just ideas for future versions!
:::

`pdgen` is designed to be flexible and customizable to fit various development environments and preferences. This page explains how to configure `pdgen` to optimize its functionality for your projects.

## Basic Configuration

Upon installation, `pdgen` works out of the box with default settings that are suitable for most projects. However, you can customize these settings to better fit your specific needs.

### Setting Output Directory

You can specify the directory where the generated UML diagrams should be saved:

```python
pdgen --output-directory /path/to/your/directory
```

### Diagram Customization

`pdgen` allows you to customize the appearance of the generated diagrams. You can specify colors, fonts, and line styles:

```python
pdgen --color-scheme dark --font Arial --line-style dotted
```

## Advanced Configuration

For users who need more control over the generation process, `pdgen` offers several advanced configuration options.

### Include Private Methods

By default, `pdgen` does not include private methods in the diagrams. To include them, use the following flag:

```python
pdgen --include-private
```

### Filter Classes

If you want to generate diagrams for specific classes, you can use the filter option to specify which classes to include:

```python
pdgen --filter "Class1,Class2"
```

## Configuration File

Instead of passing options through the command line every time, you can create a configuration file named `pdgen.config.json` and store your preferences there:

```json
{
  "outputDirectory": "/path/to/your/directory",
  "colorScheme": "dark",
  "font": "Arial",
  "lineStyle": "dotted",
  "includePrivate": true,
  "filter": ["Class1", "Class2"]
}
```

Use the configuration file by specifying it when running `pdgen`:

```python
pdgen --config pdgen.config.json
```

## Tips for Effective Configuration

- **Consistency**: Keep your configuration consistent across your team to ensure that everyone generates diagrams in the same style and format.
- **Version Control**: Consider versioning your configuration file along with your codebase to track changes over time.

## Next Steps

Explore the [Advanced Features](/guide/advanced) to learn more about what `pdgen` can do for your project.