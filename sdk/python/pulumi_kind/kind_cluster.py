# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['KindClusterArgs', 'KindCluster']

@pulumi.input_type
class KindClusterArgs:
    def __init__(__self__, *,
                 kind_config: Optional[pulumi.Input['KindClusterKindConfigArgs']] = None,
                 kubeconfig_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_image: Optional[pulumi.Input[str]] = None,
                 wait_for_ready: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a KindCluster resource.
        :param pulumi.Input['KindClusterKindConfigArgs'] kind_config: The kind_config that kind will use to bootstrap the cluster.
        :param pulumi.Input[str] kubeconfig_path: Kubeconfig path set after the the cluster is created or by the user to override defaults.
        :param pulumi.Input[str] name: The kind name that is given to the created cluster.
        :param pulumi.Input[str] node_image: The node_image that kind will use (ex: kindest/node:v1.23.4).
        :param pulumi.Input[bool] wait_for_ready: Defines wether or not the provider will wait for the control plane to be ready. Defaults to false
        """
        if kind_config is not None:
            pulumi.set(__self__, "kind_config", kind_config)
        if kubeconfig_path is not None:
            pulumi.set(__self__, "kubeconfig_path", kubeconfig_path)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if node_image is not None:
            pulumi.set(__self__, "node_image", node_image)
        if wait_for_ready is not None:
            pulumi.set(__self__, "wait_for_ready", wait_for_ready)

    @property
    @pulumi.getter(name="kindConfig")
    def kind_config(self) -> Optional[pulumi.Input['KindClusterKindConfigArgs']]:
        """
        The kind_config that kind will use to bootstrap the cluster.
        """
        return pulumi.get(self, "kind_config")

    @kind_config.setter
    def kind_config(self, value: Optional[pulumi.Input['KindClusterKindConfigArgs']]):
        pulumi.set(self, "kind_config", value)

    @property
    @pulumi.getter(name="kubeconfigPath")
    def kubeconfig_path(self) -> Optional[pulumi.Input[str]]:
        """
        Kubeconfig path set after the the cluster is created or by the user to override defaults.
        """
        return pulumi.get(self, "kubeconfig_path")

    @kubeconfig_path.setter
    def kubeconfig_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubeconfig_path", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The kind name that is given to the created cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nodeImage")
    def node_image(self) -> Optional[pulumi.Input[str]]:
        """
        The node_image that kind will use (ex: kindest/node:v1.23.4).
        """
        return pulumi.get(self, "node_image")

    @node_image.setter
    def node_image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_image", value)

    @property
    @pulumi.getter(name="waitForReady")
    def wait_for_ready(self) -> Optional[pulumi.Input[bool]]:
        """
        Defines wether or not the provider will wait for the control plane to be ready. Defaults to false
        """
        return pulumi.get(self, "wait_for_ready")

    @wait_for_ready.setter
    def wait_for_ready(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "wait_for_ready", value)


@pulumi.input_type
class _KindClusterState:
    def __init__(__self__, *,
                 client_certificate: Optional[pulumi.Input[str]] = None,
                 client_key: Optional[pulumi.Input[str]] = None,
                 cluster_ca_certificate: Optional[pulumi.Input[str]] = None,
                 completed: Optional[pulumi.Input[bool]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 kind_config: Optional[pulumi.Input['KindClusterKindConfigArgs']] = None,
                 kubeconfig: Optional[pulumi.Input[str]] = None,
                 kubeconfig_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_image: Optional[pulumi.Input[str]] = None,
                 wait_for_ready: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering KindCluster resources.
        :param pulumi.Input[str] client_certificate: Client certificate for authenticating to cluster.
        :param pulumi.Input[str] client_key: Client key for authenticating to cluster.
        :param pulumi.Input[str] cluster_ca_certificate: Client verifies the server certificate with this CA cert.
        :param pulumi.Input[bool] completed: Cluster successfully created.
        :param pulumi.Input[str] endpoint: Kubernetes APIServer endpoint.
        :param pulumi.Input['KindClusterKindConfigArgs'] kind_config: The kind_config that kind will use to bootstrap the cluster.
        :param pulumi.Input[str] kubeconfig: Kubeconfig set after the the cluster is created.
        :param pulumi.Input[str] kubeconfig_path: Kubeconfig path set after the the cluster is created or by the user to override defaults.
        :param pulumi.Input[str] name: The kind name that is given to the created cluster.
        :param pulumi.Input[str] node_image: The node_image that kind will use (ex: kindest/node:v1.23.4).
        :param pulumi.Input[bool] wait_for_ready: Defines wether or not the provider will wait for the control plane to be ready. Defaults to false
        """
        if client_certificate is not None:
            pulumi.set(__self__, "client_certificate", client_certificate)
        if client_key is not None:
            pulumi.set(__self__, "client_key", client_key)
        if cluster_ca_certificate is not None:
            pulumi.set(__self__, "cluster_ca_certificate", cluster_ca_certificate)
        if completed is not None:
            pulumi.set(__self__, "completed", completed)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if kind_config is not None:
            pulumi.set(__self__, "kind_config", kind_config)
        if kubeconfig is not None:
            pulumi.set(__self__, "kubeconfig", kubeconfig)
        if kubeconfig_path is not None:
            pulumi.set(__self__, "kubeconfig_path", kubeconfig_path)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if node_image is not None:
            pulumi.set(__self__, "node_image", node_image)
        if wait_for_ready is not None:
            pulumi.set(__self__, "wait_for_ready", wait_for_ready)

    @property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        Client certificate for authenticating to cluster.
        """
        return pulumi.get(self, "client_certificate")

    @client_certificate.setter
    def client_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_certificate", value)

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[pulumi.Input[str]]:
        """
        Client key for authenticating to cluster.
        """
        return pulumi.get(self, "client_key")

    @client_key.setter
    def client_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_key", value)

    @property
    @pulumi.getter(name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        Client verifies the server certificate with this CA cert.
        """
        return pulumi.get(self, "cluster_ca_certificate")

    @cluster_ca_certificate.setter
    def cluster_ca_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_ca_certificate", value)

    @property
    @pulumi.getter
    def completed(self) -> Optional[pulumi.Input[bool]]:
        """
        Cluster successfully created.
        """
        return pulumi.get(self, "completed")

    @completed.setter
    def completed(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "completed", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Kubernetes APIServer endpoint.
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter(name="kindConfig")
    def kind_config(self) -> Optional[pulumi.Input['KindClusterKindConfigArgs']]:
        """
        The kind_config that kind will use to bootstrap the cluster.
        """
        return pulumi.get(self, "kind_config")

    @kind_config.setter
    def kind_config(self, value: Optional[pulumi.Input['KindClusterKindConfigArgs']]):
        pulumi.set(self, "kind_config", value)

    @property
    @pulumi.getter
    def kubeconfig(self) -> Optional[pulumi.Input[str]]:
        """
        Kubeconfig set after the the cluster is created.
        """
        return pulumi.get(self, "kubeconfig")

    @kubeconfig.setter
    def kubeconfig(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubeconfig", value)

    @property
    @pulumi.getter(name="kubeconfigPath")
    def kubeconfig_path(self) -> Optional[pulumi.Input[str]]:
        """
        Kubeconfig path set after the the cluster is created or by the user to override defaults.
        """
        return pulumi.get(self, "kubeconfig_path")

    @kubeconfig_path.setter
    def kubeconfig_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kubeconfig_path", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The kind name that is given to the created cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nodeImage")
    def node_image(self) -> Optional[pulumi.Input[str]]:
        """
        The node_image that kind will use (ex: kindest/node:v1.23.4).
        """
        return pulumi.get(self, "node_image")

    @node_image.setter
    def node_image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_image", value)

    @property
    @pulumi.getter(name="waitForReady")
    def wait_for_ready(self) -> Optional[pulumi.Input[bool]]:
        """
        Defines wether or not the provider will wait for the control plane to be ready. Defaults to false
        """
        return pulumi.get(self, "wait_for_ready")

    @wait_for_ready.setter
    def wait_for_ready(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "wait_for_ready", value)


class KindCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kind_config: Optional[pulumi.Input[pulumi.InputType['KindClusterKindConfigArgs']]] = None,
                 kubeconfig_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_image: Optional[pulumi.Input[str]] = None,
                 wait_for_ready: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Create a KindCluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['KindClusterKindConfigArgs']] kind_config: The kind_config that kind will use to bootstrap the cluster.
        :param pulumi.Input[str] kubeconfig_path: Kubeconfig path set after the the cluster is created or by the user to override defaults.
        :param pulumi.Input[str] name: The kind name that is given to the created cluster.
        :param pulumi.Input[str] node_image: The node_image that kind will use (ex: kindest/node:v1.23.4).
        :param pulumi.Input[bool] wait_for_ready: Defines wether or not the provider will wait for the control plane to be ready. Defaults to false
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[KindClusterArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a KindCluster resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param KindClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KindClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kind_config: Optional[pulumi.Input[pulumi.InputType['KindClusterKindConfigArgs']]] = None,
                 kubeconfig_path: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_image: Optional[pulumi.Input[str]] = None,
                 wait_for_ready: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KindClusterArgs.__new__(KindClusterArgs)

            __props__.__dict__["kind_config"] = kind_config
            __props__.__dict__["kubeconfig_path"] = kubeconfig_path
            __props__.__dict__["name"] = name
            __props__.__dict__["node_image"] = node_image
            __props__.__dict__["wait_for_ready"] = wait_for_ready
            __props__.__dict__["client_certificate"] = None
            __props__.__dict__["client_key"] = None
            __props__.__dict__["cluster_ca_certificate"] = None
            __props__.__dict__["completed"] = None
            __props__.__dict__["endpoint"] = None
            __props__.__dict__["kubeconfig"] = None
        super(KindCluster, __self__).__init__(
            'kind:index/kindCluster:KindCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_certificate: Optional[pulumi.Input[str]] = None,
            client_key: Optional[pulumi.Input[str]] = None,
            cluster_ca_certificate: Optional[pulumi.Input[str]] = None,
            completed: Optional[pulumi.Input[bool]] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            kind_config: Optional[pulumi.Input[pulumi.InputType['KindClusterKindConfigArgs']]] = None,
            kubeconfig: Optional[pulumi.Input[str]] = None,
            kubeconfig_path: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            node_image: Optional[pulumi.Input[str]] = None,
            wait_for_ready: Optional[pulumi.Input[bool]] = None) -> 'KindCluster':
        """
        Get an existing KindCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_certificate: Client certificate for authenticating to cluster.
        :param pulumi.Input[str] client_key: Client key for authenticating to cluster.
        :param pulumi.Input[str] cluster_ca_certificate: Client verifies the server certificate with this CA cert.
        :param pulumi.Input[bool] completed: Cluster successfully created.
        :param pulumi.Input[str] endpoint: Kubernetes APIServer endpoint.
        :param pulumi.Input[pulumi.InputType['KindClusterKindConfigArgs']] kind_config: The kind_config that kind will use to bootstrap the cluster.
        :param pulumi.Input[str] kubeconfig: Kubeconfig set after the the cluster is created.
        :param pulumi.Input[str] kubeconfig_path: Kubeconfig path set after the the cluster is created or by the user to override defaults.
        :param pulumi.Input[str] name: The kind name that is given to the created cluster.
        :param pulumi.Input[str] node_image: The node_image that kind will use (ex: kindest/node:v1.23.4).
        :param pulumi.Input[bool] wait_for_ready: Defines wether or not the provider will wait for the control plane to be ready. Defaults to false
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KindClusterState.__new__(_KindClusterState)

        __props__.__dict__["client_certificate"] = client_certificate
        __props__.__dict__["client_key"] = client_key
        __props__.__dict__["cluster_ca_certificate"] = cluster_ca_certificate
        __props__.__dict__["completed"] = completed
        __props__.__dict__["endpoint"] = endpoint
        __props__.__dict__["kind_config"] = kind_config
        __props__.__dict__["kubeconfig"] = kubeconfig
        __props__.__dict__["kubeconfig_path"] = kubeconfig_path
        __props__.__dict__["name"] = name
        __props__.__dict__["node_image"] = node_image
        __props__.__dict__["wait_for_ready"] = wait_for_ready
        return KindCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> pulumi.Output[str]:
        """
        Client certificate for authenticating to cluster.
        """
        return pulumi.get(self, "client_certificate")

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> pulumi.Output[str]:
        """
        Client key for authenticating to cluster.
        """
        return pulumi.get(self, "client_key")

    @property
    @pulumi.getter(name="clusterCaCertificate")
    def cluster_ca_certificate(self) -> pulumi.Output[str]:
        """
        Client verifies the server certificate with this CA cert.
        """
        return pulumi.get(self, "cluster_ca_certificate")

    @property
    @pulumi.getter
    def completed(self) -> pulumi.Output[bool]:
        """
        Cluster successfully created.
        """
        return pulumi.get(self, "completed")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        Kubernetes APIServer endpoint.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="kindConfig")
    def kind_config(self) -> pulumi.Output[Optional['outputs.KindClusterKindConfig']]:
        """
        The kind_config that kind will use to bootstrap the cluster.
        """
        return pulumi.get(self, "kind_config")

    @property
    @pulumi.getter
    def kubeconfig(self) -> pulumi.Output[str]:
        """
        Kubeconfig set after the the cluster is created.
        """
        return pulumi.get(self, "kubeconfig")

    @property
    @pulumi.getter(name="kubeconfigPath")
    def kubeconfig_path(self) -> pulumi.Output[str]:
        """
        Kubeconfig path set after the the cluster is created or by the user to override defaults.
        """
        return pulumi.get(self, "kubeconfig_path")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The kind name that is given to the created cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeImage")
    def node_image(self) -> pulumi.Output[str]:
        """
        The node_image that kind will use (ex: kindest/node:v1.23.4).
        """
        return pulumi.get(self, "node_image")

    @property
    @pulumi.getter(name="waitForReady")
    def wait_for_ready(self) -> pulumi.Output[Optional[bool]]:
        """
        Defines wether or not the provider will wait for the control plane to be ready. Defaults to false
        """
        return pulumi.get(self, "wait_for_ready")

