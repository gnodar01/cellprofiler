from cellprofiler.utilities.zmqrequest import AnalysisRequest


class SharedDictionaryRequest(AnalysisRequest):
    def __init__(self, analysis_id, module_num=-1):
        AnalysisRequest.__init__(self, analysis_id, module_num=module_num)
