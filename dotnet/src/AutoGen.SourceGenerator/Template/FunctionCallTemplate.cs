﻿// ------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version: 17.0.0.0
//  
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
// ------------------------------------------------------------------------------
namespace AutoGen.SourceGenerator.Template
{
    using System.Linq;
    using System.Collections.Generic;
    using Microsoft.CodeAnalysis;
    using System;
    
    /// <summary>
    /// Class to produce the template output
    /// </summary>
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("Microsoft.VisualStudio.TextTemplating", "17.0.0.0")]
    internal partial class FunctionCallTemplate : FunctionCallTemplateBase
    {
        /// <summary>
        /// Create the template output
        /// </summary>
        public virtual string TransformText()
        {
            this.Write("﻿");
            this.Write(@"//----------------------
// <auto-generated>
//     This code was generated by a tool.
// </auto-generated>
//----------------------
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading.Tasks;
using System;
using AutoGen.Core;
using AutoGen.OpenAI.Extension;

");
if (!String.IsNullOrEmpty(NameSpace)) {
            this.Write("namespace ");
            this.Write(this.ToStringHelper.ToStringWithCulture(NameSpace));
            this.Write("\r\n{\r\n");
}
            this.Write("    public partial class ");
            this.Write(this.ToStringHelper.ToStringWithCulture(ClassName));
            this.Write("\r\n    {\r\n");
foreach (var functionContract in FunctionContracts) {
            this.Write("\r\n        private class ");
            this.Write(this.ToStringHelper.ToStringWithCulture(functionContract.GetFunctionSchemaClassName()));
            this.Write("\r\n        {\r\n");
foreach (var parameter in functionContract.Parameters) {
if (parameter.IsOptional) {
            this.Write("            [JsonPropertyName(@\"");
            this.Write(this.ToStringHelper.ToStringWithCulture(parameter.Name));
            this.Write("\")]\r\n\t\t\tpublic ");
            this.Write(this.ToStringHelper.ToStringWithCulture(parameter.Type));
            this.Write(" ");
            this.Write(this.ToStringHelper.ToStringWithCulture(parameter.Name));
            this.Write(" {get; set;} = ");
            this.Write(this.ToStringHelper.ToStringWithCulture(parameter.DefaultValue));
            this.Write(";\r\n");
} else {
            this.Write("            [JsonPropertyName(@\"");
            this.Write(this.ToStringHelper.ToStringWithCulture(parameter.Name));
            this.Write("\")]\r\n\t\t\tpublic ");
            this.Write(this.ToStringHelper.ToStringWithCulture(parameter.Type));
            this.Write(" ");
            this.Write(this.ToStringHelper.ToStringWithCulture(parameter.Name));
            this.Write(" {get; set;}\r\n");
}
}
            this.Write("        }\r\n\r\n        public ");
            this.Write(this.ToStringHelper.ToStringWithCulture(functionContract.ReturnType));
            this.Write(" ");
            this.Write(this.ToStringHelper.ToStringWithCulture(functionContract.GetFunctionWrapperName()));
            this.Write("(string arguments)\r\n        {\r\n            var schema = JsonSerializer.Deserializ" +
                    "e<");
            this.Write(this.ToStringHelper.ToStringWithCulture(functionContract.GetFunctionSchemaClassName()));
            this.Write(">(\r\n                arguments, \r\n                new JsonSerializerOptions\r\n     " +
                    "           {\r\n                    PropertyNamingPolicy = JsonNamingPolicy.CamelC" +
                    "ase,\r\n                });\r\n");
 var argumentLists = string.Join(", ", functionContract.Parameters.Select(p => $"schema.{p.Name}")); 
            this.Write("\r\n            return ");
            this.Write(this.ToStringHelper.ToStringWithCulture(functionContract.Name));
            this.Write("(");
            this.Write(this.ToStringHelper.ToStringWithCulture(argumentLists));
            this.Write(");\r\n        }\r\n\r\n        public FunctionContract ");
            this.Write(this.ToStringHelper.ToStringWithCulture(functionContract.GetFunctionContractName()));
            this.Write("\r\n        {\r\n            get => new FunctionContract\r\n            {\r\n");
if (functionContract.Namespace != null) {
            this.Write("                Namespace = @\"");
            this.Write(this.ToStringHelper.ToStringWithCulture(functionContract.Namespace));
            this.Write("\",\r\n");
}
if (functionContract.ClassName != null) {
            this.Write("                ClassName = @\"");
            this.Write(this.ToStringHelper.ToStringWithCulture(functionContract.ClassName));
            this.Write("\",\r\n");
}
if (functionContract.Name != null) {
            this.Write("                Name = @\"");
            this.Write(this.ToStringHelper.ToStringWithCulture(functionContract.Name));
            this.Write("\",\r\n");
}
if (functionContract.Description != null) {
            this.Write("                Description = @\"");
            this.Write(this.ToStringHelper.ToStringWithCulture(functionContract.Description.Replace("\"", "\"\"")));
            this.Write("\",\r\n");
}
if (functionContract.ReturnType != null) {
            this.Write("                ReturnType = typeof(");
            this.Write(this.ToStringHelper.ToStringWithCulture(functionContract.ReturnType));
            this.Write("),\r\n");
}
if (functionContract.ReturnDescription != null) {
            this.Write("                ReturnDescription = @\"");
            this.Write(this.ToStringHelper.ToStringWithCulture(functionContract.ReturnDescription));
            this.Write("\",\r\n");
}
if (functionContract.Parameters != null) {
            this.Write("                Parameters = new global::AutoGen.Core.FunctionParameterContract[]" +
                    "\r\n                {\r\n");
foreach (var parameter in functionContract.Parameters) {
            this.Write("                    new FunctionParameterContract\r\n                    {\r\n");
if (parameter.Name != null) {
            this.Write("                        Name = @\"");
            this.Write(this.ToStringHelper.ToStringWithCulture(parameter.Name));
            this.Write("\",\r\n");
}
if (parameter.Description != null) {
            this.Write("                        Description = @\"");
            this.Write(this.ToStringHelper.ToStringWithCulture(parameter.Description.Replace("\"", "\"\"")));
            this.Write("\",\r\n");
}
if (parameter.Type != null) {
            this.Write("                        ParameterType = typeof(");
            this.Write(this.ToStringHelper.ToStringWithCulture(parameter.Type));
            this.Write("),\r\n");
}
            this.Write("                        IsRequired = ");
            this.Write(this.ToStringHelper.ToStringWithCulture(parameter.IsOptional ? "false" : "true"));
            this.Write(",\r\n");
if (parameter.DefaultValue != null) {
            this.Write("                        DefaultValue = ");
            this.Write(this.ToStringHelper.ToStringWithCulture(parameter.DefaultValue));
            this.Write(",\r\n");
}
            this.Write("                    },\r\n");
}
            this.Write("                },\r\n");
}
            this.Write("            };\r\n        }\r\n");
}
            this.Write("    }\r\n");
if (!String.IsNullOrEmpty(NameSpace)) {
            this.Write("}\r\n");
}
            this.Write("\r\n");
            return this.GenerationEnvironment.ToString();
        }

public string NameSpace {get; set;}
public string ClassName {get; set;}
public IEnumerable<SourceGeneratorFunctionContract> FunctionContracts {get; set;}
public bool IsStatic {get; set;} = false;

    }
    #region Base class
    /// <summary>
    /// Base class for this transformation
    /// </summary>
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("Microsoft.VisualStudio.TextTemplating", "17.0.0.0")]
    internal class FunctionCallTemplateBase
    {
        #region Fields
        private global::System.Text.StringBuilder generationEnvironmentField;
        private global::System.CodeDom.Compiler.CompilerErrorCollection errorsField;
        private global::System.Collections.Generic.List<int> indentLengthsField;
        private string currentIndentField = "";
        private bool endsWithNewline;
        private global::System.Collections.Generic.IDictionary<string, object> sessionField;
        #endregion
        #region Properties
        /// <summary>
        /// The string builder that generation-time code is using to assemble generated output
        /// </summary>
        public System.Text.StringBuilder GenerationEnvironment
        {
            get
            {
                if ((this.generationEnvironmentField == null))
                {
                    this.generationEnvironmentField = new global::System.Text.StringBuilder();
                }
                return this.generationEnvironmentField;
            }
            set
            {
                this.generationEnvironmentField = value;
            }
        }
        /// <summary>
        /// The error collection for the generation process
        /// </summary>
        public System.CodeDom.Compiler.CompilerErrorCollection Errors
        {
            get
            {
                if ((this.errorsField == null))
                {
                    this.errorsField = new global::System.CodeDom.Compiler.CompilerErrorCollection();
                }
                return this.errorsField;
            }
        }
        /// <summary>
        /// A list of the lengths of each indent that was added with PushIndent
        /// </summary>
        private System.Collections.Generic.List<int> indentLengths
        {
            get
            {
                if ((this.indentLengthsField == null))
                {
                    this.indentLengthsField = new global::System.Collections.Generic.List<int>();
                }
                return this.indentLengthsField;
            }
        }
        /// <summary>
        /// Gets the current indent we use when adding lines to the output
        /// </summary>
        public string CurrentIndent
        {
            get
            {
                return this.currentIndentField;
            }
        }
        /// <summary>
        /// Current transformation session
        /// </summary>
        public virtual global::System.Collections.Generic.IDictionary<string, object> Session
        {
            get
            {
                return this.sessionField;
            }
            set
            {
                this.sessionField = value;
            }
        }
        #endregion
        #region Transform-time helpers
        /// <summary>
        /// Write text directly into the generated output
        /// </summary>
        public void Write(string textToAppend)
        {
            if (string.IsNullOrEmpty(textToAppend))
            {
                return;
            }
            // If we're starting off, or if the previous text ended with a newline,
            // we have to append the current indent first.
            if (((this.GenerationEnvironment.Length == 0) 
                        || this.endsWithNewline))
            {
                this.GenerationEnvironment.Append(this.currentIndentField);
                this.endsWithNewline = false;
            }
            // Check if the current text ends with a newline
            if (textToAppend.EndsWith(global::System.Environment.NewLine, global::System.StringComparison.CurrentCulture))
            {
                this.endsWithNewline = true;
            }
            // This is an optimization. If the current indent is "", then we don't have to do any
            // of the more complex stuff further down.
            if ((this.currentIndentField.Length == 0))
            {
                this.GenerationEnvironment.Append(textToAppend);
                return;
            }
            // Everywhere there is a newline in the text, add an indent after it
            textToAppend = textToAppend.Replace(global::System.Environment.NewLine, (global::System.Environment.NewLine + this.currentIndentField));
            // If the text ends with a newline, then we should strip off the indent added at the very end
            // because the appropriate indent will be added when the next time Write() is called
            if (this.endsWithNewline)
            {
                this.GenerationEnvironment.Append(textToAppend, 0, (textToAppend.Length - this.currentIndentField.Length));
            }
            else
            {
                this.GenerationEnvironment.Append(textToAppend);
            }
        }
        /// <summary>
        /// Write text directly into the generated output
        /// </summary>
        public void WriteLine(string textToAppend)
        {
            this.Write(textToAppend);
            this.GenerationEnvironment.AppendLine();
            this.endsWithNewline = true;
        }
        /// <summary>
        /// Write formatted text directly into the generated output
        /// </summary>
        public void Write(string format, params object[] args)
        {
            this.Write(string.Format(global::System.Globalization.CultureInfo.CurrentCulture, format, args));
        }
        /// <summary>
        /// Write formatted text directly into the generated output
        /// </summary>
        public void WriteLine(string format, params object[] args)
        {
            this.WriteLine(string.Format(global::System.Globalization.CultureInfo.CurrentCulture, format, args));
        }
        /// <summary>
        /// Raise an error
        /// </summary>
        public void Error(string message)
        {
            System.CodeDom.Compiler.CompilerError error = new global::System.CodeDom.Compiler.CompilerError();
            error.ErrorText = message;
            this.Errors.Add(error);
        }
        /// <summary>
        /// Raise a warning
        /// </summary>
        public void Warning(string message)
        {
            System.CodeDom.Compiler.CompilerError error = new global::System.CodeDom.Compiler.CompilerError();
            error.ErrorText = message;
            error.IsWarning = true;
            this.Errors.Add(error);
        }
        /// <summary>
        /// Increase the indent
        /// </summary>
        public void PushIndent(string indent)
        {
            if ((indent == null))
            {
                throw new global::System.ArgumentNullException("indent");
            }
            this.currentIndentField = (this.currentIndentField + indent);
            this.indentLengths.Add(indent.Length);
        }
        /// <summary>
        /// Remove the last indent that was added with PushIndent
        /// </summary>
        public string PopIndent()
        {
            string returnValue = "";
            if ((this.indentLengths.Count > 0))
            {
                int indentLength = this.indentLengths[(this.indentLengths.Count - 1)];
                this.indentLengths.RemoveAt((this.indentLengths.Count - 1));
                if ((indentLength > 0))
                {
                    returnValue = this.currentIndentField.Substring((this.currentIndentField.Length - indentLength));
                    this.currentIndentField = this.currentIndentField.Remove((this.currentIndentField.Length - indentLength));
                }
            }
            return returnValue;
        }
        /// <summary>
        /// Remove any indentation
        /// </summary>
        public void ClearIndent()
        {
            this.indentLengths.Clear();
            this.currentIndentField = "";
        }
        #endregion
        #region ToString Helpers
        /// <summary>
        /// Utility class to produce culture-oriented representation of an object as a string.
        /// </summary>
        public class ToStringInstanceHelper
        {
            private System.IFormatProvider formatProviderField  = global::System.Globalization.CultureInfo.InvariantCulture;
            /// <summary>
            /// Gets or sets format provider to be used by ToStringWithCulture method.
            /// </summary>
            public System.IFormatProvider FormatProvider
            {
                get
                {
                    return this.formatProviderField ;
                }
                set
                {
                    if ((value != null))
                    {
                        this.formatProviderField  = value;
                    }
                }
            }
            /// <summary>
            /// This is called from the compile/run appdomain to convert objects within an expression block to a string
            /// </summary>
            public string ToStringWithCulture(object objectToConvert)
            {
                if ((objectToConvert == null))
                {
                    throw new global::System.ArgumentNullException("objectToConvert");
                }
                System.Type t = objectToConvert.GetType();
                System.Reflection.MethodInfo method = t.GetMethod("ToString", new System.Type[] {
                            typeof(System.IFormatProvider)});
                if ((method == null))
                {
                    return objectToConvert.ToString();
                }
                else
                {
                    return ((string)(method.Invoke(objectToConvert, new object[] {
                                this.formatProviderField })));
                }
            }
        }
        private ToStringInstanceHelper toStringHelperField = new ToStringInstanceHelper();
        /// <summary>
        /// Helper to produce culture-oriented representation of an object as a string
        /// </summary>
        public ToStringInstanceHelper ToStringHelper
        {
            get
            {
                return this.toStringHelperField;
            }
        }
        #endregion
    }
    #endregion
}
