Title: {{ name }}
Date: {{ created_date_time.to_iso8601_string() }}
Modified: {{ updated_date_time.to_iso8601_string() }}
Category: posts
Tags: meetup
Slug: {{ slug_name }}
Authors: {{ hosts|join(', ') }}

{{ event_date_time.in_tz('America/Phoenix').to_day_datetime_string() }}

{% if status == 'upcoming' %}
**[RSVP on Meetup.com!]({{meetup_link}})**
{% endif %}

![Featured Photo]({{featured_photo_link}})


{{ description }}