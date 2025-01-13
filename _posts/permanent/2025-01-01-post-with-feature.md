---
title: Example Post With Features
author: your-value-here
permalink: /2025/1/post-with-features
lang: en
toc: true
map: true
map_popups:
  london_british_library: |
    <strong><a href='/travel/british-library'>British Library</a></strong>
tags:
 - document
---

{{ toc }}

## Link Preview

Move mouse over [this link]({% post_url permanent/2025-01-01-hello-world %})

## Map Integration

A map with places I visited in London.

{% include inline-map.html id="london_trip" locations="london_british_museum,london_british_library" popups=page.map_popups %}

Locations are all defined in `_data/locations.yml` like following:

{% highlight yml%}
sf_cal_academy:
  lat: 37.769773
  lng: -122.466134
  title: "California Academy of Sciences"
{% endhighlight %}

You can also add link to another post you write from the pin, like the "British Library" example shows. (I will document how to do this later)

## Multi Language Support

Navigate to [this link]({% post_url permanent/2025-01-01-sample-chinese %}) and see what happens to the "Previous", "Next" button(and some other labels).

## Other features

### Code highlight

See how many journals you have written in 2024(if you do):

{% highlight shell%}
myself@My-MacBook-Air journals % find 2024 -type f | wc -l
     366
{% endhighlight %}