Title: {{ name }}
Date: {{ created_date_time.to_iso8601_string() }}
Modified: {{ updated_date_time.to_iso8601_string() }}
Category: posts
Tags: meetup
Slug: {{ slug_name }}
Authors: {{ hosts|join(', ') }}

[See on Meetup.com]({{link}})

![Featured Photo]({{featured_photo_link}})

{{ description }}