// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kind.Inputs
{

    public sealed class KindClusterKindConfigGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("apiVersion", required: true)]
        public Input<string> ApiVersion { get; set; } = null!;

        [Input("containerdConfigPatches")]
        private InputList<string>? _containerdConfigPatches;
        public InputList<string> ContainerdConfigPatches
        {
            get => _containerdConfigPatches ?? (_containerdConfigPatches = new InputList<string>());
            set => _containerdConfigPatches = value;
        }

        [Input("kind", required: true)]
        public Input<string> Kind { get; set; } = null!;

        [Input("networking")]
        public Input<Inputs.KindClusterKindConfigNetworkingGetArgs>? Networking { get; set; }

        [Input("nodes")]
        private InputList<Inputs.KindClusterKindConfigNodeGetArgs>? _nodes;
        public InputList<Inputs.KindClusterKindConfigNodeGetArgs> Nodes
        {
            get => _nodes ?? (_nodes = new InputList<Inputs.KindClusterKindConfigNodeGetArgs>());
            set => _nodes = value;
        }

        public KindClusterKindConfigGetArgs()
        {
        }
        public static new KindClusterKindConfigGetArgs Empty => new KindClusterKindConfigGetArgs();
    }
}
