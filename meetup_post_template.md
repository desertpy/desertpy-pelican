Title: {{ name }}
Date: {{ created_date_time.to_iso8601_string() }}
Modified: {{ updated_date_time.to_iso8601_string() }}
Category: posts
Tags: meetup
Slug: {{ slug_name }}
Authors: {{ hosts|join(', ') }}

![Featured Photo]({{featured_photo_link}})

**[RSVP on Meetup.com!]({{meetup_link}})**

{{ description }}