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
    public sealed class KindClusterKindConfigNodeExtraMount
    {
        public readonly string? ContainerPath;
        public readonly string? HostPath;

        [OutputConstructor]
        private KindClusterKindConfigNodeExtraMount(
            string? containerPath,

            string? hostPath)
        {
            ContainerPath = containerPath;
            HostPath = hostPath;
        }
    }
}
