# Cascade

This [pelican](https://github.com/getpelican/pelican) plugin modifies article and page html to use bootstrap's default classes. This is especially handy if you want to write tables in markdown, since the `attr_list` extension does not play nice with `tables`.

## Requirements

* Beautifulsoup4 - install via `pip install beautifulsoup4`

## Features

Use `CASCADE_CSS` in your Pelican configuration file to pass a `{'css-selector': ['list-of-classes']}` dictionary to the plugin. Cascade will append `list-of-classes` to all tags that match `css-selector`. The selector can be as simple as a tag name (`table` or `p`) or as complicated as `a.menu:nth-of-type(3)` (see the [Beautifulsoup4 documentation](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors)).

## Example

```python
  BOOTSTRAPIFY_DEFAULT_CONFIG = {'figure': {'class': ['figure']}, 'figcaption': {'class': ['figure-caption', 'text-center']}, 'figure > img': {'class': ['figure-img', 'center-block']}}
  ```

    …this…

  ```html
  <figure>
    <img src="http://test.notreal/photos/testgallery/test.jpg" alt="some alt text"/>
    <figcaption>This is a test.</figcaption>
  </figure>
  ```

  …into…

  ```html
  <figure class="figure">
    <img alt="some alt text" class="figure-img img-responsive center-block" src="http://test.notreal/photos/testgallery/test.jpg"/>
    <figcaption class="text-center figure-caption">This is a test.</figcaption>
  </figure>
```

