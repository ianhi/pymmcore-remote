from typing import Any, Callable, Protocol, runtime_checkable


@runtime_checkable
class PSignalInstance(Protocol):
    def connect(self, slot: Callable, **kwargs: Any) -> Any:
        ...

    def disconnect(self, slot: Callable, **kwargs: Any) -> Any:
        ...

    def emit(self, args: Any) -> Any:
        ...


@runtime_checkable
class PCoreSignaler(Protocol):

    # native MMCore callback events
    propertiesChanged: PSignalInstance
    propertyChanged: PSignalInstance
    channelGroupChanged: PSignalInstance
    configGroupChanged: PSignalInstance
    configSet: PSignalInstance
    systemConfigurationLoaded: PSignalInstance
    pixelSizeChanged: PSignalInstance
    pixelSizeAffineChanged: PSignalInstance
    stagePositionChanged: PSignalInstance
    XYStagePositionChanged: PSignalInstance
    xYStagePositionChanged: PSignalInstance  # alias
    exposureChanged: PSignalInstance
    SLMExposureChanged: PSignalInstance
    sLMExposureChanged: PSignalInstance  # alias

    # added for CMMCorePlus
    imageSnapped: PSignalInstance
    mdaEngineRegistered: PSignalInstance
    continuousSequenceAcquisitionStarted: PSignalInstance
    sequenceAcquisitionStarted: PSignalInstance
    sequenceAcquisitionStopped: PSignalInstance
    autoShutterSet: PSignalInstance
    configGroupDeleted: PSignalInstance
    configDeleted: PSignalInstance
    configDefined: PSignalInstance
    roiSet: PSignalInstance