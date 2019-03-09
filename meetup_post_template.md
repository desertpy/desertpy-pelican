Title: {{ name }}
Date: {{ created_date_time.to_iso8601_string() }}
Modified: {{ updated_date_time.to_iso8601_string() }}
Category: posts
Tags: meetup
Slug: {{ slug_name }}
Authors: {{ hosts|join(', ') }}

<div class="meetup-time">

{{ event_date_time.in_tz('America/Phoenix').to_day_datetime_string() }}

</div>

<div class="meetup-venue">
{{ venue_name }}
</div>

{% if status == 'upcoming' %}

<div class="meetup-button">

<em><a href="{{meetup_link}}">RSVP on Meetup.com!</a></em>

</div>

{% else %}

<em><a href="{{meetup_link}}">See past meeting details!</a></em>

{% endif %}

![Featured Photo]({{featured_photo_link}})


{{ description }}