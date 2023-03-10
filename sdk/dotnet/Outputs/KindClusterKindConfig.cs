// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kind.Outputs
{

    [OutputType]
    public sealed class KindClusterKindConfig
    {
        public readonly string ApiVersion;
        public readonly ImmutableArray<string> ContainerdConfigPatches;
        public readonly string Kind;
        public readonly Outputs.KindClusterKindConfigNetworking? Networking;
        public readonly ImmutableArray<Outputs.KindClusterKindConfigNode> Nodes;

        [OutputConstructor]
        private KindClusterKindConfig(
            string apiVersion,

            ImmutableArray<string> containerdConfigPatches,

            string kind,

            Outputs.KindClusterKindConfigNetworking? networking,

            ImmutableArray<Outputs.KindClusterKindConfigNode> nodes)
        {
            ApiVersion = apiVersion;
            ContainerdConfigPatches = containerdConfigPatches;
            Kind = kind;
            Networking = networking;
            Nodes = nodes;
        }
    }
}
