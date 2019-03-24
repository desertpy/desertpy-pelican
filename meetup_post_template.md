Title: {{ name }}
Date: {{ event_date_time.to_iso8601_string() }}
Category: posts
Tags: meetup,{{ status }}
Slug: {{ slug_name }}
Authors: {{ hosts|join(', ') }}

<div class="meetup-time">
<i class="far fa-clock"></i> {{ event_date_time.in_tz('America/Phoenix').to_day_datetime_string() }}
</div>

<div class="meetup-venue">
<i class="fas fa-map-marked-alt"></i> {{ venue_name }}
</div>

{% if status == 'upcoming' %}

<div class="meetup-button">
<i class="fas fa-external-link-alt"></i> <a href="{{meetup_link}}">RSVP on Meetup.com!</a>
</div>

{% else %}

<em><a href="{{meetup_link}}">See past meeting details!</a></em>

{% endif %}

{% if featured_photo_link %}

![Featured Photo]({{featured_photo_link}})

{% endif %}

{{ description }}