# Generate posts from Meetup Group
import shutil
from pathlib import Path

import requests
import pendulum
from jinja2 import Template
from slugify import slugify

MEETUP_EVENTS_URL = "https://api.meetup.com/" \
                    "Phoenix-Python-Meetup-Group/" \
                    "events?desc=true&" \
                    "photo-host=public&" \
                    "page=1000&" \
                    "sig_id=80307882&status=past%2Cupcoming%2Ccancelled&" \
                    "fields=featured_photo%2Cevent_hosts&" \
                    "no_earlier_than=2017-11-10T00%3A00%3A00.000&" \
                    "sig=2c2faed0dea584b35d4fce67f35faaca424cdc51"

events = requests.get(MEETUP_EVENTS_URL).json()

# Reset Destination Folder
meetup_posts_gen_folder = Path('content/meetup_posts_gen')
shutil.rmtree(meetup_posts_gen_folder)
Path.mkdir(Path('content/meetup_posts_gen'), exist_ok=True)

for event in events:
    # Bring variables to Python types
    name = event['name']
    created_date_time = pendulum.from_timestamp(event['created'] / 1000)
    updated_date_time = pendulum.from_timestamp(event['updated'] / 1000)
    event_date_time = pendulum.from_timestamp(event['time'] / 1000)
    venue_name = event['venue']['name']
    meetup_link = event['link']
    description = event['description']
    hosts = (host['name'] for host in event['event_hosts'])
    featured_photo_link = event.get('featured_photo', {}).get('photo_link', None)

    # Higher level logic
    slug_name = f"{slugify(name)}-{created_date_time.year}-{created_date_time.month:02d}"
    file_name = f"{created_date_time.year}-{created_date_time.month:02d}-{slugify(name)}.md"

    # Generate
    with open('meetup_post_template.md') as file:
        template = Template(file.read())

    output = template.render(
        name=name,
        created_date_time=created_date_time,
        updated_date_time=updated_date_time,
        event_date_time=event_date_time,
        venue_name=venue_name,
        meetup_link=meetup_link,
        description=description,
        hosts=hosts,
        featured_photo_link=featured_photo_link,
        slug_name=slug_name,
    )

    with open(Path(meetup_posts_gen_folder, file_name), 'w') as file:
        file.write(output)
