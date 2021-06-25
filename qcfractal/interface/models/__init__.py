"""
Either pull in QCEl models or local models
"""

from typing import Union

from . import rest_models
from .common_models import (
    AutodocBaseSettings,
    Citation,
    ProtoModel,
    ComputeError,
    FailedOperation,
    KeywordSet,
    CompressionEnum,
    KVStore,
    Molecule,
    ObjectId,
    OptimizationInput,
    OptimizationResult,
    OptimizationProtocols,
    OptimizationSpecification,
    QCSpecification,
    AtomicInput,
    AtomicResult,
    AtomicResultProtocols,
    WavefunctionProperties,
    AllInputTypes,
    AllResultTypes,
    UserInfo,
    RoleInfo,
)

from .query_meta import InsertMetadata, DeleteMetadata, QueryMetadata
from .gridoptimization import GridOptimizationInput, GridOptimizationRecord
from .model_builder import build_procedure
from .model_utils import hash_dictionary, json_encoders, prepare_basis
from .records import DriverEnum, OptimizationRecord, ResultRecord, RecordStatusEnum
from .rest_models import ComputeResponse, rest_model
from .task_models import (
    ManagerStatusEnum,
    PythonComputeSpec,
    TaskRecord,
    PriorityEnum,
    SingleProcedureSpecification,
    OptimizationProcedureSpecification,
    AllProcedureSpecifications,
    AllServiceSpecifications,
)
from .torsiondrive import TorsionDriveInput, TorsionDriveRecord
