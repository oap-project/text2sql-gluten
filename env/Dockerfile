# This Dockerfile is used to construct image that can build and run texttosql model on x86 CPU platform.
# Based on https://github.com/bigPYJ1151/vllm/blob/384623538c081ed621b04c1eec107132920e5045/Dockerfile.cpu

FROM ubuntu:20.04

# http and https proxy setup
ENV http_proxy=http://proxy-us.intel.com:911
ENV https_proxy=http://proxy-us.intel.com:911

RUN apt-get update  -y \
    && apt-get install -y git wget vim numactl gcc-12 g++-12 python3 python3-pip default-jre \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 10 --slave /usr/bin/g++ g++ /usr/bin/g++-12

RUN pip install --upgrade pip \
    && pip install wheel packaging ninja setuptools>=49.4.0 numpy
    
# git proxy setup
RUN git config --global http.proxy http://proxy-us.intel.com:911

RUN git clone https://github.com/vllm-project/vllm.git /workspace/vllm

WORKDIR /workspace/vllm

# install requirements-cpu
RUN pip install -v -r requirements-cpu.txt --extra-index-url https://download.pytorch.org/whl/cpu

# install missing dependency in requirements-cpu.txt
RUN pip install pygments

# install vllm
RUN VLLM_TARGET_DEVICE=cpu python3 setup.py install

# install langchain
RUN pip install langchain

# install pyspark
RUN pip install pyspark

# dependency for pyspark-ai
RUN pip install pygments

RUN git clone https://github.com/PZD-CHINA/pyspark-ai.git /workspace/pyspark-ai

ENV PYTHONPATH="${PYTHONPATH}:/workspace/pyspark-ai"

RUN pip install notebook

CMD ["/bin/bash"]
