from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def set_system_volume(volume_level):
    # Get all active audio sessions
    sessions = AudioUtilities.GetAllSessions()

    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume.SetMasterVolume(volume_level, None)

# Example: Set system volume to 200% (2.0)
set_system_volume(2.0)  # 2.0 corresponds to 200% volume