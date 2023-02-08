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
    public sealed class KindClusterKindConfigNode
    {
        public readonly ImmutableArray<Outputs.KindClusterKindConfigNodeExtraMount> ExtraMounts;
        public readonly ImmutableArray<Outputs.KindClusterKindConfigNodeExtraPortMapping> ExtraPortMappings;
        public readonly string? Image;
        public readonly ImmutableArray<string> KubeadmConfigPatches;
        public readonly ImmutableDictionary<string, string>? Labels;
        public readonly string? Role;

        [OutputConstructor]
        private KindClusterKindConfigNode(
            ImmutableArray<Outputs.KindClusterKindConfigNodeExtraMount> extraMounts,

            ImmutableArray<Outputs.KindClusterKindConfigNodeExtraPortMapping> extraPortMappings,

            string? image,

            ImmutableArray<string> kubeadmConfigPatches,

            ImmutableDictionary<string, string>? labels,

            string? role)
        {
            ExtraMounts = extraMounts;
            ExtraPortMappings = extraPortMappings;
            Image = image;
            KubeadmConfigPatches = kubeadmConfigPatches;
            Labels = labels;
            Role = role;
        }
    }
}
