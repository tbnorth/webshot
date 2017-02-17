# webshot
Simple python web service for taking browser screen shots in Windows

A web app. (javascript) can call the address provided by this server to trigger a
snapshot of the current browser window.

To get tiles fully loaded for each frame, attach to the appropriate signal:

```javascript
viewer.scene.globe.tileLoadProgressEvent.addEventListener(tiles_loaded);
```

which could be

```coffeescript
tiles_loaded = (tiles_to_do) ->

    if tiles_to_do > 0
        return

    anim_frame()
```


with `anim_frame()` being something like

```coffeescript
anim_frame = ->

    ai = anim_info

    if not ai.interval or ai.frames == 0
        return

    request = jQ.ajax
        url: "http://127.0.0.1:8123/do_shot"

    request.then ->

        console.log ai.frames
        anim_info.frames -= 1
        Cesium.JulianDate.addSeconds viewer.clock.currentTime, ai.interval,
            viewer.clock.currentTime
```
