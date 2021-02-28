import json
from flask import Blueprint, request, jsonify

with open("data.json", "r", encoding="utf8") as read_data:
    channels = json.load(read_data)

api_channels = Blueprint('api_channels', __name__)


@api_channels.route("/channels/all")
def list_channels():
    """ Lists all channels in the database. """

    return jsonify(channels)


@api_channels.route("/channels/<channel>")
def get_channel(channel):
    if "vote" in request.args:
        vote = str(request.args["vote"])

        if channel in channels:
            if vote == "upvote":
                channels[channel] += 1
            elif vote == "downvote":
                channels[channel] -= 1
            else:
                return "Vote word not recognised."

            with open("data.json", "w", encoding="utf8") as write_data:
                json.dump(channels, write_data, indent=4)

            return f"You {vote}d successfully the channel {channel}."
        else:
            return "Channel not found on the list."
    else:
        if channel in channels:
            return "Channel: " + channel
        else:
            return "Channel not found on the list."


@api_channels.route("/channels/<channel>/image.svg")
def img_channel(channel):
    if channel in channels:
        return f"""
                <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                width="52px" height="22px" viewBox="0 0 52 22" fill="none">
                <style>
                    .text {{
                        font-family: "Segoe UI", Ubuntu, Sans-Serif;
                        font-weight: bold;
                    }}
                </style>
                <rect x="0.5" y="0.5" height="99%" width="51" fill="none"/>
                    <g>
                        <text x="5" y="17" fill="#00b4f0" class="text">
                            {channels[channel]}
                        </text>
                    </g>
                </svg>
                """
    else:
        return "Channel not found on the list"