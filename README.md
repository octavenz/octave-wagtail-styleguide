# Octave Wagtail Styleguide

This is an internal styleguide application for Octave wagtail sites.

#### Installation

1) Add github repo dependency to pyproject.toml  

```
# pyproject.toml
octave-styleguide = { git = "https://github.com/octavenz/octave-wagtail-styleguide.git", tag = "0.1.3" }
```

2) Add module to INSTALLED_APPS    
```
INSTALLED_APPS = [
   'octave_styleguide',
]
```

3) Add settings
```
# Icon directory to parse for icons
OCTAVE_STYLEGUIDE_ICON_DIR = ROOT_DIR + '/frontend/icons/'

# Scss file there `$colors: ();` are configured
OCTAVE_STYLEGUIDE_COLORS_CONFIG_FILE = ROOT_DIR + '/frontend/scss/framework-config.scss'
```


4) Add styleguide menu to base.html
```
{# load the tag #}
{% load octave_styleguide_tags %}

{# render the tag before the closing body tag #}
    {% styleguide_menu %}
</body>
```

5) Load octave_styleguide.urls
```
if settings.DEBUG:
    from octave_styleguide.urls import urlpatterns as styleguide_urlpatterns

    urlpatterns += [
        url(r'', include(styleguide_urlpatterns)),
    ]
```

Styleguide will now be loaded. By default you will be able to access a page
 for  Typography, Colors and Icons. 

You can add more pages by adding a template to `app/templates/styleguide/example.html`.
This will be available at `localhost:XXXX/styleguide/example`.

There's no way to add context to requests yet.
