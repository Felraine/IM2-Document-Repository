const APP_ID = 'fd6776f642cf4c4783a18c670407df19'
const CHANNEL = 'main'
const TOKEN = '007eJxTYFC6e3V56HK1Zu7AXuf0dptNJ1Ycfign32EQUbwl9qv9Zi0FhrQUM3NzszQzE6PkNJNkE3ML40RDi2QzcwMTA/OUNEPL1ONu6Q2BjAyVjHNYGBkgEMRnYchNzMxjYAAADboeGA=='
let UID;
const client = AgoraRTC.createClient({mode:'rtc', codec:'vp8'})

let localTracks = []
let remoteUsers = {}

let joinAndDisplayLocalStream = async () => {
    UID = await client.join(APP_ID, CHANNEL, TOKEN, null)

    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let player = `<div class="video-container" id="user-container-${UID}">
                    <div class="username-wrapper"><span class="user-name">My name</span></div>
                    <div class="video-player" id="user-${UID}"></div>
                </div>`
    document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)

    localTracks[1].play(`user-${UID}`)

    await client.publish([localTracks[0], localTracks[1]])
}

joinAndDisplayLocalStream()