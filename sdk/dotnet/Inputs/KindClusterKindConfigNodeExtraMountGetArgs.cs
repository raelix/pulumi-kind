// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kind.Inputs
{

    public sealed class KindClusterKindConfigNodeExtraMountGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("containerPath")]
        public Input<string>? ContainerPath { get; set; }

        [Input("hostPath")]
        public Input<string>? HostPath { get; set; }

        public KindClusterKindConfigNodeExtraMountGetArgs()
        {
        }
        public static new KindClusterKindConfigNodeExtraMountGetArgs Empty => new KindClusterKindConfigNodeExtraMountGetArgs();
    }
}