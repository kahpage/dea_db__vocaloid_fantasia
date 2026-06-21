# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    active_events: list[int | str] = list(range(1, 14 + 1))

    i = 1  # ==== vocaloid_fantasia1 ====
    if i in active_events:
        event_name = f"vocaloid_fantasia{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d41280.738025225925!2d139.63619093655805!3d35.438584145120856!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cfc879b30db%3A0x8d76dbf7eaf7b911!2sYokohama%20Sanbo%20Hall%20Marineria!5e0!3m2!1sen!2sfr!4v1782062083547!5m2!1sen!2sfr",
                description="横浜産貿ホール　マリネリア全面",
                sources=[
                    Source(
                        "https://web.archive.org/web/20100805082022/http://vocaloid-fantasia.com/about.htm",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
        ]
        event = Event(
            aliases=["VOCALOID Fantasia", "VOCALOID Fantasia 1", "vocafan 1"],
            dates="2010.09.05",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20100805082022/http://vocaloid-fantasia.com/about.htm",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20100916113129/http://vocaloid-fantasia.com/circle1.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.10.21",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== vocaloid_fantasia2  ====
    if i in active_events:
        event_name = f"vocaloid_fantasia{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "02_vocafan02.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20110202163749/http://vocaloid-fantasia.com/gazou/vocafan02.jpg",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "02_vocafan02_2.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20251228215041/https://vocaloid-fantasia.com/gazou/vocafan02.jpg",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d41280.738025225925!2d139.63619093655805!3d35.438584145120856!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cfc879b30db%3A0x8d76dbf7eaf7b911!2sYokohama%20Sanbo%20Hall%20Marineria!5e0!3m2!1sen!2sfr!4v1782062083547!5m2!1sen!2sfr",
                description="横浜産貿ホール　マリネリア全面",
                sources=[
                    Source(
                        "https://web.archive.org/web/20110903030244/https://vocaloid-fantasia.com/about02.htm",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
        ]
        event = Event(
            aliases=[f"VOCALOID Fantasia {i}", f"vocafan {i}"],
            dates="2011.09.18",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20110903030244/https://vocaloid-fantasia.com/about02.htm",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20110914172653/http://vocaloid-fantasia.com/cir02-iciran-k.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with まくねけ文化祭.",
            # comments=None,
            last_edited="2026.10.21",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== vocaloid_fantasia3  ====
    if i in active_events:
        event_name = f"vocaloid_fantasia{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "03_vocafan03.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20120119054705/http://vocaloid-fantasia.com/gazou/vocafan03.jpg",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "03_vocafan3.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20120119095136/http://vocaloid-fantasia.com/gazou/vocafan3.jpg",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "03_vocafan03_2.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20251228215056/https://vocaloid-fantasia.com/gazou/vocafan03.jpg",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "03_haichi03.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20130530090329/http://vocaloid-fantasia.com/cir-iciran03.htm",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                iframe_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d41280.738025225925!2d139.63619093655805!3d35.438584145120856!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x60185cfc879b30db%3A0x8d76dbf7eaf7b911!2sYokohama%20Sanbo%20Hall%20Marineria!5e0!3m2!1sen!2sfr!4v1782062083547!5m2!1sen!2sfr",
                description="横浜産貿ホール　マリネリア全面",
                sources=[
                    Source(
                        "https://web.archive.org/web/20240228191408/https://vocaloid-fantasia.com/about03.htm",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
        ]
        event = Event(
            aliases=[f"VOCALOID Fantasia {i}", f"vocafan {i}"],
            dates="2012.09.23",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20240228191408/https://vocaloid-fantasia.com/about03.htm",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20251228222107/https://vocaloid-fantasia.com/cir-iciran03.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="Simultaneous with UTAU Fantasia.",
            # comments=None,
            last_edited="2026.10.21",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== vocaloid_fantasia  ====
    # if i in active_events:
    #     event_name = f"vocaloid_fantasia{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     iframe_url="",
    #         #     description="",
    #         #     sources=[
    #         #         Source(
    #         #             "",
    #         #             (ReliabilityTypes.Reliable, OriginTypes.Official),
    #         #         )
    #         #     ],
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=[f"VOCALOID Fantasia {i}", f"vocafan {i}"],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source("Date: ", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         # last_edited="2026.10.21",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]
    links = ["http://vocaloid-fantasia.com/index.htm", "https://x.com/vocafan0905"]

    event_group = EventGroup(
        aliases=["VOCALOID Fantasia", "vocafan"],
        events=events,
        media=media,
        links=links,
        sources=[
            Source(
                'Alias "vocafan": https://web.archive.org/web/20100925184844/http://vocaloid-fantasia.com/index.htm',
                (ReliabilityTypes.Reliable, OriginTypes.Official),
            ),
            # Source(
            #     "",
            #     (ReliabilityTypes.Reliable, OriginTypes.Official),
            # ),
        ],
        comments=None,
        description=None,
        last_edited="2026.10.21",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
